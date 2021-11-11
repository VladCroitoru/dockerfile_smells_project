FROM ethereum/client-go:latest

RUN sed -ie 's/archive\.ubuntu\.com/mirrors.ustc.edu.cn/' /etc/apt/sources.list
RUN apt-get update && \
        apt-get install curl git -y && \
        locale-gen zh_CN.UTF-8

ENV LC_ALL zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install nodejs -y
RUN npm install -g pm2

WORKDIR /root

RUN git clone https://github.com/cubedro/eth-net-intelligence-api ethstats-client && \
        cd ethstats-client && \
        mkdir logs && \
        npm install

RUN mkdir .ethereum && \
        mkdir /var/lib/chaindata && \
        ln -s /var/lib/chaindata /root/.ethereum/chaindata

VOLUME /root/ethstats-client/logs
VOLUME /var/lib/chaindata

COPY static-nodes.json /root/.ethereum/
COPY setup.sh processes.json /root/

ENTRYPOINT bash setup.sh && pm2 start processes.json && exec /usr/bin/geth --rpc --fast --maxpeers 100
