# Use phusion/baseimage as base image
FROM phusion/baseimage:0.9.19

# Set environment variables the phusion way
RUN echo en_US.UTF-8 > /etc/container_environment/LANGUAGE
RUN echo en_US.UTF-8 > /etc/container_environment/LANG
RUN echo en_US.UTF-8 > /etc/container_environment/LC_ALL
RUN echo UTF-8 > /etc/container_environment/PYTHONIOENCODING

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

MAINTAINER Simon Frost <sdwfrost@gmail.com>

## Set a default user. Available via runtime flag `--user docker`
RUN useradd docker \
	&& mkdir /home/docker \
	&& chown docker:docker /home/docker \
	&& mkdir /home/docker/programs \
	&& addgroup docker staff

RUN apt-get update -qq && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
 	build-essential \
 	python3-dev \
	git \
	wget \
	cmake \
  nodejs \
  npm \
  libudunits2-dev \
  graphviz-dev

## Add RethinkDB repository

RUN echo "deb http://download.rethinkdb.com/apt xenial main" > /etc/apt/sources.list.d/rethinkdb.list
RUN wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | apt-key add -
RUN apt-get update -qq && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends rethinkdb

## Add R

RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" >> /etc/apt/sources.list'
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
RUN apt-get update -qq && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends  \
  default-jdk \
	perl \
	libcurl4-openssl-dev \
  r-base \
  r-base-dev

#setup R configs
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.rstudio.com'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages('ape')"
RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('ggforce')"
RUN Rscript -e "install.packages('plotly')"
RUN Rscript -e "install.packages('rethinker')"
RUN Rscript -e "install.packages('cowplot')"
RUN Rscript -e "install.packages('DT')"
RUN Rscript -e "install.packages('xtable')"

# Install the recent pip release
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
	python3 get-pip.py && \
	rm get-pip.py	&& \
	# Install nexthiv
	pip3 install git+https://github.com/sdwfrost/nexthiv@master

# Install IQ-TREE
RUN cd /home/docker/programs && \
	git clone https://github.com/Cibiv/IQ-TREE.git && \
	cd IQ-TREE && \
	mkdir build && \
	cd build && \
	cmake -DIQTREE_FLAGS=omp .. && \
	make && \
	cp iqtree-omp /usr/local/bin && \
	rm -rf /home/docker/programs/IQ-TREE

# Install TN93
RUN cd /home/docker/programs && \
  git clone https://github.com/veg/tn93 && \
  cd tn93 && \
  cmake . && \
  make install && \
  rm -rf /home/docker/programs/tn93

# Chateau
RUN npm install -g chateau

# RethinkDB stuff
VOLUME ["/data"]
WORKDIR /data

CMD ["rethinkdb","--bind","all"]
CMD ["chateau"]

EXPOSE 8080
EXPOSE 28015
EXPOSE 29015
EXPOSE 3000

#VOLUME ["data"]
