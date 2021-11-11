FROM python:3.8

# Create app directory
WORKDIR /app

# Copy dependencies
COPY ./requirements.txt ./

# Install Python dependencies
RUN pip install --user --no-cache-dir -r ./requirements.txt

# Copy repository
COPY ./ ./

# Export the container's port used by the API host
EXPOSE 5000

# Run the application
CMD [ "python", "-m", "server"]
