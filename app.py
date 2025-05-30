import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
def load_data():
    df = pd.read_csv(r"C:\Users\benzz\Downloads\Streamlit\jobs_in_data.csv")
    return df

def main():
    st.title("Data Science Salary Analysis")
    df = load_data()

    # Display raw data
    if st.checkbox("Show raw data"):
        st.write(df.head())

    # Filter by year
    st.subheader("Filter by Work Year")
    years = sorted(df['work_year'].unique())
    selected_year = st.selectbox("Select Work Year", years)
    df_year = df[df['work_year'] == selected_year]

    # Show average salary by job title
    st.subheader("Average Salary by Job Title (USD)")
    avg_salary = df_year.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(10)
    st.bar_chart(avg_salary)

    # Salary distribution
    st.subheader("Salary Distribution (USD)")
    fig, ax = plt.subplots()
    sns.histplot(df_year["salary_in_usd"], kde=True, ax=ax)
    st.pyplot(fig)

    # Job category counts
    st.subheader("Job Category Distribution")
    fig2, ax2 = plt.subplots()
    df_year["job_category"].value_counts().plot(kind="bar", ax=ax2)
    st.pyplot(fig2)

if __name__ == "__main__":
    main()