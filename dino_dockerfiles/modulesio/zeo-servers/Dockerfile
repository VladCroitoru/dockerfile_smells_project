FROM debian:latest

RUN apt-get update && apt-get install -y curl && apt-get clean
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash && \
  bash -c 'NVM_DIR="/root/.nvm"; . "$NVM_DIR/nvm.sh"; nvm install 8.9.3;'
ENV PATH $PATH:/root/.nvm/versions/node/v8.9.3/bin/

ADD . /root/zeo
WORKDIR /root/zeo
RUN npm install --unsafe-perm

CMD ["npm", "start"]
