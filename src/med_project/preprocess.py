from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

from med_project.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

NUM_COLS = [
    'age',
    'alcohol_consumption_per_week',
    'physical_activity_minutes_per_week',
    'diet_score',
    'sleep_hours_per_day',
    'screen_time_hours_per_day',
    'bmi',
    'waist_to_hip_ratio',
    'systolic_bp',
    'diastolic_bp',
    'heart_rate',
    'cholesterol_total',
    'hdl_cholesterol',
    'ldl_cholesterol',
    'triglycerides',
    'glucose_fasting',
    'glucose_postprandial',
    'insulin_level',
    'hba1c',
]

CAT_COLS = [
    'family_history_diabetes',
    'hypertension_history',
    'cardiovascular_history',
]

ORDINAL_ENCODER_COLS = ['education_level', 'income_level', 'smoking_status']
ORDINAL_ENCODER_CATS = [
    ['No formal', 'Highschool', 'Graduate', 'Postgraduate'],
    ['Low', 'Lower-Middle', 'Middle', 'Upper-Middle', 'High'],
    ['Never', 'Former', 'Current'],
]
ONEHOT_ENCODER_COLS = ['employment_status', 'gender', 'ethnicity']


def read_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path).drop(['diabetes_stage', 'diagnosed_diabetes'], axis=1)

    return df


def build_preprocessor(
    num_columns: list[str],
    cat_columns: list[str],
    ordinal_enc_columns: list[str],
    ordinal_enc_categories: list[list[str]],
    one_hot_enc_columns: list[str],
) -> ColumnTransformer:
    preprocessor = ColumnTransformer(
        [
            (
                'num_pipeline',
                Pipeline(
                    [
                        ('median_imputer', SimpleImputer(strategy='median')),
                        ('scaler', StandardScaler()),
                    ]
                ),
                num_columns,
            ),
            (
                'cat_pipeline',
                Pipeline(
                    [
                        (
                            'most_frequent_imputer',
                            SimpleImputer(strategy='most_frequent'),
                        ),
                    ]
                ),
                cat_columns,
            ),
            (
                'ord_pipeline',
                Pipeline(
                    [
                        (
                            'most_frequent_imputer',
                            SimpleImputer(strategy='most_frequent'),
                        ),
                        (
                            'ordinal_encoder',
                            OrdinalEncoder(categories=ordinal_enc_categories),
                        ),
                    ]
                ),
                ordinal_enc_columns,
            ),
            (
                'onehot_pipeline',
                Pipeline(
                    [
                        (
                            'most_frequent_imputer',
                            SimpleImputer(strategy='most_frequent'),
                        ),
                        (
                            'ordinal_encoder',
                            OneHotEncoder(
                                drop='first',
                                sparse_output=False,
                                handle_unknown='ignore',
                            ),
                        ),
                    ]
                ),
                one_hot_enc_columns,
            ),
        ]
    )

    return preprocessor


def remove_outliers(df: pd.DataFrame) -> pd.DataFrame:
    diabetes = df
    # blood pressure
    impossible_bp = diabetes[
        (diabetes['systolic_bp'] <= diabetes['diastolic_bp'])
        | (diabetes['systolic_bp'] < 60)
        | (diabetes['systolic_bp'] > 300)
    ]

    # cholesterol
    cholesterol_error = diabetes[
        diabetes['cholesterol_total']
        < (diabetes['hdl_cholesterol'] + diabetes['ldl_cholesterol']) - 20
    ]

    # screen time, sleep hours, age
    sleep_error = diabetes[
        (diabetes['sleep_hours_per_day'] <= 0) | (diabetes['sleep_hours_per_day'] > 24)
    ]

    age_error = diabetes[(diabetes['age'] < 0) | (diabetes['age'] > 110)]

    screentime_error = diabetes[
        (diabetes['screen_time_hours_per_day'] < 0)
        | (diabetes['screen_time_hours_per_day'] > 24)
    ]

    # WHR (Waist to hip ratio)
    whr_error = diabetes[
        (diabetes['waist_to_hip_ratio'] < 0.5) | (diabetes['waist_to_hip_ratio'] > 2.5)
    ]

    index_to_drop = (
        set(impossible_bp.index)
        | set(cholesterol_error.index)
        | set(sleep_error.index)
        | set(age_error.index)
        | set(screentime_error.index)
        | set(whr_error.index)
    )

    diabetes_clean = diabetes.drop(index=list(index_to_drop)).copy()

    return diabetes_clean


def split_data(df: pd.DataFrame) -> tuple:
    target = 'diabetes_risk_score'
    test_size = 0.2
    random_state = 42

    y = df[target]
    X = df.drop(target, axis=1)

    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def format_col_names(cols: list[str]) -> list[str]:
    new_cols = []
    for col in cols:
        new_cols.append(col.split('__')[1])
    return new_cols


def save_data(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
):
    X_train.to_csv(PROCESSED_DATA_DIR / 'X_train.csv', index=False)
    X_test.to_csv(PROCESSED_DATA_DIR / 'X_test.csv', index=False)
    y_train.to_csv(PROCESSED_DATA_DIR / 'y_train.csv', index=False)
    y_test.to_csv(PROCESSED_DATA_DIR / 'y_test.csv', index=False)


def process_features(
    preprocessor: ColumnTransformer, X_train: pd.DataFrame, X_test: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    X_train_pre = preprocessor.fit_transform(X_train)
    X_test_pre = preprocessor.transform(X_test)
    feature_names = format_col_names(preprocessor.get_feature_names_out())

    X_train_pre_df = pd.DataFrame(X_train_pre, columns=feature_names)
    X_test_pre_df = pd.DataFrame(X_test_pre, columns=feature_names)

    return X_train_pre_df, X_test_pre_df


def preprocess_data():
    df = read_data(RAW_DATA_DIR / 'diabetes_dataset.csv')

    df_cleaned = remove_outliers(df)

    y_train: pd.Series
    y_test: pd.Series
    X_train, X_test, y_train, y_test = split_data(df_cleaned)

    preprocessor = build_preprocessor(
        NUM_COLS,
        CAT_COLS,
        ORDINAL_ENCODER_COLS,
        ORDINAL_ENCODER_CATS,
        ONEHOT_ENCODER_COLS,
    )

    X_train_pre_df, X_test_pre_df = process_features(preprocessor, X_train, X_test)

    save_data(X_train_pre_df, X_test_pre_df, y_train, y_test)


if __name__ == '__main__':
    preprocess_data()
