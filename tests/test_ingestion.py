"""Tests for ingestion.py.

TODO: Implement these tests for load_csv, load_json, and load_excel in
src/data_processing/ingestion.py.
"""
import pytest
import pandas as pd
from data_processing.ingestion import load_csv, load_json, load_excel


def test_load_csv_file_not_found(tmp_path):
    fake_path = tmp_path / "nonexistent.csv"
    with pytest.raises(FileNotFoundError):
        load_csv(fake_path)


def test_load_excel_missing_sheet(tmp_path):
    # Create a valid Excel file with one sheet
    file_path = tmp_path / "test.xlsx"
    df = pd.DataFrame({"a": [1, 2]})
    df.to_excel(file_path, sheet_name="Sheet1", index=False)

    # Try loading a sheet that does NOT exist
    with pytest.raises(ValueError):
        load_excel(file_path, sheet_name="MissingSheet")


def test_load_csv_invalid_format(tmp_path):
    bad_file = tmp_path / "bad.csv"
    bad_file.write_text("not,a,valid,csv\n1,2,3")

    df = load_csv(bad_file)

    # Pandas loads ragged CSVs and fills missing values with NaN
    assert isinstance(df, pd.DataFrame)
    assert df.isna().sum().sum() > 0


def test_load_json_invalid_json(tmp_path):
    bad_json = tmp_path / "bad.json"
    bad_json.write_text("{invalid json}")

    with pytest.raises(ValueError):
        load_json(bad_json)


def test_load_json_file_not_found(tmp_path):
    fake_path = tmp_path / "missing.json"
    with pytest.raises(FileNotFoundError):
        load_json(fake_path)


def test_load_excel_file_not_found(tmp_path):
    fake_path = tmp_path / "missing.xlsx"
    with pytest.raises(FileNotFoundError):
        load_excel(fake_path)


def test_load_excel_invalid_content(tmp_path):
    bad_excel = tmp_path / "bad.xlsx"
    bad_excel.write_text("not an excel file")

    # Excel readers raise a variety of exceptions depending on engine
    with pytest.raises(Exception):
        load_excel(bad_excel)
