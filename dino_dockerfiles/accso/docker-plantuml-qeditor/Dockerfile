# See https://github.com/accso/docker-plantuml-qeditor
FROM debian:buster
MAINTAINER marcus.rickert@accso.de
RUN adduser --disabled-login --uid 1000 plantuml
RUN chown plantuml.plantuml /home/plantuml
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
           graphviz \
	   cmake \
	   g++ \
	   qt5-default \
	   libqt5core5a \
	   libqt5svg5 \
	   libqt5svg5-dev \
	   curl \
	   make \
	   unzip \
	   openjdk-8-jre-headless \
    && mkdir -p /opt/etc \
    && mkdir -p /opt/run \
    && curl -s -o /opt/run/plantuml.jar -L http://sourceforge.net/projects/plantuml/files/plantuml.jar/download \
    && mkdir -p /tmp/install \
    && cd /tmp/install \
    && curl -s -o master.zip -L https://github.com/borco/plantumlqeditor/archive/master.zip \
    && unzip master.zip \
    && cd plantumlqeditor-master \
    && cmake -G "Unix Makefiles" \
    && qmake \
    && make \
    && cp -r plantumlqeditor assistant.xml icons /opt/run \
    && cd /tmp \
    && rm -rf /tmp/install \
    && DEBIAN_FRONTEND=noninteractive apt-get -y remove --purge \
          cmake \
	  g++ \
	  make \
	  unzip \
    && DEBIAN_FRONTEND=noninteractive apt-get -y autoremove
COPY assets/docker-entrypoint.sh /docker-entrypoint.sh
COPY assets/PlantUMLEditor.conf /opt/etc
COPY assets/QtProject.conf /opt/etc
ENTRYPOINT [ "/docker-entrypoint.sh" ]
