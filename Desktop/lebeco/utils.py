import json
import pandas as pd

def load_data(filepath="data.json"):
    """Loads the economic crisis dataset from a JSON file."""
    with open(filepath, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def analyze_question(df, question):
    """Analyzes the dataset based on the user's selected dropdown question."""
    
    # 1. Peak Inflation
    if "inflation percentage peak" in question:
        peak_row = df.loc[df["inflation_cpi_pct_yoy"].idxmax()]
        answer = f"The highest annual inflation rate recorded in the dataset is **{peak_row['inflation_cpi_pct_yoy']}%**, and it occurred in **{int(peak_row['year'])}**[cite: 1]."
        return answer, peak_row
        
    # 2. Exchange Rate Evolution
    elif "exchange rate" in question and "2019 to 2023" in question:
        answer = "The Lebanese Pound (LBP) maintained an official peg around 1,507.5 per USD until 2019, after which it experienced severe depreciation starting in 2020, reaching 89,500 LBP per USD by 2023[cite: 1]."
        return answer, None
        
    # 3. Negative Inflation Years
    elif "negative inflation years" in question:
        neg_df = df[df["inflation_cpi_pct_yoy"] < 0]
        answer = "The following years recorded negative inflation (deflationary periods) according to the dataset[cite: 1]:"
        return answer, neg_df
        
    # 4. Overall Trend Summary
    elif "overall trend summary" in question:
        answer = """
        - **Pre-Crisis Era (2009–2019):** Stable exchange rates pegged at ~1,507.5 LBP/USD with low single-digit inflation[cite: 1].
        - **Crisis Onset (2020):** Immediate surge in inflation (84.8%) and beginning of currency devaluation[cite: 1].
        - **Peak Collapse (2023):** Inflation peaked destructively at over **221.3%**, while the exchange rate plateaued at **89,500 LBP/USD**[cite: 1].
        - **Post-Peak Stabilization (2024–2025):** Inflation rates decelerated down to 25.1% by 2025[cite: 1].
        """
        return answer, None

    # 5. NEW: Average inflation during the peak crisis period (2020-2025)
    elif "average inflation" in question:
        crisis_df = df[df["year"] >= 2020]
        avg_infl = crisis_df["inflation_cpi_pct_yoy"].mean()
        answer = f"The average annual inflation rate during the heavy crisis period (2020–2025) was **{avg_infl:.2f}%**[cite: 1]."
        return answer, crisis_df

    # 6. NEW: When did the exchange rate first break the peg?
    elif "break the peg" in question or "official peg" in question:
        peg_broken = df[df["exchange_rate_lbp_per_usd"] > 1507.5].iloc[0]
        answer = f"The Lebanese Pound officially broke its long-standing peg of 1,507.5 LBP/USD in **{int(peg_broken['year'])}**, jumping to **{peg_broken['exchange_rate_lbp_per_usd']} LBP per USD**[cite: 1]."
        return answer, None

    # 7. NEW: Compare inflation in 2009 vs 2023
    elif "Compare inflation in 2009" in question:
        val_2009 = df[df["year"] == 2009]["inflation_cpi_pct_yoy"].values[0]
        val_2023 = df[df["year"] == 2023]["inflation_cpi_pct_yoy"].values[0]
        answer = f"In 2009, inflation was **{val_2009}%**, whereas by 2023 it skyrocketed to **{val_2023}%**, representing an extreme magnification of economic distress[cite: 1]."
        return answer, None

    # 8. NEW: Stable pre-crisis years list
    elif "stable pre-crisis" in question:
        stable_df = df[df["year"] < 2020]
        answer = "The pre-crisis period (2009–2019) characterized by a stable exchange rate of 1,507.5 LBP/USD includes the following data points[cite: 1]:"
        return answer, stable_df
        
    return "Please select a valid question from the dropdown menu.", None