import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# =========================
# 1. Generate Random Integers
# =========================

random_integers = np.random.randint(-3, 20, 10000)


# =========================
# 2. Compute Statistics
# =========================

mean_value = np.mean(random_integers)
median_value = np.median(random_integers)
max_value = np.max(random_integers)
min_value = np.min(random_integers)
std_value = np.std(random_integers)

threshold = mean_value - 3 * std_value
percentage_below_threshold = np.sum(random_integers < threshold) / len(random_integers) * 100

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
print(f"Standard deviation: {std_value}")
print(f"Percentage below 3 std deviations: {percentage_below_threshold:.2f}%")


# =========================
# 3. Create DataFrame with Unique Values
# =========================

df = pd.DataFrame(sorted(set(random_integers)), columns=["number"])
df["is_negative"] = df["number"] < 0

print(df)


# =========================
# 4. Remove Negative Values
# =========================

df = df[df["is_negative"] == False]


# =========================
# 5. Plot Histogram
# =========================

plt.hist(df["number"], bins=len(df["number"]), edgecolor="black")
plt.xlabel("Values")
plt.ylabel("Count")
plt.title("Histogram of Unique Non-Negative Numbers")
plt.show()


# =========================
# 6. Save to CSV
# =========================

csv_file_name = f"Data_{mean_value:.2f}_{std_value:.2f}.csv"
df.to_csv(csv_file_name, index=False)