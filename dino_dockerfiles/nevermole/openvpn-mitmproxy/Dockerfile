FROM alpine:3.4

ENV LANG=en_US.UTF-8

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community/" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update openvpn iptables bash easy-rsa openvpn-auth-pam google-authenticator pamtester && \
    ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

# Needed by scripts
ENV OPENVPN /etc/openvpn
ENV EASYRSA /usr/share/easy-rsa
ENV EASYRSA_PKI $OPENVPN/pki
ENV EASYRSA_VARS_FILE $OPENVPN/vars

VOLUME ["/etc/openvpn"]

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*

# Add support for OTP authentication using a PAM module
ADD ./otp/openvpn /etc/pam.d/

COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache \
        git \
        g++ \
        libffi \
        libffi-dev \
        libjpeg-turbo \
        libjpeg-turbo-dev \
        libstdc++ \
        libxml2 \
        libxml2-dev \
        libxslt \
        libxslt-dev \
        openssl \
        openssl-dev \
        python3 \
        python3-dev \
        zlib \
        zlib-dev \
    && python3 -m ensurepip \
    && LDFLAGS=-L/lib pip3 install -r /tmp/requirements.txt \
    && apk del --purge \
        git \
        g++ \
        libffi-dev \
        libjpeg-turbo-dev \
        libxml2-dev \
        libxslt-dev \
        openssl-dev \
        python3-dev \
        zlib-dev \
    && rm /tmp/requirements.txt \
    && rm -rf ~/.cache/pip 

RUN mkdir -p /home/mitmproxy/.mitmproxy
VOLUME /home/mitmproxy/.mitmproxy

EXPOSE 8080 8081
#CMD ["mitmproxy"]


# Internally uses port 1194/udp, remap using `docker run -p 443:1194/tcp`
EXPOSE 1194/udp

CMD ["ovpn_run"]