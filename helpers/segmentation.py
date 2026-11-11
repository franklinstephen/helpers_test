"""
Customer segmentation utilities.
"""
from pyspark.sql import functions as F


class CustomerSegmenter:
    """Tags customers based on spend behavior."""

    @staticmethod
    def tag_high_value(df, threshold=500):
        """
        Tags each customer as 'high_value' if their total spend across all campaigns exceeds
        threshold, otherwise 'standard'.
        """
        totals = df.groupBy("customer_id").agg(F.sum("spend").alias("total_spend"))
        return totals.withColumn(
            "segment",
            F.when(F.col("total_spend") > threshold, "high_value").otherwise("standard")
        )
