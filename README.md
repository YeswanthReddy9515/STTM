# STTM Excel to JSON Pipeline

## Project Structure
```
sttm-project/
├── data/
│   └── sttm_mapping.xlsx       # Source Excel file (STTM mappings)
├── .github/
│   └── workflows/
│       └── excel_to_json.yml   # GitHub Actions pipeline
├── sttm_convert.py             # Python script to convert Excel → JSON
└── README.md
```

## How It Works

1. Push an `.xlsx` file to the `data/` folder on branch `poc_source`
2. GitHub Actions triggers automatically
3. `sttm_convert.py` converts each sheet in the Excel to a separate JSON file
4. A PR is automatically created from `auto/json-<run_id>` → `poc_target`

## Run Locally

```bash
# Install dependencies
pip install pandas openpyxl

# Run the conversion
python sttm_convert.py

# Output will be in: output_json/
```

## Branches
- `poc_source` → push your Excel files here
- `poc_target` → PR will be raised targeting this branch
