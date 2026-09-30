from pathlib import Path
import pandas as pd


class DataLoader:
    """Load all the rows and columns from the csv"""

    def __init__(self, path: str | Path | None = None):
        self.path = (
            Path(path)
            if path is not None
            else Path(__file__).resolve().parents[1]
            / "data"
            / "ved_vehicle531.csv"
        )

    def load(self) -> pd.DataFrame:
        """Read the dataset when called, rather than when the module is imported"""
        return pd.read_csv(self.path, low_memory=False)
