FROM heroku/jvm

ENV ACTIVATOR_VERSION 1.3.12

RUN cd /tmp && \
    wget http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \
    mkdir -p /usr/local/ && \
    unzip typesafe-activator-$ACTIVATOR_VERSION.zip -d /usr/local && \
    mv /usr/local/activator-dist-$ACTIVATOR_VERSION /usr/local/activator && \
    rm -f typesafe-activator-$ACTIVATOR_VERSION.zip
