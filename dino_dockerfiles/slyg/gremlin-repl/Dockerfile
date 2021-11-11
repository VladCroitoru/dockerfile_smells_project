FROM java:8u72-jdk

ENV GREMLIN_VERSION 3.2.0-incubating
ENV WORKSPACE gremlin

RUN wget http://mirrors.ukfast.co.uk/sites/ftp.apache.org/incubator/tinkerpop/${GREMLIN_VERSION}/apache-gremlin-console-${GREMLIN_VERSION}-bin.zip \
 && unzip apache-gremlin-console-${GREMLIN_VERSION}-bin.zip \
 && mv apache-gremlin-console-${GREMLIN_VERSION} $WORKSPACE

WORKDIR $WORKSPACE

CMD bin/gremlin.sh
