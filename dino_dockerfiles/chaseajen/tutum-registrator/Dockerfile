FROM node

# Copy source
COPY src /src

# Change working directories and install dependencies
WORKDIR /src
RUN npm install

# Run node program
ENTRYPOINT node program $TUTUM_USER $TUTUM_TOKEN $CONSUL_HOST $CONSUL_PORT $REFRESH_INTERVAL