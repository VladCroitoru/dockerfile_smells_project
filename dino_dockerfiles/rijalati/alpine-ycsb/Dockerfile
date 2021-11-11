FROM rijalati/alpine-zulu-jdk8:latest-mini
MAINTAINER ritchie@selectstar.io

ENV YCSB_VERSION=0.14.0 \
    PATH=${PATH}:/usr/bin

RUN apk --update --no-cache add python mksh \
    && cd /opt \
    && eval curl "-Ls https://github.com/brianfrankcooper/YCSB/releases/download/${YCSB_VERSION}/ycsb-${YCSB_VERSION}.tar.gz" \
    | tar -xzvf -

COPY start.sh /start.sh
RUN chmod +x /start.sh

ENV ACTION='' DBTYPE='' WORKLETTER='' DBARGS='' RECNUM='' OPNUM=''

WORKDIR "/opt/ycsb-${YCSB_VERSION}"

ENTRYPOINT ["/start.sh"]
