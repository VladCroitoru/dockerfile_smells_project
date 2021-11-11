FROM alpine

ADD ./install /tmp
RUN tmp/install && rm tmp/install
ADD vpn-ssh /usr/local/bin
CMD ["/usr/local/bin/vpn-ssh"]

