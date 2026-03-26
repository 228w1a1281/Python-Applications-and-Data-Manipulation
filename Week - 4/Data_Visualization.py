import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
import pandas as pd

# Sample dataset
data = {
    "Age": [18, 19, 20, 21, 22, 23, 24],
    "Study_Hours": [2, 3, 4, 5, 6, 4, 3],
    "Score": [60, 65, 70, 75, 80, 78, 72]
}

df = pd.DataFrame(data)

# ---------- Histogram ----------
plt.hist(df["Score"])
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

# ---------- Scatter Plot ----------
plt.scatter(df["Study_Hours"], df["Score"])
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()

# ---------- Heatmap ----------
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# ---------- Pairplot ----------
sns.pairplot(df)
plt.show()