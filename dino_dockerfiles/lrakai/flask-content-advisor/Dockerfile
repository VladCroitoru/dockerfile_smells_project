# Python v3 base layer
FROM python:3

# Set the working directory in the image's file system
WORKDIR /usr/src/app

# Copy everything in the host working directory to the container's
COPY . .

# Install code dependencies in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Indicate that the server will be listening on port 5000
EXPOSE 5000

# Set the default command to run the app
CMD [ "python", "./src/app.py" ]