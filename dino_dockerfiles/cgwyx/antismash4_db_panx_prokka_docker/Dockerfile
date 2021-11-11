# Standalone antiSMASH build
# VERSION 0.0.5

FROM antismash/standalone-lite:4.0.0

MAINTAINER cheng gong <512543469@qq.com>

ENV ANTISMASH_URL="https://dl.secondarymetabolites.org/releases"
ENV ANTISMASH_VERSION="4.0.0"

# Grab the databases
WORKDIR /antismash-${ANTISMASH_VERSION}
RUN python download_databases.py

ADD instance.cfg antismash/config/instance.cfg

#VOLUME ["/input", "/output"]
#WORKDIR /output

#ENTRYPOINT ["/usr/local/bin/run"]

#######miniconda##########
#FROM debian:8.5

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
         libglib2.0-0 libxext6 libsm6 libxrender1 \
        git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
         wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.3.14-Linux-x86_64.sh -O ~/miniconda.sh && \
         /bin/bash ~/miniconda.sh -b -p /opt/conda && \
         rm ~/miniconda.sh

RUN apt-get install -y curl grep sed dpkg && \
        TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
        curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
        dpkg -i tini.deb && \
        rm tini.deb && \
        apt-get clean
    
ENV PATH /opt/conda/bin:$PATH

#ENTRYPOINT [ "/usr/bin/tini", "--" ]
#CMD [ "/bin/bash" ]    

#######prokka##########
RUN conda update --all -y &&\
         conda config --add channels r &&\
         conda config --add channels bioconda &&\
         conda config --set show_channel_urls yes &&\
         conda install -y prokka=1.12
         
#CMD ["/bin/bash"]
#######panx##########
RUN conda update --all -y &&\
         conda config --add channels r &&\
         conda config --add channels bioconda &&\
         conda config --add channels conda-forge &&\
         #conda config --add channels defaults &&\
         #conda config --set show_channel_urls yes
         git clone https://github.com/neherlab/pan-genome-analysis.git &&\
         cd pan-genome-analysis &&\
         git submodule update --init &&\
         conda install -y python=2.7.13 biopython=1.66 numpy=1.10.4 scipy=0.16.1 pandas=0.16.2 ete2=2.3.10  diamond=0.8.36  fasttree=2.1.9 mafft=7.305 mcl=14.137 raxml=8.2.9

#Expose port 8000 (webserver)
EXPOSE :8000

WORKDIR /pan-genome-analysis

CMD ["/bin/bash"]