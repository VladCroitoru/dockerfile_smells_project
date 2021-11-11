FROM openjdk:8
MAINTAINER ome-devel@lists.openmicroscopy.org.uk

ENV GRADLE_VERSION 3.5.1
RUN wget -q https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \
    && unzip gradle-${GRADLE_VERSION}-bin.zip -d /opt \
    && rm gradle-${GRADLE_VERSION}-bin.zip

COPY . /src

WORKDIR /src
RUN /opt/gradle-${GRADLE_VERSION}/bin/gradle build install

ENV ICE_CONFIG /src/ice.config
WORKDIR /src/build/install/src
CMD ["./bin/src"]
