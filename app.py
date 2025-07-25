import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df_women = pd.read_csv("df_women.csv")
df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")

st.title("📊 Crime Analysis Dashboard - India")

# Sidebar Inputs
state = st.sidebar.selectbox("Select a State", df_women["States"].unique())
analysis_type = st.sidebar.radio("Choose Analysis Type:", [
    "Crime Against Women",
    "Gender-wise Crime Statistics",
    "Year-wise Crime Trends"
])

# -------------------------------
# 1️⃣ CRIME AGAINST WOMEN
# -------------------------------
if analysis_type == "Crime Against Women":
    st.subheader(f"🔍 Crimes Against Women in {state}")
    
    # Display full state data transposed
    data = df_women[df_women['States'] == state].T
    st.dataframe(data)

    # All crime-related columns except totals/population
    crime_cols = [
        'Murder_with_Rape/Gang_Rape', 'Dowry_Deaths', 'Abetment_to_Suicide_of_Women',
        'Miscarriage', 'Acid_Attack', 'Cruelty_by_Husband_or_his_relatives',
        'Kidnapping_&_Abduction_of_Women_(Total)', 'Procuration_of_Minor_Girls',
        'women_Trafficking', 'Selling_of_Minor_Girls', 'Rape_cases',
        'Assault_on_Women_with_Intent_to_Outrage_her_Modesty', 'Insult_to_the_Modesty_of_Women',
        'Dowry_prohibition', 'Procuring,_inducing_Children_for_the_sake_of_prostitution',
        'Publishing_or_Transmitting_of_Sexually_Explicit_Material',
        'Women_Centric_Cyber_Crimes_(Ex._Blackmailing/_Defamation/Morphing/_Fake_Profile)'
    ]

    # Plot bar chart of crime types
    crime_data = df_women[df_women["States"] == state][crime_cols].T
    crime_data.columns = ["Cases"]
    st.bar_chart(crime_data)

    # Total crimes and crime rate
    total_crimes = df_women[df_women["States"] == state]["Total_Crimes"].values[0]
    crime_rate = df_women[df_women["States"] == state]["Crimes_Per_Lakh_Women"].values[0]
    
    st.metric("📌 Total Crimes Against Women", int(total_crimes))
    st.metric("👩 Crimes per Lakh Women", f"{crime_rate:.2f}")

    # Crime Rate Ranking
    ranked_df = df_women.sort_values("Crimes_Per_Lakh_Women", ascending=False).reset_index(drop=True)
    ranked_df["Rank"] = ranked_df.index + 1
    current_rank = ranked_df[ranked_df["States"] == state]["Rank"].values[0]
    st.metric("📈 Rank (Crime Rate)", current_rank)

    # Compare with others
    higher_states = ranked_df[ranked_df["Crimes_Per_Lakh_Women"] > crime_rate]["States"].tolist()
    lower_states = ranked_df[ranked_df["Crimes_Per_Lakh_Women"] < crime_rate]["States"].tolist()

    st.write(f"🟥 States with Higher Crime per Lakh Women ({len(higher_states)}):")
    st.write(", ".join(higher_states))

    st.write(f"🟩 States with Lower Crime per Lakh Women ({len(lower_states)}):")
    st.write(", ".join(lower_states))

    # Percentile
    percentile = (ranked_df[ranked_df["States"] == state].index[0] / len(ranked_df)) * 100
    st.metric("🎯 Percentile Rank", f"{100 - percentile:.2f} percentile")

# -------------------------------
# 2️⃣ GENDER-WISE VICTIM ANALYSIS
# -------------------------------
elif analysis_type == "Gender-wise Crime Statistics":
    st.subheader(f"🧑‍🤝‍🧑 Gender-wise Victim Data in {state}")
    
    row = df2[df2["States"] == state]
    st.write(row.T)

    # Plot bar chart
    st.bar_chart({
        "Male Victims": int(row["Total_victims_M"]),
        "Female Victims": int(row["Total_victims_F"])
    })

    # Ranking
    df2["Total_victims"] = df2["Total_victims_M"] + df2["Total_victims_F"]
    ranked_df2 = df2.sort_values("Total_victims", ascending=False).reset_index(drop=True)
    ranked_df2["Rank"] = ranked_df2.index + 1
    current_total = row["Total_victims"].values[0]
    current_rank = ranked_df2[ranked_df2["States"] == state]["Rank"].values[0]

    st.metric("📊 Rank (Total_victims)", current_rank)

    higher_states = ranked_df2[ranked_df2["Total_victims"] > current_total]["States"].tolist()
    lower_states = ranked_df2[ranked_df2["Total_victims"] < current_total]["States"].tolist()

    st.write(f"🔺 States with More Victims: ({len(higher_states)})")
    st.write(", ".join(higher_states))

    st.write(f"🔻 States with Fewer Victims: ({len(lower_states)})")
    st.write(", ".join(lower_states))

    percentile2 = (ranked_df2[ranked_df2["States"] == state].index[0] / len(ranked_df2)) * 100
    st.metric("🎯 Percentile Rank", f"{100 - percentile2:.2f} percentile")

# -------------------------------
# 3️⃣ YEAR-WISE TREND ANALYSIS
# -------------------------------
elif analysis_type == "Year-wise Crime Trends":
    st.subheader(f"📈 Crime Trends (2020–2022) for {state}")
    
    row = df1[df1["States"] == state]
    years = ['2020', '2021', '2022']
    values = row[years].values.flatten()

    trend_df = pd.DataFrame({
        "Year": years,
        "Cases": values
    })
    st.line_chart(trend_df.set_index("Year"))

# -------------------------------
# 📥 CSV DOWNLOAD BUTTON
# -------------------------------
csv_data = df_women[df_women["States"] == state].to_csv(index=False)
st.download_button(
    label="📥 Download State Crime Data as CSV",
    data=csv_data,
    file_name=f"{state}_crime_data.csv",
    mime="text/csv"
)


