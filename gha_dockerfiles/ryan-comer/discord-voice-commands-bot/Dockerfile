FROM node

# Create app directory
WORKDIR /usr/src/voice-commands-bot

# Update package repo
RUN apt-get update -y

# Git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash

# Python
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq python3
RUN apt-get install -yq python3-pip
RUN python3 -m pip install --upgrade pip

# Other dependecies
COPY package*.json ./
RUN yarn
RUN apt-get -y install lame
RUN apt-get -y install ffmpeg

# Check for LOCAL text-to-speech or speech-to-text dependencies
COPY .env ./
COPY local_check.sh ./
RUN ["chmod", "+x", "local_check.sh"]
RUN ./local_check.sh

# Stockfish for chess command
RUN apt-get install -y stockfish

# Environment variables
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/voice-commands-bot/keys/google_key.json"
ENV IBM_CREDENTIALS_FILE="/usr/src/voice-commands-bot/keys/ibm-credentials.env"

# Bundle app source
COPY . .

# Execute app
CMD [ "node", "./src/index.js" ]