FROM ubuntu:20.04 AS base

LABEL image python-r-base

################ VARIABLES ################

# Environment variables available only at build time
ARG DEBIAN_FRONTEND=noninteractive

# Environment variables always available
ENV TZ=America/New_York
ENV LANG C.UTF-8

ENV R_GPG_KEY E298A3A825C0D65DFD57CBB651716619E084DAB9

ENV PYTHON_GPG_KEY E3FF2839C048B25C084DEBE9B26995E310250568
ENV PYTHON_VERSION 3.8.11
ENV PYTHON_PIP_VERSION 21.1.3
ENV PYTHON_GET_PIP_URL https://github.com/pypa/get-pip/raw/a1675ab6c2bd898ed82b1f58c486097f763c74a9/public/get-pip.py
ENV PYTHON_GET_PIP_SHA256 6665659241292b2147b58922b9ffe11dda66b39d52d8a6f3aa310bc1d60ea6f7
ENV PYTHON_POETRY_VERSION 1.1.6

################ BASE REQUIREMENTS ################

# Install base packages
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
    	curl \
		gnupg \
		sudo \
        wget \
    && apt-get update -y \
    && apt-get install -y \
        vim \
        software-properties-common \
        libssl-dev \
        libcurl4-openssl-dev \
        libxml2-dev \
        libbluetooth-dev \
        tk-dev \
        uuid-dev \
        libspatialindex-dev \
        libpq-dev \
		libglpk-dev\
    && rm -rf /var/lib/apt/lists/*

################ R ################

# Install base R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys "${R_GPG_KEY}"
RUN add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
RUN apt-get update -y \
    && apt-get install -y \
    	r-base \
        jags \
    && rm -rf /var/lib/apt/lists/*

################ POST INSTALLATION ################

# Install user yogi
RUN adduser yogi --disabled-password \
    && usermod -aG sudo yogi \
    && echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo "Set disable_coredump false" >> /etc/sudo.conf

USER yogi

WORKDIR /home/yogi
RUN mkdir -p /home/yogi/.R/lib
ENV R_LIBS="/home/yogi/.R/lib"

# Install R requirements
COPY --chown=yogi:yogi renv.lock .Rprofile /home/yogi/
COPY --chown=yogi:yogi renv/activate.R /home/yogi/renv/activate.R
RUN Rscript -e 'if(!requireNamespace("remotes")){install.packages("remotes");remotes::install_github("rstudio/renv")} else {remotes::install_github("rstudio/renv")}' \
    && Rscript -e 'renv::restore()'

CMD ["bash"]
