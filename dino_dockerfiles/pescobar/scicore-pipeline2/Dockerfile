FROM centos:7.3.1611
MAINTAINER Pablo Escobar <pablo.escobarlopez@unibas.ch>

ENV BOWTIE2_VERSION=2.2.9
ENV SAMTOOLS_VERSION=1.3.1
ENV FREEBAYES_VERSION=1.1.0
ENV VCFTOOLS_VERSION=0.1.14
ENV SEQTK_VERSION=1.2
ENV SRA_TOOLKIT_VERSION=2.8.1-3

# install the build dependencies
RUN yum makecache fast && \
    yum -y install epel-release && \
    yum -y install \
    unzip \
    wget \
    make \
    gcc \
    gcc-c++ \
    zlib-devel \
    bzip2-devel \
    ncurses-devel \
    bzip2 \
    git \
    cmake \
 && yum clean all

# Download Bowtie2 binaries and copy them so /usr/local/bin
WORKDIR /usr/local/src
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/${BOWTIE2_VERSION}/bowtie2-${BOWTIE2_VERSION}-linux-x86_64.zip && \
    unzip bowtie2-${BOWTIE2_VERSION}-linux-x86_64.zip && \
    cp bowtie2-${BOWTIE2_VERSION}/bowtie2* /usr/local/bin/

# Download and compile samtools
WORKDIR /usr/local/src
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
    tar xf samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
    cd /usr/local/src/samtools-${SAMTOOLS_VERSION} && \
    ./configure && \
    make && \
    make install

# Download freebayes source code
# the release system for freebayes does git --recursive which makes hard to reproduce the same installation
# To workaround it I do some git checkout to use the same source code installed in the scicore cluster
# 39e5e4b is the git commit for freebayes release 1.1.0
WORKDIR /usr/local/src
RUN git clone --recursive git://github.com/ekg/freebayes.git && \
   cd /usr/local/src/freebayes/ && git checkout 39e5e4b && \ 
   cd /usr/local/src/freebayes/SeqLib && git checkout cce1e410ef6d2ac64972f5cacd8a0f9b86cecdd8 && \
   cd /usr/local/src/freebayes/SeqLib/bwa && git checkout fbd4dbc03904eccd71cdca8cac7aa48da749c19c && \
   cd /usr/local/src/freebayes/SeqLib/htslib && git checkout 0f298ce22c5c825c506129bf242348a31630c382 && \
   cd /usr/local/src/freebayes/SeqLib/fermi-lite && git checkout 5bc90f8d70e2b66184eccbd223a3be714c914365 && \
   cd /usr/local/src/freebayes/bamtools && git checkout e77a43f5097ea7eee432ee765049c6b246d49baa && \
   cd /usr/local/src/freebayes/intervaltree && git checkout dbb4c513d1ad3baac516fc1484c995daf9b42838 && \
   cd /usr/local/src/freebayes/vcflib && git checkout 5e3ce04f758c6df16bc4d242b18a24d725d2e6e5 && \
   cd /usr/local/src/freebayes/vcflib/fsom && git checkout a6ef318fbd347c53189384aef7f670c0e6ce89a3 && \
   cd /usr/local/src/freebayes/vcflib/intervaltree && git checkout b704f195e9b51d44dad68e33c209b06e63ebb353 && \
   cd /usr/local/src/freebayes/vcflib/smithwaterman && git checkout 84c08d7eae7211d87fbcb1871dae20e6c2041e96 && \
   cd /usr/local/src/freebayes/vcflib/fastahack && git checkout c68cebb4f2e5d5d2b70cf08fbdf1944e9ab2c2dd && \
   cd /usr/local/src/freebayes/vcflib/filevercmp && git checkout 1a9b779b93d0b244040274794d402106907b71b7 && \
   cd /usr/local/src/freebayes/vcflib/tabixpp/htslib/ && git checkout 0f298ce22c5c825c506129bf242348a31630c382 && \
   cd /usr/local/src/freebayes/vcflib/tabixpp && git checkout 80012f86dc22b13c75b73baf38195956db92473e && \
   cd /usr/local/src/freebayes/vcflib/multichoose && git checkout 73d35daa18bf35729b9ba758041a9247a72484a5 && \
   cd /usr/local/src/freebayes/vcflib/googletest/ && git checkout d225acc90bc3a8c420a9bcd1f033033c1ccd7fe0 

# compile and install freebayes
WORKDIR /usr/local/src/freebayes/
RUN make && \
    make install

# Install vcftools
WORKDIR /usr/local/src
RUN wget https://github.com/vcftools/vcftools/releases/download/v${VCFTOOLS_VERSION}/vcftools-${VCFTOOLS_VERSION}.tar.gz && \
    tar xf vcftools-${VCFTOOLS_VERSION}.tar.gz && \
    cd vcftools-${VCFTOOLS_VERSION} && \
    ./configure && \
    make && \
    make install

# Install seqtk
WORKDIR /usr/local/src
RUN wget https://github.com/lh3/seqtk/archive/v${SEQTK_VERSION}.tar.gz && \
   tar xf v${SEQTK_VERSION}.tar.gz && \
   cd /usr/local/src/seqtk-${SEQTK_VERSION}/ && \
   make && \
   cp /usr/local/src/seqtk-${SEQTK_VERSION}/seqtk /usr/local/bin/

# Install SRA-Toolkit
WORKDIR /usr/local/src
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/${SRA_TOOLKIT_VERSION}/sratoolkit.${SRA_TOOLKIT_VERSION}-centos_linux64.tar.gz && \
   tar xf sratoolkit.${SRA_TOOLKIT_VERSION}-centos_linux64.tar.gz && \
   cp -ra /usr/local/src/sratoolkit.${SRA_TOOLKIT_VERSION}-centos_linux64/bin/* /usr/local/bin/ && \
   rm -fr /usr/local/src/sratoolkit.${SRA_TOOLKIT_VERSION}-centos_linux64/

ENTRYPOINT ["echo", "-e", "This container includes the following apps:\\n\
    Bowtie2/2.2.9 - http://bowtie-bio.sourceforge.net/bowtie2/index.shtml\\n\
    SAMtools/1.3.1 - http://www.htslib.org/\\n\
    freebayes/1.1.0 - https://github.com/ekg/freebayes\\n\
    vcftools/0.1.14 - https://vcftools.github.io\\n\
    Optional tools only used to download the public data and downsample it:\\n\
    SRA-Toolkit/2.8.1-3-centos_linux64 - https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=std  \\n\
    Seqtk/1.2 - https://github.com/lh3/seqtk\\n\
    To execute a binary inside the container do \"singularity exec /path/to/container.img binary-name\""]

