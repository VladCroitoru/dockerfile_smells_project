# Standalone antiSMASH build without databases
# VERSION 0.0.4
FROM antismash/base:4.0.0

MAINTAINER cheng gong <512543469@qq.com>

ENV ANTISMASH_URL="https://dl.secondarymetabolites.org/releases/"
ENV ANTISMASH_VERSION="4.0.0"

# Grab antiSMASH
RUN curl -L ${ANTISMASH_URL}/${ANTISMASH_VERSION}/antismash-${ANTISMASH_VERSION}.tar.gz > /tmp/antismash-${ANTISMASH_VERSION}.tar.gz && \
         tar xf /tmp/antismash-${ANTISMASH_VERSION}.tar.gz && \
         rm /tmp/antismash-${ANTISMASH_VERSION}.tar.gz

ADD instance.cfg /antismash-${ANTISMASH_VERSION}/antismash/config/instance.cfg

# Create the shared bgc_seeds.hmm file
RUN /antismash-${ANTISMASH_VERSION}/scripts/create_bgc_seeds.sh /antismash-${ANTISMASH_VERSION}

# compress the shipped profiles
RUN hmmpress /antismash-${ANTISMASH_VERSION}/antismash/specific_modules/nrpspks/abmotifs.hmm && \
         hmmpress /antismash-${ANTISMASH_VERSION}/antismash/specific_modules/nrpspks/dockingdomains.hmm && \
         hmmpress /antismash-${ANTISMASH_VERSION}/antismash/specific_modules/nrpspks/ksdomains.hmm && \
         hmmpress /antismash-${ANTISMASH_VERSION}/antismash/specific_modules/nrpspks/nrpspksdomains.hmm && \
         hmmpress /antismash-${ANTISMASH_VERSION}/antismash/specific_modules/nrpspks/sandpuma/flat/fullset0_smiles/fullset0_smiles_nrpsA.hmmdb && \
         hmmpress /antismash-${ANTISMASH_VERSION}/antismash/generic_modules/smcogs/smcogs.hmm && \
         hmmpress /antismash-${ANTISMASH_VERSION}/antismash/generic_modules/active_site_finder/hmm/p450.hmm3 && \
         hmmpress /antismash-${ANTISMASH_VERSION}/antismash/generic_modules/hmm_detection/bgc_seeds.hmm
ADD run /usr/local/bin/run

WORKDIR /usr/local/bin
RUN ln -s /antismash-${ANTISMASH_VERSION}/run_antismash.py

#VOLUME ["/input", "/output", "/databases"]
#WORKDIR /output

#ENTRYPOINT ["/usr/local/bin/run"]

#######miniconda##########
#FROM debian:8.5

#MAINTAINER Kamil Kwiek <kamil.kwiek@continuum.io>

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
RUN conda update --all -y&&\
         conda config --add channels r &&\
         conda config --add channels bioconda &&\
         conda config --set show_channel_urls yes &&\
         conda install prokka
         
#CMD ["/bin/bash"]

#######panX##########
RUN git clone https://github.com/neherlab/pan-genome-analysis.git &&\
         cd pan-genome-analysis &&\
         git submodule update --init &&\
         conda env create -f panX-environment.yml

#Expose port 8000 (webserver)
EXPOSE :8000

WORKDIR /pan-genome-analysis

ENTRYPOINT ["source activate panX"]
#CMD ["source activate panX"]