FROM centos:7

RUN yum update -y && \
	yum clean all

##Extra
RUN yum -y update
RUN yum -y install \
           file which

RUN yum -y install binutils-devel gcc gcc-c++ gcc-gfortran git make patch python-devel \
	   glibc.i686 zlib.i686 ncurses-libs.i686 bzip2-libs.i686 uuid.i686 libxcb.i686 \
	   libXmu.so.6 libncurses.so.5 tcsh


#These are needed to build IRAF
RUN yum -y install \
           bzip2-devel \
           libXpm-devel libXft-devel libXext-devel \
           libxml2-devel \
           libuuid-devel \
           ncurses-devel \
           texinfo \
           wget \
	   bzip2 sudo passwd bc csh vim libXScrnSaver evince


## Intall minicoda python 2.7
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh  -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH


##With iraf
##Install
ENV PATH /opt/conda/bin:$PATH

#DS9
RUN wget http://ds9.si.edu/download/centos7/ds9.centos7.7.5.tar.gz  && tar -zxvf ds9.centos7.7.5.tar.gz && rm ds9.centos7.7.5.tar.gz

RUN mv ds9 /usr/bin

WORKDIR "/root"
#Install iraf
#Astroconda other way
#RUN /opt/conda/bin/conda config --add channels http://ssb.stsci.edu/astroconda
#RUN /opt/conda/bin/conda create -y -n iraf27 python=2.7 iraf pyraf Flask bokeh
ADD environmentpyraf.yml	      /root/
RUN conda env create -f environmentpyraf.yml
ADD login.cl /root/login.cl
ADD jupyter_notebook_config.py /root/.jupyter/
#RUN /opt/conda/envs/iraf27/bin/mkiraf


#RUN echo '#!/bin/bash' > clonerepo.sh && chmod +x clonerepo.sh
#RUN echo 'git clone https://github.com/manuelmarcano22/VIMOSReduced.git .' >> clonerepo.sh

##Clone Repo. T
#RUN git clone https://github.com/manuelmarcano22/VIMOSReduced.git
##Clone only tmp branch
RUN git clone https://github.com/manuelmarcano22/VIMOSReduced.git --branch temp --single-branch
#ADD downloadfitsdocker.sh /root/downloadfitsdocker.sh
#RUN /bin/bash /root/downloadfitsdocker.sh


# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]


EXPOSE  80 8080 8888
ADD start.sh /root/start.sh
RUN chmod +x start.sh
CMD ["/bin/bash", "start.sh"]
