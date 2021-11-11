FROM nginx:1.11.8
MAINTAINER Abdul Hagi <abdul.hagi@turner.com>

# update base image
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
                                                  curl

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 6.3.1

# Install nvm with node and npm
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# Set up our PATH correctly so we don't have to long-reference npm, node, &c.
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# Add our applicaiton source
ADD nginx.tmp.conf /opt/dynamic-nginx/
ADD nginx-conf.js /opt/dynamic-nginx/

WORKDIR /opt/dynamic-nginx

ADD ./package.json package.json

#Install NPM Packages
RUN npm install


EXPOSE 80

RUN rm /etc/nginx/conf.d/*

CMD ["bash","-c","node nginx-conf.js --listen 80 --location / --proxy_pass http://gateway:8080/ --nginx_location /etc/nginx/nginx.conf && nginx -g 'daemon off;'"]


