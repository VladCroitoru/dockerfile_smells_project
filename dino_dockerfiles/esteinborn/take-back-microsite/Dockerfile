FROM node:9

# Run all commands from this location
WORKDIR /usr/src/app

# Copy in the App code
COPY . .

# Install dependencies
RUN yarn

# We're serving from port 5000
EXPOSE 5000

RUN chmod +x run.sh

# Run the server
CMD ["/usr/src/app/run.sh"]