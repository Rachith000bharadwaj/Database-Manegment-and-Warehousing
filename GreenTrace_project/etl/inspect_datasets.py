from pathlib import Path
import pandas as pd

DATASET_FOLDER = Path("D:/Bachelor of Technology/IIIT Dharwad/Rachith Bharadwaj T N 24BDS062/2nd Year/4th SEM/Database Manegment and Warehousing/DMW - Project/GreenTrace_project/datasets/green_trace_export/green_trace_export_20260310_195112")
CSV_FILES = sorted(DATASET_FOLDER.glob("*.csv"))

print(f"CSV dataset count: {len(CSV_FILES)}")

for csv_path in CSV_FILES:
    print("=" * 100)
    print(f"Dataset: {csv_path.name}")
    df = pd.read_csv(csv_path)

    print("Columns:")
    print(list(df.columns))

    print("\nData types:")
    print(df.dtypes)

    print("\nShape:")
    print(df.shape)

    print("\nSample rows:")
    print(df.head(3).to_string(index=False))
    print()
