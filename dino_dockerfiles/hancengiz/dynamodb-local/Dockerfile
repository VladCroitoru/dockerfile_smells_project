FROM openjdk:8-jre
MAINTAINER Cengiz Han <cengiz@cengizhan.com>

#dynamodb local
WORKDIR /var/dynamodb_local
RUN wget -O /tmp/dynamodb_local https://s3.eu-central-1.amazonaws.com/dynamodb-local-frankfurt/dynamodb_local_latest.tar.gz && \
    tar xfz /tmp/dynamodb_local && rm -f /tmp/dynamodb_local

#nodejs and supervisor
RUN apt-get update && apt-get -y upgrade
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs supervisor
RUN apt-get clean

#dynamodb-admin
RUN npm install dynamodb-admin -g

VOLUME ["/var/dynamodb_local","/var/dynamodb_data"]
EXPOSE 8000 8001

COPY supervisord.conf /etc/supervisord.conf
RUN mkdir -p /var/log/supervisord

ENV DYNAMO_ENDPOINT http://0.0.0.0:8000/
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]