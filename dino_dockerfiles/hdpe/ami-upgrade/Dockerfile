FROM alpine

RUN apk update \
     && apk --no-cache add bash openssh jq py-pip \
     && pip install awscli
     
COPY ami-upgrade.sh /
     
CMD ["/ami-upgrade.sh"]
