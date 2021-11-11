FROM debian:latest

ARG DLURL=https://nightly.mtasa.com/?multitheftauto_linux_x64-1.5-rc-latest
ARG ARCH=x64

ENV ARCH $ARCH

COPY ./install.sh /install.sh

RUN /bin/sh ./install.sh && \
    rm install.sh && \
    groupadd -g 2000 container && \ 
    useradd -d /home/container -m container -u 2000 -g 2000 && \
    mkdir /mtasa && \
    chown 2000:2000 /mtasa

USER 2000:2000

RUN wget -q -O /home/container/mtaserver.tar.gz $DLURL && \
    tar -xf /home/container/mtaserver.tar.gz -C /mtasa --strip-components=1 && \
    rm -f /home/container/mtaserver.tar.gz && \
    mkdir /mtasa/config && \
    wget -q -O /home/container/baseconfig.tar.gz https://linux.mtasa.com/dl/baseconfig.tar.gz && \
    tar -xf /home/container/baseconfig.tar.gz -C /mtasa/config --strip-components=1 && \
    rm /home/container/baseconfig.tar.gz

EXPOSE 22003 22005 22126

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
