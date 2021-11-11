FROM node:0.12.7-slim

MAINTAINER Snorre Magnus Davøen <snorremd@gmail.com>

# Get the app
RUN \
  apt-get update && \
  apt-get install git -y && \
  git clone https://github.com/outsideris/slack-invite-automation.git \
  /src && \
  cd /src && \
  npm install && \
  apt-get --purge remove git -y && \
  apt-get autoremove -y && apt-get autoclean -y

# Run app at 8888
EXPOSE 3000

# Run from project root
WORKDIR /src

# Define default command.
CMD ["npm", "start"]
