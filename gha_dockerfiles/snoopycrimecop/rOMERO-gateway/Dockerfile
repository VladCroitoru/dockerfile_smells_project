# Build the local source. Not yet optimized but
# leaves development tools in place.
FROM r-base

# Manually copy the files relevant for the build.
# This speeds up the build process while the docker
# file itself is being developed, but eventually
# `COPY . /src/` may be preferred.
COPY R /src/R/
COPY NAMESPACE /src/
COPY DESCRIPTION /src/
COPY man /src/man/
COPY pom.xml /src/
COPY tests /src/tests/
COPY install.R /src/

# Dependencies necessary for install.R
RUN echo "deb-src http://deb.debian.org/debian testing main" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get -y install libssl-dev libxml2-dev libcurl4-openssl-dev

#########################################################################################
## Necessary for running maven
## copied from https://hub.docker.com/r/cardcorp/r-java/~/dockerfile/
##
## gnupg is needed to add new key
RUN apt-get update && apt-get install -y gnupg2

## Install Java 
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" \
      | tee /etc/apt/sources.list.d/webupd8team-java.list \
    &&  echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" \
      | tee -a /etc/apt/sources.list.d/webupd8team-java.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \
    && echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" \
        | /usr/bin/debconf-set-selections \
    && apt-get update \
    && apt-get install -y oracle-java8-installer \
    && update-alternatives --display java \
    && echo "MAVEN IS NOT IN THE UPSTREAM LIST (JOSH)" \
    && apt-get install -y maven \ 
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && R CMD javareconf

## make sure Java can be found in rApache and other daemons not looking in R ldpaths
RUN echo "/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server/" > /etc/ld.so.conf.d/rJava.conf
RUN /sbin/ldconfig

## Install rJava package
RUN install2.r --error rJava \
  && rm -rf /tmp/downloaded_packages/ /tmp/*.rds
##
##
#########################################################################################

RUN useradd -ms /bin/bash t && chown -R t /src/
RUN chown t /usr/local/lib/R/site-library
USER t
WORKDIR /src
RUN Rscript install.R --local
