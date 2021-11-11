FROM alpine:3.6

RUN set -xe \
    && apk update \
    && apk upgrade \
    && apk add --update \
    && apk add samba \
    && apk add samba-common-tools \
    && apk add supervisor \
    && apk add python \
    && apk add python-dev \
    && apk add py-pip \
    && apk add build-base \
    && apk add vim \
    && apk add nmap \
    && pip install --upgrade pip \
    && pip install python-nmap \
    && pip install openpyxl \
    && pip install requests \
    && pip install BeautifulSoup4 \
    && pip install pymongo \
    && rm -rf /var/cache/apk/* \
    && mkdir /config /shared \
    && chmod 777 /shared


VOLUME /config /shared
COPY *.conf /config/
COPY *.py /config/
COPY nselib /usr/share/nmap/nselib
COPY scripts /usr/share/nmap/scripts
COPY nse_main.lua /usr/share/nmap


EXPOSE 137/udp 138/udp 139 445

ENTRYPOINT ["supervisord", "-c", "/config/supervisord.conf"]

#Reference pwntr/samba-alpine
