from pybaseball import statcast_pitcher
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Gerrit Cole, June 1–10, 2023
data = statcast_pitcher("2023-06-01", "2023-06-10", 543037)

# Filter pitches
data = data.dropna(subset=['plate_x', 'plate_z', 'pitch_type'])
data = data[data['description'].isin(['called_strike', 'ball', 'swinging_strike', 'foul'])]

# Plot
plt.figure(figsize=(7, 9))
sns.scatterplot(data=data, x='plate_x', y='plate_z', hue='pitch_type', alpha=0.7, legend='full')

# Strike zone
plt.axhline(3.5, color='gray', linestyle='--')
plt.axhline(1.5, color='gray', linestyle='--')
plt.axvline(-0.95, color='gray', linestyle='--')
plt.axvline(0.95, color='gray', linestyle='--')

plt.title("Pitch Locations by Type")
plt.xlabel("Horizontal (plate_x)")
plt.ylabel("Vertical (plate_z)")
plt.legend()
plt.grid(True)
plt.show()
