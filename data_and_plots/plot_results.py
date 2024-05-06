import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

original_data = pd.read_csv('./data_and_plots/normalized_CIFAR_original_stan.csv')
observed_data = pd.read_csv('./data_and_plots/normalized_CIFAR_observed_stan.csv')

# both datasets have only one feature
feature_name = original_data.columns[0]

fig, ax = plt.subplots()
ax.scatter(original_data.iloc[:, 0], observed_data.iloc[:, 0], alpha=0.5, s=5)
ax.set_xlabel(f'Normalized MNIST Run Times')
ax.set_ylabel(f'Normalized CIFAR Run Times')
ax.set_title(f'Normalized MNIST vs Normalized CIFAR (Stanley)')

# Add a diagonal line for reference
min_val = min(original_data.iloc[:, 0].min(), observed_data.iloc[:, 0].min())
max_val = max(original_data.iloc[:, 0].max(), observed_data.iloc[:, 0].max())
# ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=1)

model = LinearRegression().fit(original_data.iloc[:, 0].values.reshape(-1, 1), observed_data.iloc[:, 0].values.reshape(-1, 1))
x_range = np.linspace(min_val, max_val, 100)
y_range = model.predict(x_range.reshape(-1, 1))
ax.plot(x_range, y_range, 'g-', label=f'Linear Regression (R²={r2_score(observed_data.iloc[:, 0], model.predict(original_data.iloc[:, 0].values.reshape(-1, 1))).round(3)})')
ax.legend()

plt.savefig('./data_and_plots/observed_stan_cifar_plot.png', dpi=300, bbox_inches='tight')