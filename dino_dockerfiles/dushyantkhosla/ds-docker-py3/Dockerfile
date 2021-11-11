FROM centos:latest
MAINTAINER Dushyant Khosla <dushyant.khosla@yahoo.com

# === COPY FILES ===

COPY environment.yml /root/environment.yml
COPY start.sh /etc/profile.d/
COPY pip.conf /root/pip.conf

# === SET ENVIRONMENT VARIABLES ===

ENV PATH="/miniconda/bin:${PATH}"
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8

# === INSTALL DEPENDENCIES ===

WORKDIR /root
RUN yum -y install bzip2 \
                   wget \
                   which \
		   curl \
	&& yum -y groupinstall "Development Tools" \
	&& yum -y remove git \
	&& yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
	&& yum -y install git2u-core.x86_64 \
	&& wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh \
	&& bash miniconda.sh  -b -p /miniconda \
	&& conda config --append channels conda-forge \
	&& conda env create -f environment.yml \
	&& conda clean -i -l -t -y \
	&& rm miniconda.sh \
	&& wget https://download.opensuse.org/repositories/shells:fish:release:2/CentOS_7/shells:fish:release:2.repo -P /etc/yum.repos.d/ \
	&& yum install -y fish \
	&& yum -y autoremove \
	&& yum clean all \
	&& rm -rf /var/cache/yum \
  && yum makecache \
  && yum install -y 'graphviz*'

# === INITIALIZE ===
WORKDIR /home/
EXPOSE 8888
EXPOSE 5000
EXPOSE 3128
CMD /usr/bin/bash
