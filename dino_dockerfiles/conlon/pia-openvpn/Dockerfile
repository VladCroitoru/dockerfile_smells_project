FROM alpine:latest
MAINTAINER conlon

RUN apk -U upgrade && \
    apk add --no-cache openvpn curl bash && \
    #
    #AES256 encryption profiles
    curl -o /openvpn-strong.zip https://www.privateinternetaccess.com/openvpn/openvpn-strong.zip && \
    mkdir /etc/openvpn/pia-strong && \
    unzip -d /etc/openvpn/pia-strong/ /openvpn-strong.zip && \
    #AES128 encryption profiles
    curl -o /openvpn.zip https://www.privateinternetaccess.com/openvpn/openvpn.zip && \
    mkdir /etc/openvpn/pia-standard && \
    unzip -d /etc/openvpn/pia-standard/ /openvpn.zip && \
    #
    # cleanup temporary files
    # rm -rf /tmp && \
    rm /openvpn.zip && \
    rm /openvpn-strong.zip && \
    rm -rf /var/cache/apk/*


COPY openvpn.sh /usr/local/bin/openvpn.sh
WORKDIR /etc/openvpn

ENV REGION="us_texas"
ENTRYPOINT ["openvpn.sh"]
#ENTRYPOINT ["/bin/bash"]
