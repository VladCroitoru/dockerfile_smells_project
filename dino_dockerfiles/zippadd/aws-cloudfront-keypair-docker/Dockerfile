FROM alpine:latest

ENV scriptFilePath genAndPackKeyPair.sh
###Update packages###
RUN apk update && apk upgrade && apk add --update openssl \
###Install new packages###
#AWS cli
    && apk add py-pip && pip install --upgrade pip \
    && pip install awscli && aws configure set default.region us-west-2 \
#Parallel
    && apk add parallel
###Prep script###
COPY script/genAndPackKeyPair.sh genAndPackKeyPair.sh
RUN chmod 755 $scriptFilePath \
    && mkdir /output \
    && aws configure set default.region us-west-2
COPY *regions LICENSE /
WORKDIR /output
###Generate###
ENTRYPOINT ["/genAndPackKeyPair.sh"]
