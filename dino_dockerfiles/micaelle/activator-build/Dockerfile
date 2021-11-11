# image for building Play 2.3 based app
FROM openjdk:8-slim
RUN apt-get update && apt-get install -y wget unzip scala

# avoid AWTError for org.GNOME.Accessibility.AtkWrapper
RUN sed -i 's/^assistive_technologies=/#&/' /etc/java-8-openjdk/accessibility.properties


# install sbt
ENV SBT sbt-0.13.8
RUN wget -q https://dl.bintray.com/sbt/debian/$SBT.deb && \
    dpkg -i $SBT.deb && rm $SBT.deb && \
    apt-get update && apt-get install sbt && \
    sbt sbtVersion


# install activator
ENV VER=1.3.12
ENV ACTIVATOR=activator-$VER-minimal
WORKDIR /opt
RUN wget -q http://downloads.typesafe.com/typesafe-activator/$VER/typesafe-$ACTIVATOR.zip && \
    unzip typesafe-$ACTIVATOR.zip && \
    rm typesafe-$ACTIVATOR.zip && \
    mv $ACTIVATOR activator


ENV PATH="${PATH}:/opt/activator:/opt/activator/bin"
RUN bash -c "source ~/.bashrc" && \
    chmod a+x /opt/activator/bin/activator

# run activator first time and cache its dependencies
RUN cd /tmp && activator new init play-scala && \
    rmdir --ignore-fail-on-non-empty /tmp/init

# don't forget to remove
RUN apt-get install -y git