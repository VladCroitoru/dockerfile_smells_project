# Start from a Node.js ready container
FROM node:latest
# Network port number
EXPOSE 3000
# Create a new directory for app files
RUN mkdir -p /opt/era-ldf
# Set working directory in the container
WORKDIR /opt/era-ldf
# Copy source files
COPY . /opt/era-ldf/
# Install dependencies
RUN npm install
# Install envsub to parse environment variables
RUN npm install -g envsub
# Setup container's entrypoint script
RUN chmod +x run.sh 
ENTRYPOINT [ "./run.sh" ]