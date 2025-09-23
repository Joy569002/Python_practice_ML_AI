from sklearn.inspection import partial_dependence, PartialDependenceDisplay
import matplotlib.pyplot as plt
# model is your fitted regression estimator
features = [0]  # index of the feature to inspect
disp = PartialDependenceDisplay.from_estimator(
    model, X, features, kind="average", grid_resolution=50
)
plt.show()