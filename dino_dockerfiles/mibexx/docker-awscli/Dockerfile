FROM alpine
MAINTAINER Mike Bertram <contact@mibexx.de>


RUN apk update \
 && apk add --no-cache \
    bash \
    curl \
    groff \
    less \
    python3 \
 && python3 -m ensurepip \
 && pip3 install awscli

COPY aws.sh /
RUN chmod +x /aws.sh

ENTRYPOINT ["/aws.sh"]
CMD ["version"]