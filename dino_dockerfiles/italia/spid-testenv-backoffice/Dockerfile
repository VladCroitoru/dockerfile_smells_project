FROM ubuntu:latest
MAINTAINER Umberto Rosini, rosini@agid.gov.it

# Create user to run is and the backoffice (not root for security reason!)
RUN useradd --user-group --create-home --shell /bin/false yoda

# Update and install utilities
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y vim && \
    apt-get install -y net-tools && \
    apt-get install -y unzip libxml2-utils

# Node 6
RUN apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt-get install -y nodejs && \
    apt-get install -y build-essential

# Oracle Java 8
RUN apt-get install -y software-properties-common python-software-properties && \
    add-apt-repository --yes ppa:webupd8team/java && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get install oracle-java8-set-default && \
    rm -rf /var/cache/oracle-jdk8-installer

ENV JAVA_HOME="/usr/lib/jvm/java-8-oracle"

# Backoffice
RUN mkdir /spid-testenvironment && \
    curl -o /spid-testenvironment/spid-testenv-backoffice.tar.gz https://codeload.github.com/italia/spid-testenv-backoffice/tar.gz/master && \
    mkdir /spid-testenvironment/bo && \
    tar -zxvf /spid-testenvironment/spid-testenv-backoffice.tar.gz -C /spid-testenvironment/bo --strip-components=1 && \
    rm -f /spid-testenvironment/spid-testenv-backoffice.tar.gz

# Build backoffice
RUN cd /spid-testenvironment/bo/backoffice && \
    npm install --suppress-warnings && \
    cd server && \
    npm install --suppress-warnings && \
    cd .. && \
    cd idp_metadata && \
    curl -o xmlsectool-2.0.0-bin.zip https://shibboleth.net/downloads/tools/xmlsectool/2.0.0/xmlsectool-2.0.0-bin.zip && \
    unzip xmlsectool-2.0.0-bin.zip && \
    rm xmlsectool-2.0.0-bin.zip && \
    cd .. && \
    npm run build-metadata && \
    npm run build

# Ports exposed
EXPOSE 8080

RUN chown -R yoda:yoda /spid-testenvironment/*

USER yoda

WORKDIR /spid-testenvironment/bo/backoffice

ENTRYPOINT ["npm", "run", "start-prod"]
