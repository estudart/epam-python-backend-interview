# Use an official Python runtime as a parent image
FROM python:3.9
# Set the working directory in the container
WORKDIR /app
# Copy requirements.txt to the container
COPY ./requirements.txt /app
# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the current directory contents into the container at /app
COPY src/ /app
# Copy the environment variables file into the container at /app
COPY .env /app
# Run command on terminal
CMD ["python", "-m", "app"]
