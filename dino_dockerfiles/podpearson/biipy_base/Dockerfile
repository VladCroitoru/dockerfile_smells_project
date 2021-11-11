FROM ubuntu:15.10
MAINTAINER Richard Pearson <rpearson@well.ox.ac.uk>

# install various libraries and software
RUN apt-get update && apt-get install -y \
    software-properties-common \
    build-essential \
    byobu \
    curl \
    git \
    htop \
    man \
    unzip \
    vim \
    wget \
    emacs24-nox \
    qt4-qtconfig \
    libqt4-core \
    libqt4-gui \
    libqt4-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libxft-dev \
    x11-apps \
    libncurses5-dev  \
    libncursesw5-dev \
    bzip2 \
    openjdk-7-jdk \
    openjdk-7-jre \
    maven
ENV DISPLAY :0

ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64

# install fonts
RUN apt-add-repository multiverse
RUN apt-get install -y \
    fonts-liberation \
    fonts-dejavu \
    ttf-ubuntu-font-family
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install ttf-mscorefonts-installer

# install R for RPY2
RUN apt-get update -y && apt-get install -y r-base r-base-dev

# install APE
RUN R -e 'install.packages("ape", repos="http://cran.us.r-project.org")'

# install BWA & SAMTOOLS
RUN cd /opt
RUN git clone https://github.com/lh3/bwa.git
RUN git clone --branch=develop git://github.com/samtools/htslib.git
RUN git clone --branch=develop git://github.com/samtools/bcftools.git
RUN git clone --branch=develop git://github.com/samtools/samtools.git
RUN cd bwa; make
RUN cd ../bcftools; make; make install
RUN cd ../samtools; make; make install

ENV PATH=$PATH:/opt

# PICARD
ENV ZIP=picard-tools-1.139.zip
ENV URL=https://github.com/broadinstitute/picard/releases/download/1.139/
ENV FOLDER=picard-tools-1.139
ENV DST=/opt/
RUN wget $URL/$ZIP -O $DST/$ZIP && \
    unzip $DST/$ZIP -d $DST && \
    rm $DST/$ZIP && \
    cd $DST/$FOLDER && \
    mv * .. && \
    cd / && \
    bash -c 'echo -e "#!/bin/bash\njava -jar '$DST'/picard.jar \$@" > '$DST'/picard' && \
    chmod +x $DST/picard && \
    rm -rf $DST/$FOLDER

# GATK
ENV FOLDER=gatk
RUN git clone https://github.com/broadgsa/gatk-protected.git $DST/$FOLDER && \
    cd $DST/$FOLDER && \
    sed -i 's/import oracle.jrockit.jfr.StringConstantPool/\/\/import oracle.jrockit.jfr.StringConstantPool/g' ./public/gatk-tools-public/src/main/java/org/broadinstitute/gatk/tools/walkers/varianteval/VariantEval.java && \
    mvn verify -P\!queue && \
    bash -c 'echo -e "#!/bin/bash\njava -jar '$DST/$FOLDER'/target/GenomeAnalysisTK.jar  \$@" > '$DST'/GenomeAnalysisTK' && \
    chmod +x $DST/GenomeAnalysisTK
ENV PATH=/usr/lib/jvm/java-7-openjdk-amd64/bin:$PATH


# HDF5
RUN apt-get install -y libhdf5-dev libhdf5-serial-dev

# PYTHON 3.5
RUN apt-get install -y python3.5-dev libpython3.5-dev
RUN apt-get install -y libpq-dev python3-pyqt5 python3-pyqt4 python3-pip
RUN python3.5 -m pip install -U pip setuptools wheel

# DEPENDENCIES FOR ETE3
ENV LICENSE accept
RUN curl -L -O http://downloads.sourceforge.net/project/pyqt/sip/sip-4.16.9/sip-4.16.9.tar.gz
RUN tar -xvzf sip-4.16.9.tar.gz
RUN cd sip-4.16.9 && python3.5 configure.py && make && make install
RUN curl -L -O http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt-x11-gpl-4.11.4.tar.gz
RUN tar -xvzf PyQt-x11-gpl-4.11.4.tar.gz

CMD ["/bin/bash"]
