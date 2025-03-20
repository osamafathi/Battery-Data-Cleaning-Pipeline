# Use an official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script and dataset into the container
COPY battery_cleaning.py /app/
COPY measurements_coding_challenge.csv /app/

# Install required Python libraries
RUN pip install pandas

# Set the default command to run the script
CMD ["python", "battery_cleaning.py"]
