FROM node:8-slim

RUN echo $'\n94.31.29.131 warehouse.meteor.com\n' >> /etc/hosts

# From: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199#23
RUN mkdir -p /usr/share/man/man1 && apt-get update && \
    apt-get install --no-install-recommends -y curl python build-essential g++ git openjdk-7-jdk-headless unzip && apt-get clean
RUN npm install npm@latest -g
RUN npm install --unsafe -g chimp@0.35.0 phantomjs-prebuilt eslint mocha chai

USER node
VOLUME /app
WORKDIR /app
RUN curl -sL https://install.meteor.com | /bin/sh

ENV PATH /home/node/.meteor:$PATH
EXPOSE 3000
CMD [ "meteor", "run"]
