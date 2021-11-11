# EricScript Plants Docker Image
#FROM ubuntu:14.04
FROM asherkhb/workqueue-docker:base

# Add R-Project to Apt-Get, Update Apt-Get
RUN sh -c 'echo "deb http://cloud.r-project.org/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list' \
    && gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \
    && gpg -a --export E084DAB9 | apt-key add - \
    && apt-get update

# Install basic tools:
RUN apt-get install -y \
    git \
    r-base \
    r-base-dev \
    wget \
    && R -e "install.packages('ada', repos='http://cloud.r-project.org/')"

# Install dependencies: samtools, BWA, bedtools, seqtk, blatSuite, SRA Toolkit
RUN apt-get install -y samtools \
    && cd /usr/src \
    && git clone http://github.com/lh3/bwa.git \
    && cd bwa && make && cd - \
    && wget https://github.com/arq5x/bedtools2/releases/download/v2.26.0/bedtools-2.26.0.tar.gz \
    && tar xvfz bedtools-2.26.0.tar.gz && rm bedtools-2.26.0.tar.gz && cd bedtools2/ && make install && cd - \
    && git clone https://github.com/lh3/seqtk.git \
    && cd seqtk && make && cd - \
    && mkdir blatSuite && cd blatSuite && wget http://genome-test.cse.ucsc.edu/~kent/exe/linux/blatSuite.zip \
    && unzip blatSuite.zip && rm blatSuite.zip && cd - \
    && wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.8.2-1/sratoolkit.2.8.2-1-ubuntu64.tar.gz \
    && tar xvfz sratoolkit*.tar.gz && rm sratoolkit*.tar.gz && mv sratoolkit* sratoolkit \
    && cd /usr/local/bin/ && ln -s /usr/src/bwa/bwa bwa && ln -s /usr/src/seqtk/seqtk seqtk \
    && cd

# Install EricScript-Plants
# Old Method
# RUN cd /usr/src/ && git clone https://github.com/asherkhb/EricScript-Plants.git \
#     && chmod +x EricScript-Plants/ericscript.pl \
#     && cd /usr/local/bin && sudo ln -s /usr/src/EricScript-Plants/ericscript.pl ericscript && cd
COPY EricScript-Plants/ /usr/src/EricScript-Plants
RUN chmod +x /usr/src/EricScript-Plants/ericscript.pl \
    && cd /usr/local/bin \ 
    && sudo ln -s /usr/src/EricScript-Plants/ericscript.pl ericscript \
    && cd

# Set path to include BLAT and SRA Toolkit
ENV PATH="${PATH}:/usr/src/blatSuite:/usr/src/sratoolkit/bin"

# Set Workdir - test w/ -v folder:/usr/local/data
WORKDIR /usr/local/data

# Set ENTRYPOINT and CMD (instructions)
ENTRYPOINT ["/bin/bash", "-c"]
# Old Method
# CMD ["echo 'Usage: docker run -v </my/data/folder>:/usr/local/data -d ericscript-plants:0.1 <quoted command>'"]
CMD ["bash"]