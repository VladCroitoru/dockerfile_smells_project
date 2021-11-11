FROM dockerfile/java

MAINTAINER SequenceIq

# install the ec2 cli tools
RUN apt-get update
RUN apt-get -y install awscli

ADD snapshot.sh /etc/snapshot.sh
RUN chmod +x /etc/snapshot.sh

ENTRYPOINT ["/etc/snapshot.sh"]
