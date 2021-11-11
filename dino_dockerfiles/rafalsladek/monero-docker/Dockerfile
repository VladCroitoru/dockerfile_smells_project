FROM ubuntu:latest
LABEL Author="Rafal Sladek rafal.sladek@gmail.com"

ENV TZ=Europe/Berlin
ENV RPCUSER=PleaseChangeUser
ENV RPCPASS=PleaseChangePass
ENV RPCHOST=localhost
ENV RPCPORT=18081
ENV WALLETFILE=PleaseChangeWalletFile
ENV WALLETPASSWORDFILE=PleaseChangeWalletPassFile

ENV DAEMON_VERSION=0.15.0.1
ENV DAEMON_ZIP=monero-linux-x64-v${DAEMON_VERSION}.tar.bz2
ENV DAEMON_SRC=https://dlsrc.getmonero.org/cli/${DAEMON_ZIP}
ENV DAEMON_FILE_SHA265=8d61f992a7e2dbc3d753470b4928b5bb9134ea14cf6f2973ba11d1600c0ce9ad

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -yq update && \
    apt-get -y upgrade && \
    apt-get -y install tree wget bzip2 tzdata gzip curl && \
    apt-get autoclean autoremove -yq && \
    apt-get clean -yq

RUN dpkg-reconfigure -f noninteractive tzdata

COPY run_monerod.sh /usr/local/bin/
COPY run_wallet.sh /usr/local/bin/
COPY start.sh /usr/local/bin/
COPY bitmonero.conf /root/.bitmonero/bitmonero.conf

RUN cd /tmp && \
    wget -q $DAEMON_SRC && \
    echo "$DAEMON_FILE_SHA265  /tmp/${DAEMON_ZIP}" | sha256sum -c -  && \
    tar -xvf $DAEMON_ZIP && \
    rm $DAEMON_ZIP && \
    cd monero-x86_64-linux-gnu-v$DAEMON_VERSION/ && \
    mv * /usr/local/bin/ && \
    ls -al /usr/local/bin/

WORKDIR /root

VOLUME [ "/root/.bitmonero", "/root/wallet" ]

EXPOSE  18080 18081

CMD [ "sh", "/usr/local/bin/start.sh" ]