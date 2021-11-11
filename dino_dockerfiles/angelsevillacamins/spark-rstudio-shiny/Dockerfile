FROM ubuntu:14.04

MAINTAINER asevilla@inbionova.com

## General ENV
## R-base,  R-studio and shiny versions
ENV R_BASE_VERSION 3.3.1
ENV RSTUDIO_SERVER_VERSION 0.99.1251
ENV SHINY_SERVER_VERSION 1.4.2.786

## Password rstudio
ENV PASSWORD rstudio

## Spark version
ENV SPARK_VERSION 1.6.2

## Install Java8 and RStudio server dependencies
## From relateiq/oracle-java8
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
RUN apt-get -y update \
&& apt-get install -y --no-install-recommends \
    ca-certificates \
    gdebi-core \
    git \
    libapparmor1 \
    libedit2 \
    libcairo2-dev \
    libcurl4-openssl-dev \
    libssl1.0.0 \
    libssl-dev \
    libxml2-dev \
    libxt-dev \
    lsb-release \
    nano \
    psmisc \
    python-setuptools \
    openssh-client \
    oracle-java8-installer \
    software-properties-common \
    sudo \
    supervisor \
    pandoc \
    pandoc-citeproc \
    wget \
&& rm -rf /var/lib/apt/lists/

## Add Java binaries to PATH
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/jre
ENV PATH=$JAVA_HOME/bin:$PATH

## From  rocker/r-base
## Configure default locale, see https://github.com/rocker-org/rocker/issues/19
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
  && locale-gen en_US.utf8 \
  && /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

## R-studio as CRAN mirror
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" | sudo tee -a /etc/apt/sources.list \
  && gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \
  && gpg -a --export E084DAB9 | sudo apt-key add -
## R-base
## From rocker/r-base
RUN apt-get -y update \
  && apt-get install -y --no-install-recommends \
     littler \
     r-cran-littler \
     r-base=${R_BASE_VERSION}* \
	   r-base-dev=${R_BASE_VERSION}* \
     r-recommended=${R_BASE_VERSION}* \
  && echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), download.file.method = "libcurl")' >> /etc/R/Rprofile.site \
  && echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/install.r /usr/local/bin/install.r \
	&& install.r docopt \
	&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
## Rstudio server
## From rocker/r-studio
  && wget -q https://s3.amazonaws.com/rstudio-dailybuilds/rstudio-server-${RSTUDIO_SERVER_VERSION}-amd64.deb \
  && dpkg -i rstudio-server-${RSTUDIO_SERVER_VERSION}-amd64.deb  \
  && rm rstudio-server-*-amd64.deb \
  && ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc /usr/local/bin \
  && ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc-citeproc /usr/local/bin \
  && wget https://github.com/jgm/pandoc-templates/archive/1.15.0.6.tar.gz \
  && mkdir -p /opt/pandoc/templates && tar zxf 1.15.0.6.tar.gz \
  && cp -r pandoc-templates*/* /opt/pandoc/templates && rm -rf pandoc-templates* \
  && mkdir /root/.pandoc && ln -s /opt/pandoc/templates /root/.pandoc/templates \
  && rm -rf /var/lib/apt/lists/

## Add R-base, RStudio binaries to PATH
ENV PATH /usr/lib/rstudio-server/bin/:$PATH
ENV PATH /usr/local/bin/:$PATH

## Install devtools and Shiny
RUN install.r devtools
RUN R -e "install.packages(c('shiny','rmarkdown'), repos='https://cran.rstudio.com/')"

## Install additional R packages from CRAN or github
## RUN install.r dplyr
## RUN R -e "devtools::install_github('rstudio/sparklyr')"

## Install Shiny server
RUN wget -q https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-server-${SHINY_SERVER_VERSION}-amd64.deb \
&& gdebi --n shiny-server-${SHINY_SERVER_VERSION}-amd64.deb \
&& rm shiny-server-*-amd64.deb \
&& cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ \
&& rm -rf /var/lib/apt/lists/

## A default user system configuration
RUN useradd -m -d /home/rstudio rstudio \
  && echo "rstudio:${PASSWORD}" | chpasswd \
  && chown -R rstudio /home/rstudio \
  && chown -R rstudio /srv/shiny-server \
  && ln -s /srv/shiny-server /home/rstudio/

## Install Spark
## From https://www.anchormen.nl/spark-docker/
RUN wget http://apache.mirror.triple-it.nl/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.6.tgz \
&&  tar -xzf spark-${SPARK_VERSION}-bin-hadoop2.6.tgz \
&&  mv spark-${SPARK_VERSION}-bin-hadoop2.6 /opt/spark \
&&  rm spark-${SPARK_VERSION}-bin-hadoop2.6.tgz

ENV SPARK_HOME /opt/spark
ENV PATH $PATH:$SPARK_HOME/bin

## Set SPARK_HOME and the Spark installation directory in R environment
RUN echo "SPARK_HOME=$SPARK_HOME" >> /etc/R/Renviron.site
RUN echo "spark.install.dir=/opt/spark" >> /etc/R/Renviron.site

## Carina has some limitations regarding memory assignment
## and the following restriction should be added to avoid java errors
RUN echo "_JAVA_OPTIONS=-Xmx4g" >> /etc/R/Renviron.site

## Add conf files [to be used by supervisord for running spark master/worker]
COPY master.conf /opt/conf/master.conf
COPY worker.conf /opt/conf/worker.conf

## Expose port 8080 for spark master UI, 3838 for Shiny and 8787 for Rstudio
EXPOSE 8080
EXPOSE 3838
EXPOSE 8787
CMD ["/usr/bin/supervisord"]
