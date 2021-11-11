FROM  ipython/scipystack

MAINTAINER John McCallum cfljam@users.noreply.github.com

####### R install ######################
## Following https://registry.hub.docker.com/u/rocker/r-base/dockerfile ####

RUN useradd docker \
  && mkdir /home/docker \
  && chown docker:docker /home/docker \
  && addgroup docker staff

## Install _all_ prerequisites in hope that they do not change much.
## follow recommendations https://docs.docker.com/articles/dockerfile_best-practices/#run
RUN set -xe ;\
  apt-get update;\
  apt-get -y upgrade;\
  apt-get -y dist-upgrade ;\
  apt-get autoremove;\
  apt-get autoclean;\
  apt-get install -y --no-install-recommends\
    asciidoc \
    less \
    locales \
    libicu-dev\
    libncurses5-dev \
    libpango-1.0-0\
    libpq-dev \
    libxml2 \
    libxml2-dev \
    libxml2-utils \
    nano\
    wget \
  && rm -rf /var/lib/apt/lists/*

## Configure default locale, see https://github.com/rocker-org/rocker/issues/19
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
  && locale-gen en_US.utf8 \
  && /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8

## Use Ubuntu repo at CRAN, and use RStudio CDN as mirror
## This gets us updated r-base, r-base-dev, r-recommended and littler
RUN gpg --keyserver hkp://pgpkeys.mit.edu:80 --recv-key 51716619E084DAB9  \
&& gpg -a --export 51716619E084DAB9 | sudo apt-key add  - \
  && echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" > /etc/apt/sources.list.d/r-cran.list

ENV R_BASE_VERSION 3.2.0

## Now install R and littler, and create a link for littler in /usr/local/bin
## Also set a default CRAN repo, and make sure littler knows about it too
RUN apt-get update \
  && apt-get install  -y --force-yes --no-install-recommends \
		littler \
		r-base=${R_BASE_VERSION}* \
		r-base-dev=${R_BASE_VERSION}* \
		r-recommended=${R_BASE_VERSION}* \
        && echo 'options(repos = list(CRAN = "http://cran.rstudio.com/"))' >> /etc/R/Rprofile.site \
        && echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \
	&& ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r \
	&& ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r \
	&& ln -s /usr/share/doc/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
	&& ln -s /usr/share/doc/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
	&& install.r docopt \
	&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
	&& rm -rf /var/lib/apt/lists/*

## Set a default CRAN Repo
RUN mkdir -p /etc/R \
  && echo 'options(repos = list(CRAN = "http://cran.rstudio.com/"))' >> /etc/R/Rprofile.site

## Install  R packages for Generic Data Manipulation
ADD R-requirements.txt /tmp/
RUN install2.r --error $(cat /tmp/R-requirements.txt)

## Install rpy2 for R magics
RUN python2 /usr/local/bin/pip   --default-timeout=100 install rpy2

##Install R kernel for all users
RUN install.r devtools \
&& git clone https://github.com/armstrtw/rzmq.git --recursive \
&& echo "library(devtools) ; install_local('./rzmq')" | r  \
&& echo "library(devtools) ; install_github('IRkernel/repr' )" | r  \
&& echo "library(devtools) ; install_github(c('IRkernel/IRdisplay','IRkernel/IRkernel'))" | r \
&& echo "IRkernel::installspec(user=FALSE)" | r

### Install the Reveal Slideshow
RUN set -xe ;\
	git clone https://github.com/damianavila/RISE ;\
  cd RISE ;\
  git checkout tags/3.x ;\
  python setup.py install

## set up for Gisting Notebooks
RUN apt-get update \
  && apt-get install  -y --force-yes --no-install-recommends \
	ruby; \
  gem install gist

### Bash Shell
RUN pip install bash_kernel

#########
## Clean up
RUN rm -rf /tmp/*
##########################################
### Launch ipynb as default 

CMD  ipython notebook  --ip=0.0.0.0 --port=8888 --no-browser

##################### INSTALLATION END #####################

## TEST
WORKDIR /tmp
ADD ./test-suite.sh /tmp/test-suite.sh
RUN ./test-suite.sh
