FROM ubuntu:xenial

ENV OVFTOOL_FILENAME=VMware-ovftool-4.2.0-4586971-lin.x86_64.bundle

ADD $OVFTOOL_FILENAME /tmp/

WORKDIR /root

RUN /bin/sh /tmp/$OVFTOOL_FILENAME --console --required --eulas-agreed \
    && rm -f /tmp/$OVFTOOL_FILENAME \
    && ovftool -v


ENTRYPOINT ["ovftool"]