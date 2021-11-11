FROM jenkinsci/jnlp-slave

MAINTAINER dookie23 <dookie10@gmail.com>
USER root

# Install system dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  git \
  jq \
  rsync \
  g++ \
  build-essential \
  libssl-dev \
  libssh2-1-dev \
  libcurl4-openssl-dev \
  libxml2-dev  \
  software-properties-common \
  && rm -rf /var/lib/apt/lists/*


# Install R
ENV R_BASE_VERSION 3.4
RUN add-apt-repository 'deb http://cloud.r-project.org/bin/linux/debian jessie-cran34/'

########################################################
## (Extract from: https://github.com/rocker-org/rocker/blob/e9758030e435915d5e6f21aaab0fc35a5a8efaae/r-base/Dockerfile)
## Set a default user. Available via runtime flag `--user docker`
## Add user to 'staff' group, granting them write privileges to /usr/local/lib/R/site.library
## User should also have & own a home directory (for rstudio or linked volumes to work properly).
RUN useradd docker \
    && mkdir /home/docker \
    && chown docker:docker /home/docker \
    && addgroup docker staff

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ed \
        less \
        locales \
        vim-tiny \
        wget \
        ca-certificates \
        fonts-texgyre \
    && rm -rf /var/lib/apt/lists/*

## Configure default locale, see https://github.com/rocker-org/rocker/issues/19
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen en_US.utf8 \
    && /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

## Now install R and littler, and create a link for littler in /usr/local/bin
## Also set a default CRAN repo, and make sure littler knows about it too
RUN apt-get update \
    && apt-get install -y --force-yes --no-install-recommends \
        littler \
        r-base=${R_BASE_VERSION}* \
        r-base-dev=${R_BASE_VERSION}* \
        r-recommended=${R_BASE_VERSION}* \
        && echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), download.file.method = "libcurl")' >> /etc/R/Rprofile.site \
        && echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \
    && ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r \
    && ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r \
    && ln -s /usr/share/doc/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
    && ln -s /usr/share/doc/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
    && install.r docopt \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
    && rm -rf /var/lib/apt/lists/*

########################################################


# Install R build packages
RUN R -e "install.packages(c('testthat', 'devtools', 'roxygen2'), repos='http://cloud.r-project.org/')"

# Install Docker binary
ENV DOCKER_VERSION 1.12.6
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && tar --strip-components=1 -xvzf docker-${DOCKER_VERSION}.tgz -C /usr/bin

USER jenkins
