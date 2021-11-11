# https://docs.docker.com/get-started/part2/#define-a-container-with-a-dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-alpine
RUN pip install --no-cache-dir pipenv

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pipenv install --system --deploy

# Run app.py when the container launches
CMD ["./server.py", "--mpd-hostname=mpd.chaosdorf.space", "--mqtt-hostname=mqttserver.chaosdorf.space"]
