# Check out https://hub.docker.com/_/node to select a new base image
FROM node:10-slim

# Installing Oracle instant client
WORKDIR    /opt/oracle
RUN        apt-get update && apt-get install -y libaio1 wget unzip \
            && wget https://download.oracle.com/otn_software/linux/instantclient/19800/instantclient-basiclite-linux.x64-19.8.0.0.0dbru.zip \
            && wget https://download.oracle.com/otn_software/linux/instantclient/19800/instantclient-sqlplus-linux.x64-19.8.0.0.0dbru.zip \
            && wget https://download.oracle.com/otn_software/linux/instantclient/19800/instantclient-sdk-linux.x64-19.8.0.0.0dbru.zip \
            && unzip instantclient-basiclite-linux.x64-19.8.0.0.0dbru.zip \
            && unzip instantclient-sqlplus-linux.x64-19.8.0.0.0dbru.zip \
            && unzip instantclient-sdk-linux.x64-19.8.0.0.0dbru.zip \
            && rm -f instantclient-basiclite-linux.x64-19.8.0.0.0dbru.zip \
            && rm -f instantclient-sqlplus-linux.x64-19.8.0.0.0dbru.zip \
            && rm -f instantclient-sdk-linux.x64-19.8.0.0.0dbru.zip \
            && cd /opt/oracle/instantclient* \
            && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
            && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
            && ldconfig

# Set to a non-root built-in user `node`
USER node

# Create app directory (with user `node`)
RUN mkdir -p /home/node/app

WORKDIR /home/node/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY --chown=node package*.json ./

RUN npm install

# Bundle app source code
COPY --chown=node . .

# Bind to all network interfaces so that it can be mapped to the host OS
ENV HOST=0.0.0.0

EXPOSE ${PORT}
CMD npm start
