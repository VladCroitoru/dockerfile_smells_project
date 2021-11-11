ARG version=xenial
FROM ubuntu:${version}

LABEL maintainer="foersterfrank@gmx.de"

RUN apt update && apt install --yes \
	build-essential \
	cpanminus \
	libdbi* \
	libdbd* \
	libdbix* \
	libposix-strftime-compiler-perl \
	libapache-logformat-compiler-perl \
	mysql-client

RUN cpanm \
	Dancer2 \
	Dancer2::Plugin::DBIC

RUN apt install --yes \
    	apt-transport-https \
	python-software-properties \
	software-properties-common

RUN add-apt-repository ppa:webupd8team/java \
    && apt update \
    && echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
    && echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections \
    && apt install --yes oracle-java8-installer

RUN apt-key adv \
    	    --keyserver hkp://keyserver.ubuntu.com:80 \
	    --recv-keys 379CE192D401AB61 \
    && echo "deb https://dl.bintray.com/ontologizer/deb unstable main" \
       	    > /etc/apt/sources.list.d/ontologizer.list \
    && apt update && apt install --yes \
       	   ontologizer-cli

RUN apt install --yes \
        r-base \
	build-essential

RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("topGO",suppressUpdates=T, ask=F, suppressAutoUpdate=T);'
