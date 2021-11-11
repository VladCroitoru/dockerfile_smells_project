FROM fedora:latest as builder
MAINTAINER Xueshan Feng <xueshan.feng@gmail.com>
RUN echo "Installing socat...." && dnf install socat -y
RUN libssl=$(ldd /usr/bin/socat | grep libssl.so | awk '{print $1}') && \
    libcrypto=$(ldd /usr/bin/socat | grep libcrypto | awk '{print $1}') && \
    libreadline=$(ldd /usr/bin/socat | grep libreadline | awk '{print $1}') && \
    libtinfo=$(ldd /usr/bin/socat | grep libtinfo | awk '{print $1}') && \
    mkdir -p /socat.d/lib /socat.d/bin  && \
    cp -vf /usr/bin/socat /socat.d/bin/socat && chmod 755 /socat.d/bin/socat && \
    cp -vf /usr/lib64/$libssl /usr/lib64/$libcrypto /usr/lib64/$libreadline /usr/lib64/$libtinfo /socat.d/lib/

FROM alpine:latest
RUN mkdir /socat.d
COPY --from=builder /socat.d /socat.d/
ADD start.sh /start.sh
RUN chmod 755 /start.sh
ADD socat.sh /socat.sh
RUN chmod 755 /socat.sh
VOLUME ["/opt/bin"]
CMD [ "/start.sh" ]
