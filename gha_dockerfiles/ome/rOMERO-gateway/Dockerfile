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
COPY tests /src/tests/
COPY install.R /src/
COPY .Rbuildignore /src/

# Dependencies necessary for install.R
RUN echo "deb-src http://deb.debian.org/debian testing main" >> /etc/apt/sources.list
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
RUN apt-get -y install libssl-dev libxml2-dev libcurl4-gnutls-dev

#########################################################################################
## Necessary for running maven
## copied from https://hub.docker.com/r/cardcorp/r-java/~/dockerfile/
##
## gnupg is needed to add new key
RUN apt-get update && apt-get install -y gnupg2

## Install Java 
RUN apt-get install -y openjdk-11-jdk \
    && update-alternatives --display java \
    && echo "MAVEN IS NOT IN THE UPSTREAM LIST (JOSH)" \
    && apt-get install -y maven \ 
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && R CMD javareconf

## make sure Java can be found in rApache and other daemons not looking in R ldpaths
RUN echo "/usr/lib/jvm/java-11-openjdk-amd64/" > /etc/ld.so.conf.d/rJava.conf
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
ENV OMERO_LIBS_DOWNLOAD=TRUE
CMD ["/src/tests/runtest"]
