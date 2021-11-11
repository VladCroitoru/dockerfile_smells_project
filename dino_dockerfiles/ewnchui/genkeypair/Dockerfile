FROM node

ENV VER=${VER:-master} \
    REPO=https://github.com/ewnchui/genKeyPair \
    APP=/usr/src/app

RUN apt-get update \  
&&  apt-get -y install git openssl \
&&  apt-get clean \
&&  git clone -b $VER $REPO $APP

WORKDIR /usr/src/app

# set emailAddress and StateOrProvinceName of openssl config
# as required to match and optional respectively
RUN sed 's/^emailAddress.*=.*optional$/emailAddress = match/g' < /etc/ssl/openssl.cnf | sed 's/^stateOrProvinceName.*=.*match$/stateOrProvinceName = optional/g' >/tmp/$$ \
&&  mv /tmp/$$ /etc/ssl/openssl.cnf \
&&  npm install \
&&  node_modules/.bin/bower install --allow-root
	
EXPOSE 1337

ENTRYPOINT ./entrypoint.sh
