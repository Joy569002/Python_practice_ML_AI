import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df_features = pd.DataFrame(X, columns=feature_names)
plt.figure(figsize=(8,6))
sns.heatmap(df_features.corr(), annot=True, cmap="coolwarm", center=0)
plt.title("Feature Correlation Heatmap")
plt.show()