import matplotlib.pyplot as plt
import numpy as np

# y_true, y_pred from your MLR model
plt.figure(figsize=(6,6))
plt.scatter(y_true, y_pred, alpha=0.6)
mn, mx = np.min([y_true, y_pred]), np.max([y_true, y_pred])
plt.plot([mn, mx], [mn, mx], 'r--', linewidth=2)
plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title("Actual vs Predicted (Parity Plot)")
plt.grid(True)
plt.show()