FROM alpine
MAINTAINER Mike Bertram <contact@mibexx.de>


RUN apk update \
 && apk add --no-cache \
    bash \
    curl \
    groff \
    less \
    python3 \
    sshpass \
    openssh-client \
    rsync \
 && python3 -m ensurepip \
 && pip3 install awscli

COPY entrypoint.sh /
COPY bin/ /usr/local/bin/

RUN chmod +x /entrypoint.sh \
 && chmod -Rf +x /usr/local/bin

ENTRYPOINT ["/entrypoint.sh"]
CMD ["help"]