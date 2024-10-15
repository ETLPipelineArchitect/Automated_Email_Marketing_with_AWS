import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Visualization Data
summary_df = pd.read_csv('s3://your-bucket/email-campaigns/reports/summary_report.csv')

# Visualization Example
plt.figure(figsize=(12, 6))
sns.barplot(data=summary_df, x='metric', y='value', palette='viridis')
plt.title('Email Campaign Summary Metrics')
plt.xlabel('Metric')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.show()
