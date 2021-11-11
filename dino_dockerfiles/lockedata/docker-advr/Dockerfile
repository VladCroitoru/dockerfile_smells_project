FROM lockedata/docker-intror
MAINTAINER Steph Locke <steph@itsalocke.com>
# Instal python stuff
RUN apt-get update --fix-missing \
	&& apt-get install -y \
		ca-certificates \
    	libglib2.0-0 \
	 	libxext6 \
	   	libsm6  \
	   	libxrender1 \
		libxml2-dev

# install python3, virtualenv and anaconda

RUN apt-get install -y \
		python3-pip \
		python3-dev \
	&& pip3 install virtualenv

# install anaconda

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

ENV PATH /opt/conda/bin:$PATH

# install h2o
RUN apt-get update -qq \
  && apt-get -y --no-install-recommends install \
    default-jdk \
    default-jre \
  && R CMD javareconf \
  && install2.r --error \
    --repos 'http://cran.rstudio.com' \
    h2o

# instal js deps
RUN apt-get install -y libv8-dev
	
# install r deps
RUN R -e 'devtools::install_github("lockedata/DOCKER-advR")' \
  && R -e 'sparklyr::spark_install("2.2.1","2.7")'



