import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance_sample.csv")

print("Dataset Head:\n", df.head())
print("\n Data Info:")
print(df.info())
print("\n Null Values:\n", df.isnull().sum())
print("\n Descriptive Statistics:\n", df.describe())
print("\n Gender Distribution:\n", df['gender'].value_counts())

#  Average Scores by Lunch Type
print("\n Average Scores by Lunch Type:\n")
print(df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean())

#  Visualization
#Math Score Distribution
plt.figure(figsize=(6, 4))
sns.histplot(df['math score'], kde=True,  color='skyblue')
plt.title('Math Score Distribution')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("math_score_distribution.png")
plt.show()

#  Math Score by Parental Education
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x='parental level of education',
    y='math score',
    hue='parental level of education', 
    palette='viridis',
)
plt.xticks(rotation=45)
plt.title('Math Score by Parental Education')
plt.tight_layout()
plt.savefig("math_score_by_parent_edu.png")
plt.show()

# Plot pie chart
avg_scores = df.groupby('gender')['reading score'].mean()

plt.figure(figsize=(6, 6))
plt.pie(avg_scores, labels=avg_scores.index, autopct='%1.1f%%', colors=['#66c2a5', '#fc8d62'])
plt.title(' Reading Score Distribution by Gender')
plt.tight_layout()
plt.savefig("reading_score_piechart.png")
plt.show()

#  Save Cleaned Data
df.to_csv("cleaned_student_data.csv", index=False)
print("\n Cleaned data exported as 'cleaned_student_data.csv'")