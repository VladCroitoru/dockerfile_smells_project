# Original credit: https://github.com/jpetazzo/dockvpn

# Smallest base image
FROM node:10.23.1-alpine3.9

#Install ubuntu build-essentials equivalent
RUN apk add --no-cache --update-cache build-base linux-headers libressl-dev lzo-dev iproute2 linux-pam-dev

#Testing: pamtester
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update iptables bash easy-rsa openvpn-auth-pam google-authenticator pamtester libqrencode && \
    ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*


#Build openvpn from source & install xor patch
RUN wget http://swupdate.openvpn.org/community/releases/openvpn-2.5.0.tar.gz && tar xvf openvpn-2.5.0.tar.gz && \
    wget https://github.com/Tunnelblick/Tunnelblick/archive/v3.8.5beta02.zip && unzip v3.8.5beta02.zip && \
    cp Tunnelblick-3.8.5beta02/third_party/sources/openvpn/openvpn-2.5.0/patches/*.diff openvpn-2.5.0 && \
    cd openvpn-2.5.0 && \
    patch -p1 < 02-tunnelblick-openvpn_xorpatch-a.diff && \
    patch -p1 < 03-tunnelblick-openvpn_xorpatch-b.diff && \
    patch -p1 < 04-tunnelblick-openvpn_xorpatch-c.diff && \
    patch -p1 < 05-tunnelblick-openvpn_xorpatch-d.diff && \
    patch -p1 < 06-tunnelblick-openvpn_xorpatch-e.diff && \
    ./configure --disable-systemd --disable-systemd --enable-async-push --enable-iproute2 && \
    make && make install && \
    cd .. && rm -r openvpn-2.5.0 && rm -r Tunnelblick-3.8.5beta02


# Needed by scripts
ENV OPENVPN=/etc/openvpn
ENV EASYRSA=/usr/share/easy-rsa \
    EASYRSA_CRL_DAYS=3650 \
    EASYRSA_PKI=$OPENVPN/pki

VOLUME ["/etc/openvpn"]

# Internally uses port 1194/udp, remap using `docker run -p 443:1194/tcp`
EXPOSE 1194/udp

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*

# Ngrok tunneling
COPY start.sh /
COPY server/* /server/
RUN yarn --cwd /server
RUN npm install typescript ts-node -g

# Add support for OTP authentication using a PAM module
ADD ./otp/openvpn /etc/pam.d/

# Add ngrok health check

HEALTHCHECK --timeout=3s \
    CMD pgrep ngrok || exit 1

#START
RUN awk '{ sub("\r$", ""); print }' /start.sh > /start_unix.sh
RUN chmod +x /start_unix.sh 
CMD ["./start_unix.sh"]
