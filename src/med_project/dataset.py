import os

from config import RAW_DATA_DIR
import kagglehub

# Download latest version
path = kagglehub.dataset_download(
    handle='mohankrishnathalla/diabetes-health-indicators-dataset', force_download=True
)

filename = 'diabetes_dataset.csv'
src_path = os.path.join(path, filename)

print(f'Dataset downloaded to: {src_path}')

dest_path = f'{RAW_DATA_DIR}/{filename}'
print(f'Moving dataset to: {dest_path}')

os.rename(src_path, f'{RAW_DATA_DIR}/{filename}')
