## Emacs, make this -*- mode: sh; -*-
 
FROM ubuntu:latest

## This handle reaches Carl and Dirk
MAINTAINER "Flavio Barros" flaviomargarito@gmail.com

## Set a default user. Available via runtime flag `--user docker` 
## Add user to 'staff' group, granting them write privileges to /usr/local/lib/R/site.library
## User should also have & own a home directory (for rstudio or linked volumes to work properly). 
RUN useradd docker \
	&& mkdir /home/docker \
	&& chown docker:docker /home/docker \
	&& addgroup docker staff

## Noninteractive
ENV DEBIAN_FRONTEND=noninteractive

## Run update
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
		less \
		vim \
		wget \
		ca-certificates \
		fonts-texgyre \
		libssl-dev \
		curl \
		libssh2-1-dev \
		libcurl4-openssl-dev \
		texlive-full 

ENV R_BASE_VERSION 4.0.5 

## Now install R and littler, and create a link for littler in /usr/local/bin
## Also set a default CRAN repo, and make sure littler knows about it too
## NB '-t unstable' paused to allow drr35 repo to supply current ones
RUN apt-get update 
RUN apt-get install -y --no-install-recommends \
		littler \
                r-cran-littler \
		r-base \
		r-base-dev \
		r-recommended \
        && echo 'options(repos = c(CRAN = "https://cloud.r-project.org/"), download.file.method = "libcurl")' >> /etc/R/Rprofile.site \
        && echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/install.r /usr/local/bin/install.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/install2.r /usr/local/bin/install2.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
	&& install.r docopt devtools exams tools tth purrr tringr magrittr \
	&& install.r docopt httr devtools exams tools tth purrr tringr magrittr \
	&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
	&& rm -rf /var/lib/apt/lists/*

CMD ["R"]
