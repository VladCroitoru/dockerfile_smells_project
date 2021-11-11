## Neo4J dependency: java
## get java from official repo
FROM java:latest
MAINTAINER Tiago Pires, tandrepires@gmail.com

## install neo4j according to http://www.neo4j.org/download/linux
# Import neo4j signing key
# Create an apt sources.list file
# Find out about the files in neo4j repo ; install neo4j community edition

RUN wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key add - && \
    echo 'deb http://debian.neo4j.org/repo stable/' > /etc/apt/sources.list.d/neo4j.list && \
    apt-get update ; apt-get install neo4j -y

ADD launch.sh /
RUN chmod +x /launch.sh

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# expose REST and shell server ports
EXPOSE 7474
EXPOSE 1337

WORKDIR /

## entrypoint
CMD ["/bin/bash", "-c", "/launch.sh"]
