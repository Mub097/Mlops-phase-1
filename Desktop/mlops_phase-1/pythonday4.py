import os

dataset_path = os.getenv("DATASET_PATH", "default_dataset.csv")
print(f"Dataset path: {dataset_path}")