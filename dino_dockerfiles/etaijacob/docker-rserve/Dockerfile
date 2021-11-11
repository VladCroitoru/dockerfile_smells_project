
FROM ubuntu:latest
MAINTAINER etai@cgen.com

# Update
RUN apt-get update

# Install wget
RUN apt-get install -y wget
RUN apt-get install -y sudo
RUN apt-get install apt-utils

# Install latest R
RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list'
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
RUN gpg -a --export E084DAB9 | sudo apt-key add -


# Update and install
RUN apt-get update && apt-get install -y \
  r-base \
  r-recommended \
  r-base-dev \
  libcurl4-gnutls-dev \
  libxml2-dev \
  libmime-base64-urlsafe-perl \
  libdigest-hmac-perl \
  libdigest-sha-perl \
  libssl-dev \
  libapparmor1



# log R version
RUN R --version

#install R packages
RUN sudo su - -c "/usr/bin/R -e \"install.packages('Rserve', repos='http://cran.r-project.org')\""
RUN sudo su - -c "/usr/bin/R -e \"install.packages('dplyr', repos='http://cran.r-project.org')\""
RUN sudo su - -c "/usr/bin/R -e \"install.packages('data.table', repos='http://cran.r-project.org')\""
RUN sudo su - -c "/usr/bin/R -e \"install.packages('reshape2', repos='http://cran.r-project.org')\""

# adding start R script: you can find the RScript on the docker github
ADD start.R start.R
ADD Rserv.conf /Rserv.conf
EXPOSE 6311
CMD Rscript start.R
