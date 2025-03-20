#!/usr/bin/env python
# coding: utf-8




import pandas as pd

# Load the CSV file with the correct delimiter (;)
file_path = "measurements_coding_challenge.csv"
df = pd.read_csv(file_path, sep=";")

# Showing basic information about the dataset
print(df.info())
print(df.head())



# Convert timestamp to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["date"] = pd.to_datetime(df["date"],errors="coerce")

# Convert grid_purchase and grid_feedin to numeric, replacing invalid values
df["grid_purchase"] = pd.to_numeric(df["grid_purchase"], errors="coerce")
df["grid_feedin"] = pd.to_numeric(df["grid_feedin"], errors="coerce")



print(df.info())
print(df.head())


# Drop the direct_consumption column as it has mostly missing values
df.drop(columns=["direct_consumption"], inplace=True)

# Fill missing grid_purchase values with 0 (assuming missing means no purchase)
df["grid_purchase"].fillna(0, inplace=True)




print(df.info())




df["hour"] = df["timestamp"].dt.hour
df["date"] = df["timestamp"].dt.date  # Extract date for grouping



hourly_aggregation = df.groupby(["date", "hour"], as_index=False).agg(
    total_grid_purchase=("grid_purchase", "sum"),
    total_grid_feedin=("grid_feedin", "sum")
)



print(hourly_aggregation)



hourly_aggregation["max_feedin_hour"] = hourly_aggregation.groupby("date")["total_grid_feedin"].transform(
    lambda x: x == x.max()
)



output_file_path = "cleaned_battery_data.csv"
hourly_aggregation.to_csv(output_file_path, index=False)

print(hourly_aggregation.head())





