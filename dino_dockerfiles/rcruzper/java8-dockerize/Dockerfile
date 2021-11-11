FROM java:8
MAINTAINER Raúl Cruz

# install Dockerize
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz
RUN rm dockerize-linux-amd64-v0.2.0.tar.gz

# install Java Cryptography Extension
RUN cd /tmp/ && \
    curl -LO "http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip" -H 'Cookie: oraclelicense=accept-securebackup-cookie' && \
    unzip jce_policy-8.zip && \
    rm jce_policy-8.zip && \
    yes |cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/

# remove wget
RUN apt-get --purge autoremove -y wget

# install newrelic APM agent
ADD newrelic.jar .
ADD newrelic.yml .

# install entryproint script
ADD entrypoint.sh .
