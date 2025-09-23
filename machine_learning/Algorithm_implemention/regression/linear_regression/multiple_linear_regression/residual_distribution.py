import seaborn as sns
import statsmodels.api as sm

# Histogram + KDE
plt.figure(figsize=(6,4))
sns.histplot(residuals, kde=True)
plt.title("Residual Distribution")
plt.show()

# QQ-Plot
sm.qqplot(residuals, line='45', fit=True)
plt.title("QQ-Plot of Residuals")
plt.show()