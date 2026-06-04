import pandas as pd
import json
import os
import glob

# Output directory for JSON files
OUTPUT_DIR = "output_json"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def excel_to_json(excel_path):
    """Convert an Excel file to JSON files (one per sheet)."""
    print(f"Processing: {excel_path}")

    xls = pd.ExcelFile(excel_path)
    base_name = os.path.splitext(os.path.basename(excel_path))[0]

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet_name)

        # Clean up: replace NaN with None for clean JSON
        df = df.where(pd.notnull(df), None)

        records = df.to_dict(orient="records")

        output_file = os.path.join(OUTPUT_DIR, f"{base_name}_{sheet_name}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2, default=str)

        print(f"  ✅ Sheet '{sheet_name}' → {output_file} ({len(records)} rows)")

def main():
    # Find all Excel files under data/
    excel_files = glob.glob("data/**/*.xlsx", recursive=True)

    if not excel_files:
        print("No Excel files found in data/ directory.")
        return

    for excel_file in excel_files:
        excel_to_json(excel_file)

    print(f"\nDone! JSON files saved to: {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
