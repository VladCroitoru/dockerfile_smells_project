FROM pamtrak06/ubuntu16.04-jdk7

RUN apt-get update && \
    apt-get install -y wget unzip

ENV DEGREE_VERSION=3.3.20

RUN wget http://repo.deegree.org/content/repositories/public/org/deegree/deegree-webservices/${DEGREE_VERSION}/deegree-webservices-${DEGREE_VERSION}.zip
RUN unzip deegree-webservices-${DEGREE_VERSION}.zip

WORKDIR /deegree-webservices-${DEGREE_VERSION}

CMD [ "/deegree-webservices-${DEGREE_VERSION}/start-deegree-linux.sh" ]
