# cost_history from your training loop
plt.figure(figsize=(6,4))
plt.plot(cost_history, linewidth=2)
plt.xlabel("Iteration")
plt.ylabel("Cost (MSE)")
plt.title("Gradient Descent Convergence")
plt.grid(True)
plt.show()