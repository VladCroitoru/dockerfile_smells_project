FROM zazukoians/hitch
MAINTAINER Adrian Gschwend <adrian.gschwend@zazuko.com>

RUN apk --update add git
RUN cd /tmp/ && \
    git clone https://github.com/Neilpang/acme.sh.git && \
    cd ./acme.sh && \
    ./acme.sh --install --cert-home /etc/ssl/acme --config-home /etc/acme
RUN apk del git

