FROM node:12.18.2-alpine
RUN  apt-get update && apt-get install -y gnupg2 && \
     apt-get install -y --no-install-recommends apt-utils && \
     echo node -v && \
     apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6 && \
    echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list && \
    apt-get update && \
    apt install -y git && \
    apt-get install -y mongodb-org && \
    apt-get install -y libssl-dev && \
    apt-get install -y ruby-full rubygems autogen autoconf libtool make && \
    npm install grunt -g && \
    npm install bower -g && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# This Dockerfile doesn't need to have an entrypoint and a command
# as Bitbucket Pipelines will overwrite it with a bash script.
