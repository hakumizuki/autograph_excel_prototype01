for %%a in (converted_csv_files/*.csv) do (
    python3 autograph.py %%a
)