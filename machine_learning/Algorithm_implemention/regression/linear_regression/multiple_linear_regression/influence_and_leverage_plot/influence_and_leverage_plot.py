import statsmodels.api as sm

# Fit using statsmodels for diagnostics
X_sm = sm.add_constant(X)
ols = sm.OLS(y, X_sm).fit()
influence = ols.get_influence()

# Leverage vs. Studentized Residuals
sm.graphics.influence_plot(ols, criterion="cooks")
plt.show()