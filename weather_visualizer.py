'''
Name: Kirti Saini
Date: 04/12/2025
Title: Weather Data Visualizer
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# Task 1: Load Dataset
# ---------------------------------------------------------------

df = pd.read_csv("weather.csv")

print("\n----- HEAD -----")
print(df.head())

print("\n----- INFO -----")
print(df.info())

print("\n----- DESCRIBE -----")
print(df.describe())

# ---------------------------------------------------------------
# Task 2: Data Cleaning
# ---------------------------------------------------------------

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['date'])

# Fill missing numeric values
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Select relevant columns for Delhi dataset
columns_needed = ['date', 'meantemp', 'humidity']
df = df[columns_needed]

# Rename meantemp → temperature for easier handling
df = df.rename(columns={'meantemp': 'temperature'})

print("\nCleaned Data:")
print(df.head())

# Add month & year for grouping
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# ---------------------------------------------------------------
# Task 3: Statistical Analysis
# ---------------------------------------------------------------

daily_mean = df['temperature'].mean()
daily_min = df['temperature'].min()
daily_max = df['temperature'].max()
daily_std = df['temperature'].std()

print("\nDaily Temperature Statistics:")
print(f"Mean Temp: {daily_mean:.2f}")
print(f"Min Temp: {daily_min:.2f}")
print(f"Max Temp: {daily_max:.2f}")
print(f"Std Dev: {daily_std:.2f}")

# ---------------------------------------------------------------
# Task 4: Visualizations
# ---------------------------------------------------------------

# 1. Line chart — Daily Temperature Trend
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Trend")
plt.grid()
plt.savefig("daily_temperature_trend.png")
plt.close()

# 2. Scatter Plot — Humidity vs Temperature
plt.figure(figsize=(8,5))
plt.scatter(df['humidity'], df['temperature'])
plt.xlabel("Humidity (%)")
plt.ylabel("Temperature (°C)")
plt.title("Humidity vs Temperature")
plt.grid()
plt.savefig("humidity_vs_temperature.png")
plt.close()

# 3. Combined Plots
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Trend")

plt.subplot(1,2,2)
plt.scatter(df['humidity'], df['temperature'])
plt.title("Humidity vs Temperature")

plt.tight_layout()
plt.savefig("combined_plots.png")
plt.close()

# ---------------------------------------------------------------
# Task 5: Grouping and Aggregation
# ---------------------------------------------------------------

monthly_stats = df.groupby('month').agg({
    'temperature': ['mean', 'min', 'max'],
    'humidity': 'mean'
})

print("\nMonthly Aggregated Statistics:")
print(monthly_stats)

# ---------------------------------------------------------------
# Task 6: Export Results
# ---------------------------------------------------------------

# Save cleaned data
df.to_csv("cleaned_weather_data.csv", index=False)

# Save text summary report
with open("summary_report.txt", "w") as f:
    f.write("WEATHER DATA ANALYSIS SUMMARY\n")
    f.write("-------------------------------------\n")
    f.write(f"Average Temperature: {daily_mean:.2f}\n")
    f.write(f"Min Temperature: {daily_min:.2f}\n")
    f.write(f"Max Temperature: {daily_max:.2f}\n")
    f.write(f"Temperature Std Dev: {daily_std:.2f}\n\n")
    f.write("Monthly Stats:\n")
    f.write(str(monthly_stats))

print("\nAll tasks completed successfully!")
print("Generated files:")
print("- cleaned_weather_data.csv")
print("- daily_temperature_trend.png")
print("- humidity_vs_temperature.png")
print("- combined_plots.png")
print("- summary_report.txt")
