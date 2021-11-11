FROM node:0.12

ENV TESTNET 0
ENV VERSION latest

WORKDIR /opt/insight

RUN apt-get update \
    && apt-get install -y wget \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

#install bitcore-node
RUN npm install -g bitcore-node

ADD . /opt/insight

#create livenet insight
RUN bitcore-node create livenet \
    && cd livenet \
    && bitcore-node install insight-api \
    && bitcore-node install insight-ui \
    && mv node_modules ..

#create testnet insight
RUN bitcore-node create -t testnet \
    && cd testnet \
    && bitcore-node install insight-api \
    && bitcore-node install insight-ui \
    && rm -rf node_modules

VOLUME /var/lib/insight

RUN chmod 755 run.sh

EXPOSE 3001
CMD ["./run.sh"]
