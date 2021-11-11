FROM ubuntu:latest
MAINTAINER nathan.trujillo@intensity.com
WORKDIR /app

## Add in custom scripts
ADD ./gbm.zip /gbm.zip
ADD ./go.R /go.R
ADD ./go.m /go.m

RUN apt-get update

## Install R
## https://www.datascienceriot.com/how-to-install-r-in-linux-ubuntu-16-04-xenial-xerus/kris/
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
RUN gpg -a --export E084DAB9 | apt-key add -
RUN apt-get update
RUN apt-get install -y r-base r-base-dev octave ed libcurl4-openssl-dev libssl-dev pandoc libxml2-dev

## Install the R libraries
RUN unzip /gbm.zip
RUN Rscript /go.R
RUN R CMD build ./gbm
RUN R CMD INSTALL ./gbm_2.1.3.tar.gz

## Install octave and octave-dev (for building stuff)
RUN apt-get install -y octave liboctave-dev
## Install the libraries
RUN octave /go.m

## Install aws cli
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# Node JS 6
RUN curl -sL https://deb.nodesource.com/setup_6.x -o /nodesource_setup.sh
RUN bash /nodesource_setup.sh
RUN apt-get install -y nodejs
#RUN ln -s "$(which nodejs)" /usr/bin/node

RUN apt-get install -y sudo
ADD ./addUser.sh /addUser.sh
RUN bash /addUser.sh avgjoe

## Clean up downloads
RUN rm -rf /app/* /nodesource_setup.sh /go.R /go.m /gbm /gbm.zip 2>/dev/null
