"""Extract one vehicle's driving records from the raw VED weekly CSVs.

Source: Vehicle Energy Dataset (VED), https://github.com/gsoh/VED
Download VED_DynamicData_Part1.7z and Part2.7z from the repo's Data/ folder,
extract both into one folder, then run:

    uv run python src/extract_ved.py --src path/to/extracted_csvs
"""

from argparse import ArgumentParser
from pathlib import Path
import pandas as pd

COLUMNS = [
    "DayNum",
    "VehId",
    "Trip",
    "Timestamp(ms)",
    "Vehicle Speed[km/h]",
    "MAF[g/sec]",
]


def extract_vehicle(src: Path, veh_id: int) -> pd.DataFrame:
    """Read every VED_*_week.csv in src and keep only the rows for veh_id"""
    files = sorted(src.glob("VED_*_week.csv"))
    if not files:
        raise FileNotFoundError(f"No VED_*_week.csv files found in {src}")

    parts = []
    for file in files:
        week = pd.read_csv(file, usecols=COLUMNS, low_memory=False)
        parts.append(week[week["VehId"] == veh_id])
    return pd.concat(parts, ignore_index=True).sort_values(
        ["Trip", "Timestamp(ms)"], ignore_index=True
    )


def main() -> None:
    parser = ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--src", type=Path, required=True, help="folder of extracted VED weekly CSVs")
    parser.add_argument("--veh", type=int, default=531, help="VehId to extract (default: 531)")
    parser.add_argument("--out", type=Path, default=None, help="output CSV path")
    args = parser.parse_args()

    out = args.out or Path(__file__).resolve().parents[1] / "data" / f"ved_vehicle{args.veh}.csv"
    df = extract_vehicle(args.src, args.veh)
    df.to_csv(out, index=False)
    print(f"Saved {len(df):,} rows from {df['Trip'].nunique()} trips to {out}")


if __name__ == "__main__":
    main()
