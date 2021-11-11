FROM lnlscon/epics-debian9-r3.15.8:2021-02-26
LABEL MAINTAINER="Guilherme Francisco de Freitas <guilherme.freitas@cnpem.br>"

RUN cd ${EPICS_MODULES};\
    wget -O asyn-failover-0.1.1.tar.gz https://github.com/cnpem-iot/asyn-failover/archive/refs/tags/v0.1.1.tar.gz;\
    tar -xzf asyn-failover-0.1.1.tar.gz;\
    ls;\
    cd asyn-failover-0.1.1;\
    make

WORKDIR /opt/redis-ioc

RUN apt-get -y update && apt-get install -y python3 curl python3-pip && \
    pip3 install pylightxl && mkdir -p sockets && mkdir -p log

COPY . . 

CMD ["/bin/bash", "-c", "set -e; cd scripts/; make run"]
