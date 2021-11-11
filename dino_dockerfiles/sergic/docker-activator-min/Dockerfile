#docker run --name=activator --rm=true -a stdin -a stdout -i -t sergic/docker-activator-min

FROM podbox/java8

ENV ACTIVATOR_VERSION 1.3.7

RUN \
    apt-get install -yq wget unzip && \
    cd /tmp && \
    wget  --progress=dot:mega https://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION-minimal.zip && \
    unzip typesafe-activator-$ACTIVATOR_VERSION-minimal.zip && \
    mkdir /opt/typesafe && \
    mv /tmp/activator-$ACTIVATOR_VERSION-minimal /opt/typesafe/activator-$ACTIVATOR_VERSION && \
    ln -s /opt/typesafe/activator-$ACTIVATOR_VERSION/activator /usr/local/bin/activator && \
    rm /tmp/typesafe-activator-$ACTIVATOR_VERSION-minimal.zip