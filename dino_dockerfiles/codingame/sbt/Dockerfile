FROM openjdk:8

ENV SBT_VERSION=0.13.15

# Install sbt
RUN apt-get update \
	&& apt-get install -y apt-transport-https \
	&& echo "deb https://dl.bintray.com/sbt/debian /" > /etc/apt/sources.list.d/sbt.list \
	&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 \
	&& apt-get update \
	&& apt-get install -y sbt="$SBT_VERSION" \
	&& rm -rf /var/lib/apt/lists/* \
	&& sbt sbtVersion
