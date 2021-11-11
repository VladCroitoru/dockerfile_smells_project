FROM alpine:3.13

RUN apk --no-cache add bash \
                       bind \
                       bind-tools \
                       ca-certificates \
                       curl \
                       git \
                       iperf \
                       iputils \
                       jq \
                       openldap-clients \
                       mtr \
                       netcat-openbsd \
                       nmap \
                       openssh-client \
                       rsync \
                       tcpdump \
                       vim \
                       wget

ENTRYPOINT [ "/bin/bash" ]
