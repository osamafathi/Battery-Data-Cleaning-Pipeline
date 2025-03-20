# Battery Data Cleaning Pipeline

## Overview
This project processes battery time series data by cleaning, transforming, and aggregating it using **Python (pandas)**. The application is then containerized using **Docker** for easy deployment.

## Features
- Loads raw CSV data
- Cleans and transforms data:
  - Converts incorrect data types
  - Fills missing values
  - Removes duplicates
  - Extracts date and hour from timestamps
  - Aggregates `grid_purchase` and `grid_feedin` per hour
  - Identifies the hour with the highest `grid_feedin` per day
- Saves the cleaned data to `cleaned_battery_data.csv`

## Prerequisites
Ensure you have the following installed:
- **Python 3.9+**
- **Docker Desktop** (for Windows/Mac) or Docker Engine (for Linux)

## Running the Python Script (Without Docker)
To run the script manually:

```sh
# Install dependencies
pip install pandas

# Run the script
python battery_cleaning.py
```

## Docker Setup

### 1️⃣ Build the Docker Image
```sh
docker build -t battery-data-cleaner .
```

### 2️⃣ Run the Docker Container
```sh
docker run --rm -v "$(pwd):/app" battery-data-cleaner
```
- `--rm` removes the container after execution
- `-v "$(pwd):/app"` ensures the output file is saved to your local directory

This will generate `cleaned_battery_data.csv` in your current directory.

## Repository Structure
```
📂 project-folder/
├── 📄 Dockerfile
├── 📄 battery_cleaning.py
├── 📄 measurements_coding_challenge.csv (Sample dataset)
├── 📄 cleaned_battery_data.csv (Generated output)
└── 📄 README.md
```

## Notes
- The script assumes `measurements_coding_challenge.csv` is in the same directory.
- The output file `cleaned_battery_data.csv` contains the transformed data.
- If running on **Windows**, use `"%cd%":/app` instead of `$(pwd):/app` in the Docker command.
