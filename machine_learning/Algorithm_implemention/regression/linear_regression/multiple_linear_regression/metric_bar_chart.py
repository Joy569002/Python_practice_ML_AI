from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
metrics = {
    "R2": r2_score(y_true, y_pred),
    "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),
    "MAE": mean_absolute_error(y_true, y_pred),
    "MAPE": np.mean(np.abs((y_true - y_pred) / y_true)) * 100
}

plt.figure(figsize=(6,4))
plt.bar(metrics.keys(), metrics.values(), color=['skyblue','orange','green','red'])
plt.ylabel("Value")
plt.title("Regression Performance Metrics")
plt.grid(axis='y')
plt.show()