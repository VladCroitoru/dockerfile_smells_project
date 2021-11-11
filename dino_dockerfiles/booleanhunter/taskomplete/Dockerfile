# Node v8 as the base image to support ES6
FROM node:8.11.2

# Create a new user to our new container and avoid the root user
RUN useradd --user-group --create-home --shell /bin/false booleanhunter && \
    apt-get clean && apt-get update && apt-get install -y --no-install-recommends apt-utils && apt-get install sudo

ENV HOME=/home/booleanhunter

# Copies the curent directory into the container at the mentioned path
COPY ./ $HOME/apps/tasKomplete

#RUN chown -R booleanhunter:booleanhunter $HOME/* /usr/local/

WORKDIR $HOME/apps/tasKomplete

RUN npm install --production

#RUN chown -R booleanhunter:booleanhunter $HOME/*

USER booleanhunter

EXPOSE 4321

CMD DEBUG=taskomplete:*, node app.js