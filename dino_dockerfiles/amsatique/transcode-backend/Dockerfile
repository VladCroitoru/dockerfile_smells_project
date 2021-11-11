FROM ubuntu:latest
MAINTAINER Francois Dazan

# Installing dependencies
RUN apt-get update && \
    apt-get -y install curl wget git g++ make python-dev build-essential

# Installing nodejs
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - && \
    apt-get -y install nodejs

# Copy app et clean parameters to container
COPY app /app
COPY parameters.json /app/config/parameters.json

# Set script
COPY entrypoint.sh /entrypoint.sh
COPY pushbullet.sh /pushbullet.sh
RUN chmod +x /*.sh

# Start requirement installation
WORKDIR /app
RUN npm install

# Expose port
EXPOSE 3000
EXPOSE 80

# Executing entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Executing node
CMD ["npm", "start"]
