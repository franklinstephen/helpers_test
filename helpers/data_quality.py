"""
Data quality utilities.
"""
from pyspark.sql import functions as F


class DataQualityChecker:
    """Schema checks for incoming DataFrames."""

    @staticmethod
    def validate_schema(df, expected_columns):
        actual = set(df.columns)
        expected = set(expected_columns)
        missing = expected - actual
        extra = actual - expected
        return {"missing": sorted(missing), "extra": sorted(extra), "ok": not missing}


def flag_null_rates(df, threshold=0.05):
    """
    Standalone helper (deliberately not a method on DataQualityChecker) that returns the null
    rate for every column in df, flagging any column whose null rate exceeds `threshold`.
    """
    total = df.count()
    report = {}
    for c in df.columns:
        null_count = df.filter(F.col(c).isNull()).count()
        rate = null_count / total if total else 0
        report[c] = {"null_rate": round(rate, 4), "flagged": rate > threshold}
    return report
