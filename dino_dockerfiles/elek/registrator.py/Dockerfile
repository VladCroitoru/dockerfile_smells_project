FROM alpine
RUN apk add --update bash ca-certificates openssl curl python py2-pip && rm -rf /var/cache/apk/* && update-ca-certificates
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init
ADD requirements.txt /root/
ADD registrator.py /root/
RUN pip install -r /root/requirements.txt
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "/root/registrator.py"]
