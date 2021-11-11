FROM zouchao2010/python:2.7

VOLUME /var/lib/litecoind

ADD . /opt/litecoind
WORKDIR /opt/litecoind
RUN cp -r testnet /var/lib/litecoind
RUN cp -r livenet /var/lib/litecoind

ENV TESTNET 0
ENV VERSION 0.10.4.0

RUN apt-get update \
    && apt-get install -y wget \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

#安装litecoind
RUN wget https://download.litecoin.org/litecoin-$VERSION/linux/litecoin-$VERSION-linux64.tar.gz \
    && tar zxvf litecoin-$VERSION-linux64.tar.gz \
    && ln -sfv /opt/litecoind/litecoin-$VERSION/bin/* /usr/local/bin \
    && rm -rf litecoin-$VERSION-linux64.tar.gz

RUN chmod 755 run.sh

#Livenet
EXPOSE 9332
EXPOSE 9333

#Testnet
EXPOSE 19332
EXPOSE 19333

CMD ["./run.sh"]
