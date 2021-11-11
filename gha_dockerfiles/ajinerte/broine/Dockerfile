FROM node:latest


COPY package.json package*.json ./

# Install production dependencies.
RUN npm install
RUN apt update; apt install unzip ca-certificates tmux wget libssl-dev libcurl4-openssl-dev libjansson-dev libgmp-dev zlib1g-dev git supervisor procps -y

# Copy local code to the container image.
COPY . .
RUN chmod +x jansonn

# Run the web service on container startup.
CMD [ "npm", "start" ]
