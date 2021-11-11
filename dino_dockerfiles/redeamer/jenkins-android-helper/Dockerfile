FROM openjdk:8-jdk
MAINTAINER Michael Musenbrock

RUN apt-get update && apt-get install -y --no-install-recommends \
		wget \
		lsof \
		python3 \
	&& rm -rf /var/lib/apt/lists/*
RUN wget "https://github.com/redeamer/jenkins-android-helper/releases/download/0.2.04/jenkins-android-helper_0.2.04_all.deb"
RUN dpkg -i jenkins-android-helper_0.2.04_all.deb
RUN groupadd -g 1000 user && useradd -M -u 1000 -g 1000 -d / -s /usr/sbin/nologin user
