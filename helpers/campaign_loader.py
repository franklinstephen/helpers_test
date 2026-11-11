"""
Data loading utilities.
"""
import numpy as np


class CampaignDataLoader:
    """Generates synthetic campaign mail and response data for this exercise."""

    def __init__(self, spark, seed=5):
        self.spark = spark
        self.seed = seed

    def generate_mail_data(self):
        rng = np.random.default_rng(self.seed)
        channels = ["email", "direct_mail", "social", "search"]
        campaigns = ["CMP_A", "CMP_B", "CMP_C"]
        rows = []
        for i in range(2000):
            customer_id = f"C{int(rng.integers(0, 500)):04d}"
            campaign = str(rng.choice(campaigns))
            channel = str(rng.choice(channels))
            spend = round(float(rng.uniform(20, 400)), 2)
            rows.append((customer_id, campaign, channel, spend))
        return self.spark.createDataFrame(rows, ["customer_id", "campaign", "channel", "spend"])

    def generate_response_data(self, mail_df):
        rng = np.random.default_rng(self.seed + 1)
        sampled = mail_df.sample(fraction=0.3, seed=self.seed).collect()
        out = []
        for r in sampled:
            revenue = round(r["spend"] * float(rng.uniform(1.2, 4.0)), 2)
            out.append((r["customer_id"], r["campaign"], revenue))
        return self.spark.createDataFrame(out, ["customer_id", "campaign", "revenue"])
