import matplotlib.pyplot as plt


feature_idx = 0  # pick a feature column
plt.figure(figsize=(6,4))
plt.scatter(X[:, feature_idx], residuals, alpha=0.6)
plt.axhline(0, color='r', linestyle='--')
plt.xlabel(f"Feature {feature_idx}")
plt.ylabel("Residuals")
plt.title("Residuals vs Feature")
plt.grid(True)
plt.show()