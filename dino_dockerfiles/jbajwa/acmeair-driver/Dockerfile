FROM travix/base-debian-jre8

MAINTAINER Jaideep Bajwa

RUN apt-get update && apt-get install -y \
    curl

COPY ./ /acmeair/acmeair-driver

WORKDIR /acmeair/acmeair-driver

# apache jmeter with acmeair driver tar, simple_json tar
# and other summary setting enabled
RUN tar -xf deps/apache-jmeter-2.9.tar && \
    rm deps/apache-jmeter-2.9.tar \
    rm -rf .git

ENV JMETER_HOME=/acmeair/acmeair-driver/apache-jmeter-2.9

WORKDIR /acmeair/acmeair-driver/acmeair-jmeter/scripts

RUN chmod u+x ./run.sh

ENTRYPOINT ["./run.sh"]
