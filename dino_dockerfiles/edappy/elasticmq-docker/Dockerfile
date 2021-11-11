FROM       ubuntu:14.04
MAINTAINER Edappy

RUN sudo apt-get update && apt-get install default-jre -y

ADD  https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-server-0.9.0-beta1.jar /elasticmq/elasticmq-server-0.9.0-beta1.jar
ADD  elasticmq.conf /elasticmq/elasticmq.conf
ADD  custom.conf /elasticmq/custom.conf
ADD  run /elasticmq/run
RUN  chmod +x /elasticmq/run

EXPOSE 9324

ENTRYPOINT ["/elasticmq/run"]
CMD        []
