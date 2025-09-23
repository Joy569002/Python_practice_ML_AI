from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
vif_data = [
    variance_inflation_factor(X, i) for i in range(X.shape[1])
]
plt.figure(figsize=(6,4))
plt.bar(feature_names, vif_data, color='lightgreen')
plt.xticks(rotation=45)
plt.ylabel("VIF")
plt.title("Variance Inflation Factor")
plt.grid(axis='y')
plt.show()