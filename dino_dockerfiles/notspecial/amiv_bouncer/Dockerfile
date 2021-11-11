FROM node:alpine

# Port 8080 can be used as non root
EXPOSE 8080

# URL can be set via env var for build
ENV API_URL='api.amiv.ethz.ch'

# Create user with home directory and no password
RUN adduser -Dh /bouncer bouncer
USER bouncer
WORKDIR /bouncer

# Copy files and install dependencies
COPY ./ /bouncer/
RUN npm install

# Build on demand (to consider container env vars) and run http server
CMD ["npm", "run", "server"]
