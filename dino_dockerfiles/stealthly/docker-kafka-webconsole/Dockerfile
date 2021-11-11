FROM stealthly/docker-java

MAINTAINER stealthly

ENV PLAY_VERSION 2.2.3
ENV PLAY_RELEASE play-$PLAY_VERSION
ENV PLAY_URL http://downloads.typesafe.com/play/$PLAY_VERSION/$PLAY_RELEASE.zip
ENV PLAY_HOME /opt/$PLAY_RELEASE

ENV KAFKA_CONSOLE_URL https://github.com/claudemamo/kafka-web-console.git
ENV KAFKA_CONSOLE_HOME /opt/kafka-web-console

RUN wget -q $PLAY_URL -O /tmp/$PLAY_RELEASE.zip
RUN unzip /tmp/$PLAY_RELEASE.zip -d /opt

RUN cd /opt && git clone $KAFKA_CONSOLE_URL

EXPOSE 9000

CMD cd $KAFKA_CONSOLE_HOME && $PLAY_HOME/play -DapplyEvolutions.default=true start
