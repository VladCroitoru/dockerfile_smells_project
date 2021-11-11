#R installation
FROM    phusion/baseimage

# Variables
ENV     DEBIAN_FRONTEND noninteractive
ENV     CRAN_MIRROR http://watson.nci.nih.gov/cran_mirror/

# Add cran mirror to package installer's sources list and update
RUN     echo "\n# R cran mirror" >> /etc/apt/sources.list
RUN     echo "deb $CRAN_MIRROR/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list

# Add the signed key
RUN     gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E084DAB9
RUN     gpg -a --export E084DAB9 | apt-key add -

# Update & upgrade packages
RUN     apt-get -y update; \
        /usr/bin/workaround-docker-2267; \
        apt-get -y upgrade

# Install R
RUN     apt-get install -y r-base

# Specify the CRAN mirror for R to use
#   source: http://stackoverflow.com/a/8475208/1967630
RUN     touch ~/.Rprofile
RUN     echo "options(repos=structure(c(CRAN=\"$CRAN_MIRROR\")))" >> ~/.Rprofile
