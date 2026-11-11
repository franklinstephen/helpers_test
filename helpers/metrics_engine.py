"""
Metric calculation utilities.
"""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


class MetricsEngine:
    """Computes campaign-level performance metrics."""

    @staticmethod
    def compute_campaign_summary(mail_df, response_df):
        spend = mail_df.groupBy("campaign").agg(F.sum("spend").alias("total_spend"))
        revenue = response_df.groupBy("campaign").agg(F.sum("revenue").alias("total_revenue"))
        summary = spend.join(revenue, "campaign", "left").fillna(0, subset=["total_revenue"])
        summary = summary.withColumn(
            "roi", (F.col("total_revenue") - F.col("total_spend")) / F.col("total_spend")
        )
        return summary

    @staticmethod
    def rank_by_roi(summary_df):
        w = Window.orderBy(F.col("roi").desc())
        return summary_df.withColumn("rank", F.rank().over(w))
