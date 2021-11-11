FROM alpine:3.4

RUN mkdir /scripts \
 && apk update \
 && apk add python \
 && apk add py-pip \
 && apk add curl \
 && apk add bash \
 && pip install awscli

ADD ec2-metadata /usr/local/bin/ec2-metadata
RUN chmod +x /usr/local/bin/ec2-metadata

ENTRYPOINT ["ec2-metadata"]

