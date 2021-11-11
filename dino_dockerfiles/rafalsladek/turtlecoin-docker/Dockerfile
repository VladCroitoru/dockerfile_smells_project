FROM ubuntu:latest
LABEL Author="Rafal Sladek rafal.sladek@gmail.com"

ENV TZ=Europe/Berlin
ENV COIN=turtlecoin
ENV DAEMON_VERSION=v0.5.0
ENV DAEMON_ZIP=${COIN}-${DAEMON_VERSION}-linux.tar.gz
ENV DAEMON_SRC=https://github.com/turtlecoin/turtlecoin/releases/download/${DAEMON_VERSION}/${DAEMON_ZIP}

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -yq update && \
    apt-get -y upgrade && \
    apt-get autoclean autoremove -yq && \
    apt-get clean -yq

RUN apt-get -y install tree wget tzdata

RUN dpkg-reconfigure -f noninteractive tzdata

RUN cd /tmp && \
    echo $DAEMON_SRC && \
    wget -q $DAEMON_SRC && \
    cd /usr/local/bin && \
    tar -xvzf /tmp/${DAEMON_ZIP} && \
    mv ${COIN}-${DAEMON_VERSION}/* . && \ 
    rm -f /tmp/${DAEMON_ZIP} && \
    rm -rf ${COIN}-${DAEMON_VERSION} && \
    tree

WORKDIR /root
VOLUME [ "/root/.TurtleCoin" ]
EXPOSE  11897 11898

CMD [ "TurtleCoind"]
