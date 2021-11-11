# Galaxy - requirements according to https://wiki.galaxyproject.org/Admin/Config/ToolDependenciesList
#
# VERSION   2015.1
# Updated to ubuntu 17.10 as this is easier than pinning stuff from artful repositories in order to get slurm working.

FROM ubuntu:17.10

MAINTAINER Björn A. Grüning, Dave Bouvier

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && apt-get install --no-install-recommends -y apt-transport-https software-properties-common python-software-properties && \ 
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9 && \
    apt-get update -qq && apt-get upgrade -y && \
    apt-get install --no-install-recommends -y autoconf automake build-essential gfortran cmake \
    git-core libatlas-base-dev libblas-dev liblapack-dev openssl \
    openjdk-8-jre python-dev python-setuptools \
    python-virtualenv zlib1g-dev libyaml-dev subversion pkg-config slurm-client munge && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    git clone --branch 1.2 https://github.com/samtools/htslib.git && \
    git clone --branch 1.2 https://github.com/samtools/bcftools.git && \
    make -C bcftools && cp bcftools/bcftools /usr/bin && \
    rm -rf bcftools htslib
