FROM openjdk:latest

RUN apt-get update && apt-get install -y \
	build-essential \
	apt-transport-https \ 
	ca-certificates \
	curl \
	gnupg2 \
	software-properties-common \
	tar

## Docker static binaries
RUN curl -s https://download.docker.com/linux/static/stable/`uname -m`/docker-17.09.0-ce.tgz | tar xzvf - -C /usr/local/bin/ --strip-components=1

## Gradle
ENV GRADLE_HOME /opt/gradle
ENV GRADLE_VERSION 4.6
RUN wget --output-document=gradle.zip  https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip
RUN unzip gradle.zip \
	&& rm gradle.zip \
	&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \
	&& ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle
	
## Install Gauge to /usr/local/bin
RUN curl -SsL https://downloads.gauge.org/stable | sh

## emundo User
RUN addgroup --gid 1101 rancher && \
    # Für RancherOS brauchen wir diese Gruppe: http://rancher.com/docs/os/v1.1/en/system-services/custom-system-services/#creating-your-own-console
    addgroup --gid 999 aws && \
    # Für die AWS brauchen wir diese Gruppe
    useradd -ms /bin/bash emundo && \
    adduser emundo sudo && \
    # Das ist notwendig, damit das Image in RancherOS funktioniert
    usermod -aG 999 emundo && \
    # Das ist notwendig, damit das Image in RancherOS funktioniert
    usermod -aG 1101 emundo && \
    # Das ist notwendig, damit das Image lokal funktioniert
    usermod -aG root emundo

USER emundo
WORKDIR /home/emundo

# Install gauge plugins to /home/emundo/.gauge/plugin
RUN gauge install java && \  
	gauge install screenshot && \
	gauge install html-report &&\
	gauge install xml-report &&\
	gauge install spectacle

ENV PATH=$HOME/.gauge:$PATH
