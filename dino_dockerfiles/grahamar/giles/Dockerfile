# Giles The Librarian
#
# VERSION       1.0

FROM ubuntu:latest

MAINTAINER Graham Rhodes <graham.a.r@gmail.com>

RUN apt-get update

# Create the MongoDB data directory and install dependencies
RUN mkdir -p /data/db && mkdir /data/.git_checkouts && \
  apt-get -y install openjdk-6-jdk git graphviz && apt-get clean

WORKDIR /opt

ADD https://nexus.gilt.com/nexus/content/repositories/internal-releases/com/gilt/giles_2.10/1.0.2/giles_2.10-1.0.2.tgz /opt/
RUN tar xfv /opt/giles_2.10-1.0.2.tgz

EXPOSE 1717

ENTRYPOINT ["/opt/giles-1.0.2/bin/giles"]
CMD ["-Dhttp.port=1717", "-Dconfig.file=/opt/giles-1.0.2/conf/production.application.conf"]
