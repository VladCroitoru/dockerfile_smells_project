FROM ubuntu

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy

ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

ENV PATH $PATH:/opt/conda/bin
ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]

COPY environment.yml /
RUN conda env create -f /environment.yml
ENV PATH /opt/conda/envs/tf-activity/bin:$PATH

# Install container-wide requrements gcc, pip, zlib, libssl, make, libncurses, fortran77, g++, R
RUN apt-get update && \
    apt-get install -y \
    git \
    gcc \
    g++ \
    make \
    perl \
    wget \
    build-essential \
    libbz2-dev \
    libcurl4-openssl-dev \
    liblzma-dev \
    libncurses5-dev \
    libpcre3-dev \
    libreadline-dev \
    libssl-dev \
    curl \
    zip \
    unzip \
    zlib1g-dev

# Install HOMER
RUN mkdir /opt/homer
RUN curl -fsSL http://homer.ucsd.edu/homer/configureHomer.pl -o /opt/homer/configureHomer.pl
RUN perl /opt/homer/configureHomer.pl -install

# Install MEME
RUN curl -fsSL meme-suite.org/meme-software/4.12.0/meme_4.12.0.tar.gz -o /opt/meme_4.12.0.tar.gz
RUN cd /opt/ && tar -xzf /opt/meme_4.12.0.tar.gz
RUN cd /opt/meme_4.12.0; ./configure --prefix=/opt/meme --enable-build-libxml2 --enable-build-libxslt; \
make; make install

COPY assets/JASPAR2018_CORE_vertebrates_nr_pfms.homer /
COPY assets/JASPAR2018_CORE_vertebrates_nr_pfms.jaspar /
COPY assets/merged_concat_tfs/* /merged_concat_tfs_encode/

ENV PATH $PATH:/opt/homer/bin:/opt/meme/bin