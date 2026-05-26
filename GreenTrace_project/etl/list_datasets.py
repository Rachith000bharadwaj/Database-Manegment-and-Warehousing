import os
from pathlib import Path

DATASET_FOLDER = Path("D:/Bachelor of Technology/IIIT Dharwad/Rachith Bharadwaj T N 24BDS062/2nd Year/4th SEM/Database Manegment and Warehousing/DMW - Project/GreenTrace_project/datasets/green_trace_export/green_trace_export_20260310_195112")

files = sorted(os.listdir(DATASET_FOLDER))
print(f"Total files: {len(files)}")
for f in files:
    print(f)
