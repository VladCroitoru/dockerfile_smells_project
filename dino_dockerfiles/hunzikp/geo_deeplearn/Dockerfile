# Set the base image
FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

# Dockerfile author / maintainer 
MAINTAINER Philipp Hunziker <hunzikp@gmail.com> 


### Make user 'coder', pw 'deep', make sudo

RUN useradd -m -p BxRjFIHfl37dc -s /bin/bash coder
RUN usermod -aG sudo coder


### Python-related things

# Install apt-utils, python3, pip
RUN apt-get update && apt-get install -y apt-utils python3 python3-pip python3-dev

# Update pip
RUN pip3 install --upgrade pip

# Install TF dependencies
RUN apt-get -y install libcupti-dev

# Install tensorflow
RUN pip3 install tensorflow-gpu

# Install keras
RUN pip3 install keras

# Install sklearn, scikit-image, pandas
RUN pip3 install scikit-image
RUN pip3 install scikit-learn
RUN pip3 install pandas

# Install jupyter
RUN pip3 install jupyter

# Install pycharm
RUN apt-get install -y wget
RUN wget https://download.jetbrains.com/python/pycharm-community-2017.3.tar.gz
RUN tar xf pycharm-community-*.tar.gz -C /opt/

# Creates shortcut so that pycharm may be started anywhere using 'pycharm' in terminal
RUN ln -s /opt/pycharm-community-2017.3/bin/pycharm.sh /opt/pycharm-community-2017.3/bin/pycharm
RUN echo 'PATH=/opt/pycharm-community-2017.3/bin:$PATH' >> /home/coder/.bashrc

# Set locale (so that pycharm won't complain)
RUN apt-get install -y language-pack-en-base
RUN locale-gen en_US.UTF-8


### R-related things

# Install latest R
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
RUN gpg -a --export E084DAB9 | apt-key add -
RUN apt-get update
RUN apt-get install -y r-base r-base-dev

# Install Rstudio Server
RUN apt-get install -y gdebi-core
RUN wget https://download2.rstudio.org/rstudio-server-1.1.383-amd64.deb
RUN gdebi -n rstudio-server-1.1.383-amd64.deb
RUN echo 'server-app-armor-enabled=0' >> /etc/rstudio/rserver.conf

# Install R devtools package
RUN apt-get install -y build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev
RUN touch instl.txt \ 
	&& echo 'install.packages(c("devtools"), repos="http://cran.r-project.org" )' >> instl.txt
RUN Rscript --no-save --no-restore instl.txt
RUN rm instl.txt

# Install R geo packages
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable
RUN apt-get update
RUN apt-get install -y libudunits2-dev libgdal-dev libgeos-dev libproj-dev  
RUN touch instl.txt \ 
	&& echo 'install.packages(c("sf", "raster", "velox"), repos="http://cran.r-project.org" )' >> instl.txt
RUN Rscript --no-save --no-restore instl.txt
RUN rm instl.txt

# Tensorflow for R
RUN touch instl.txt \ 
	&& echo 'install.packages(c("tensorflow"), repos="http://cran.r-project.org" )' >> instl.txt
RUN Rscript --no-save --no-restore instl.txt
RUN rm instl.txt


### Version control

RUN apt-get install -y subversion git


