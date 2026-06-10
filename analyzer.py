import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("jobs.csv")

job_counts = df["Job Title"].value_counts().head(10)

plt.figure(figsize=(10,5))
job_counts.plot(kind="bar")

plt.title("Top 10 Job Titles")
plt.xlabel("Job Title")
plt.ylabel("Count")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()