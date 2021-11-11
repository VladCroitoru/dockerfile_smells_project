FROM ubuntu:14.04

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A && \
    echo "deb http://repo.percona.com/apt "$(lsb_release -sc)" main" | tee /etc/apt/sources.list.d/percona.list && \
    apt-get update && \
    apt-get install -y --force-yes pmm-client curl
ADD run.sh /run.sh
CMD /run.sh
