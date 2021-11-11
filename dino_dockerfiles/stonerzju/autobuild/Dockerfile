# Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Michael Chen "Michael.chen@schneider-electric.com"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# gcc are required to build python package twisted
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 curl grep sed openssh-server\
    git mercurial subversion gcc openssh-server
	
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.3.14-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda create -q -y --name py35 python=3.5 && \
	conda create -q -y --name py27 python=2.7

# ADD or COPY command need use absolute file path
ADD requirement /root/requirement

# default shell is /bin/sh, command source require use /bin/bash
RUN /bin/bash -c "source activate py35; \
	pip install -r /root/requirement"

RUN mkdir /var/run/sshd	
RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]	
EXPOSE 80
EXPOSE 22
