# 📋 Diabetes Dataset Data Dictionary (generated with Gemini from Kaggle dataset description)

## 1. Demographics & Socio-economic
Basic background information about the patients.

* **`patient_id`**: Unique patient identifier.
* **`age`**: Age of patient in years.
* **`gender`**: Biological sex or gender identity.
* **`ethnicity`**: Ethnic background.
* **`education_level`**: Highest completed education.
* **`income_level`**: Income category.
* **`employment_status`**: Current work status.

---

## 2. Lifestyle Factors
Modifiable risk factors heavily influencing Type 2 Diabetes.

* **`smoking_status`**: Smoking behavior.
    * `Never` -> ✅ Low Risk
    * `Former` -> ⚠️ Moderate Risk
    * `Current` -> 🚨 **High Risk** (Vascular damage)
* **`alcohol_consumption_per_week`**: Drinks consumed per week.
    * *Range:* 0–30
    * *Note:* High intake (>14-20) increases caloric intake and liver stress.
* **`physical_activity_minutes_per_week`**: Weekly exercise duration.
    * *Range:* 0–600
    * *Note:* Lower values (<150 min) -> ⚠️ Sedentary risk.
* **`diet_score`**: Diet quality index.
    * *Range:* 0 (Worst) – 10 (Best)
    * *Note:* Low score -> 🚨 High sugar/fat intake risk.
* **`sleep_hours_per_day`**: Average daily sleep.
    * *Range:* 3–12
    * *Note:* <6 or >9 hours is associated with metabolic issues.
* **`screen_time_hours_per_day`**: Sedentary behavior proxy.
    * *Range:* 0–12
    * *Note:* High values correlate with low physical activity.

---

## 3. Medical History
Binary flags for comorbidities (0 = No, 1 = Yes).

* **`family_history_diabetes`**: Genetic predisposition.
    * `1`: Yes -> 🚨 **Strong Risk Factor**
* **`hypertension_history`**: History of high blood pressure.
    * `1`: Yes -> ⚠️ Increases cardiovascular risk.
* **`cardiovascular_history`**: History of heart issues.
    * `1`: Yes -> ⚠️ Common comorbidity.

---

## 4. Biometrics & Vitals
Physical measurements indicating metabolic health.

* **`bmi`**: Body Mass Index (kg/m²).
    * `18.5-24.9`: Normal -> ✅
    * `25-29.9`: Overweight -> ⚠️
    * `>30`: Obese -> 🚨 **High Risk** for Type 2 Diabetes.
* **`waist_to_hip_ratio`**: Fat distribution metric.
    * *Range:* 0.7–1.2
    * *Note:* >0.9 (Men) or >0.85 (Women) indicates abdominal obesity (Visceral Fat).
* **`systolic_bp`**: Systolic blood pressure (Upper number).
    * *Range:* 90–180
    * *Note:* >140 -> ⚠️ Hypertension.
* **`diastolic_bp`**: Diastolic blood pressure (Lower number).
    * *Range:* 60–120
    * *Note:* >90 -> ⚠️ Hypertension.
* **`heart_rate`**: Resting heart rate (bpm).
    * *Range:* 50–120
    * *Note:* >100 is Tachycardia.

---

## 5. Lab Results (Lipids)
Blood work related to cholesterol and heart health.

* **`cholesterol_total`**: Total cholesterol (mg/dL).
    * *Note:* >200 is borderline; >240 is high.
* **`hdl_cholesterol`**: "Good" cholesterol.
    * *Note:* Higher is better. <40 (Men) / <50 (Women) is bad.
* **`ldl_cholesterol`**: "Bad" cholesterol.
    * *Note:* >100 is bad; >160 is high risk.
* **`triglycerides`**: Fats in the blood.
    * *Note:* >150 -> ⚠️ High risk (strongly linked to diabetes).

---

## 6. Lab Results (Glucose & Insulin)
**CRITICAL SECTION** - Direct indicators of Diabetes.

* **`glucose_fasting`**: Blood sugar after not eating (mg/dL).
    * `< 100`: Normal -> ✅
    * `100 - 125`: Pre-Diabetes -> ⚠️
    * `> 126`: Diabetes -> 🚨 **Diagnostic Criteria**
* **`glucose_postprandial`**: Blood sugar after a meal (mg/dL).
    * `> 200`: Suggests Diabetes -> 🚨
* **`insulin_level`**: Blood insulin level (µU/mL).
    * *Range:* 2–50
    * *Note:* High levels suggest **Insulin Resistance** (Type 2 precursor).
* **`hba1c`**: Average blood sugar over past 3 months (%).
    * `< 5.7%`: Normal -> ✅
    * `5.7% - 6.4%`: Pre-Diabetes -> ⚠️
    * `> 6.5%`: Diabetes -> 🚨 **Gold Standard for Diagnosis**

---

## 7. Target Variables & Diagnosis
The outcomes to predict.

* **`diabetes_risk_score`**: Calculated probability/risk.
    * *Range:* 0–100
* **`diabetes_stage`**: Classification of disease status.
    * *Values:* 'No Diabetes', 'Pre-Diabetes', 'Type 1', 'Type 2', 'Gestational'
* **`diagnosed_diabetes`**: **TARGET VARIABLE**
    * `0`: No
    * `1`: Yes (Positive Diagnosis)