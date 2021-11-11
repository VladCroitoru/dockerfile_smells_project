FROM redsnow1992/ubuntu-oracle-jdk
ENV DEBIAN_FRONTEND noninteractive
ENV SCALA_VERSION 2.11.7
ENV ACTIVATOR_VERSION 1.3.5

RUN apt-get update -y && apt-get install -y unzip && apt-get install -y wget

RUN wget -O scala-$SCALA_VERSION.deb http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.deb?_ga=1.125690446.532480391.1437734713
RUN dpkg -i scala-$SCALA_VERSION.deb

RUN wget https://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip
RUN unzip typesafe-activator-$ACTIVATOR_VERSION.zip
RUN mv activator-dist-$ACTIVATOR_VERSION /opt
RUN rm typesafe-activator-$ACTIVATOR_VERSION.zip && chmod a+x /opt/activator-dist-$ACTIVATOR_VERSION/activator
ENV PATH $PATH:/opt/activator-dist-$ACTIVATOR_VERSION

EXPOSE 9000 8888
RUN mkdir -p /srv/app
WORKDIR /srv/app


CMD ["activator", "run"]

# reference from https://registry.hub.docker.com/u/ingensi/play-framework/dockerfile/
# reference https://registry.hub.docker.com/u/dordoka/play-framework/dockerfile/
# docker run -v /home/donald/git_repo/play-demo/:/srv/app:rw -p 80:8888 -u $(id -u) playframework
