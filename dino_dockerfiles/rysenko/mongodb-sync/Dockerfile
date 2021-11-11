FROM ubuntu:trusty
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv BC711F9BA15703C6 && \
    echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list && \
    apt-get update && \
    apt-get install -y mongodb-org-shell mongodb-org-tools python-pip && \
    echo "mongodb-org-shell hold" | dpkg --set-selections && \
    echo "mongodb-org-tools hold" | dpkg --set-selections && \
    pip install awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    mkdir /backup

ENV CRON_TIME="0 0 * * *"
ENV S3_PATH=mongodb
ENV AWS_DEFAULT_REGION=us-east-1

ADD docker_entrypoint.sh /docker_entrypoint.sh
ADD backup.sh /backup.sh
ADD restore.sh /restore.sh
ADD sync.sh /sync.sh

VOLUME ["/backup"]

ENTRYPOINT ["/docker_entrypoint.sh"]

CMD ["sync"]
