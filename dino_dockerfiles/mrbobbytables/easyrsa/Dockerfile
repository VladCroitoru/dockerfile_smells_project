FROM alpine

RUN apk update  \
 && apk add     \
   bash         \
   openssl      \
   wget         \
 && mkdir -p /usr/share/easy-rsa  \
 && wget --no-check-certificate -P /tmp https://github.com/OpenVPN/easy-rsa/releases/download/2.2.2/EasyRSA-2.2.2.tgz  \
 && tar -xvzf /tmp/EasyRSA-2.2.2.tgz -C /tmp     \
 && mv /tmp/EasyRSA-2.2.2/* /usr/share/easy-rsa  \
 && rm -rf /tmp/*

COPY ./skel /

RUN chmod +x ./init.sh

CMD ["./init.sh"]
