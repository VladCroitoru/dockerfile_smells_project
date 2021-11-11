FROM debian:jessie

RUN true && \
    echo 'APT::Default-Release "stable";' > /etc/apt/apt.conf.d/00default && \
    awk '$1 ~ "^deb" { $3 = "testing"; print; exit }' /etc/apt/sources.list > /etc/apt/sources.list.d/testing.list && \
    apt-get update && \
    apt-get -y --no-install-recommends install vim-tiny netcat-openbsd logrotate nginx uwsgi uwsgi-plugin-python3 python3 python3-pip python3-flask python3-crypto python3-rsa python3-pyasn1 python3-pil && \
    apt-get -y --no-install-recommends -t testing install python3-mysql.connector python3-redis && \
    rm -rf /var/lib/apt/lists/* && \
    true

RUN pip3 install qrcode flask-cors

CMD ["/bin/bash"]
