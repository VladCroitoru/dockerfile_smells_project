FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
       wget \
       g++ \
       build-essential \
       file \
       unzip \
       libncurses5-dev \
       zlib1g-dev \
       libbz2-dev \
       liblzma-dev \
       libtbb-dev \
       git \
       libipc-run-perl \
       python \
       openjdk-8-jre-headless \
       bc && \
    rm -rf /var/lib/apt/lists/*

ENV reperDir /reper
ENV depDir /dependencies

WORKDIR $reperDir
COPY reper .
COPY reper.conf .
COPY update_exe_path.sh .
COPY scripts/ ./scripts/
ENV PATH="$reperDir":$PATH

WORKDIR $depDir
RUN wget https://github.com/gmarcais/Jellyfish/releases/download/v2.2.6/jellyfish-2.2.6.tar.gz && \
    tar xzf jellyfish-2.2.6.tar.gz && \
    cd jellyfish-2.2.6 && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf jellyfish-2.2.6 jellyfish-2.2.6.tar.gz
ENV LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH

RUN wget https://github.com/BenLangmead/bowtie2/releases/download/v2.3.2/bowtie2-2.3.2-linux-x86_64.zip && \
    unzip bowtie2-2.3.2-linux-x86_64.zip && \
    rm bowtie2-2.3.2-linux-x86_64.zip

ENV PATH="$depDir"/bowtie2-2.3.2:"$PATH"

RUN wget https://github.com/weizhongli/cdhit/releases/download/V4.6.7/cd-hit-v4.6.7-2017-0501-Linux-binary.tar.gz && \
    tar xzf cd-hit-v4.6.7-2017-0501-Linux-binary.tar.gz && \
    cd cd-hit-v4.6.7-2017-0501 && \
    make install && \
    cd .. && \
    rm -rf cd-hit-v4.6.7-2017-0501 cd-hit-v4.6.7-2017-0501-Linux-binary.tar.gz

RUN wget https://github.com/samtools/samtools/releases/download/1.4.1/samtools-1.4.1.tar.bz2 && \
    tar xjf samtools-1.4.1.tar.bz2 && \
    cd samtools-1.4.1 && \
    ./configure && \
    make && \
    make check && \
    make install && \
    cd .. && \
    rm -rf samtools-1.4.1 samtools-1.4.1.tar.bz2

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.28/ncbi-blast-2.2.28+-x64-linux.tar.gz && \
    tar xzf ncbi-blast-2.2.28+-x64-linux.tar.gz && \
    rm ncbi-blast-2.2.28+-x64-linux.tar.gz

ENV PATH="$depDir"/ncbi-blast-2.2.28+/bin:"$PATH"

RUN wget https://github.com/trinityrnaseq/trinityrnaseq/archive/Trinity-v2.4.0.tar.gz && \
    tar xzf Trinity-v2.4.0.tar.gz && \
    cd trinityrnaseq-Trinity-v2.4.0 && \
    make && \
    make plugins && \
    cd .. && \
    rm Trinity-v2.4.0.tar.gz

ENV TRINITY_HOME="$depDir"/trinityrnaseq-Trinity-v2.4.0
ENV PATH="$TRINITY_HOME":"$PATH"

RUN git clone https://github.com/thackl/kmer-scripts.git
ENV PATH="$depDir"/kmer-scripts/bin/:"$PATH"

WORKDIR $depDir/lib
ENV PERL5LIB="$depDir/lib:$PERL5LIB"

RUN wget http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/Log-Log4perl-1.49.tar.gz && \
    tar xzf Log-Log4perl-1.49.tar.gz && \
    cd Log-Log4perl-1.49 && \
    perl Makefile.PL && \
    make && \
    make test && \
    make install && \
    cd .. && \
    rm -rf Log-Log4perl-1.49 Log-Log4perl-1.49.tar.gz

RUN wget http://search.cpan.org/CPAN/authors/id/P/PL/PLICEASE/File-Which-1.22.tar.gz && \
    tar xzf File-Which-1.22.tar.gz && \
    cd File-Which-1.22 && \
    perl Makefile.PL && \
    make && \
    make test && \
    make install && \
    cd .. && \
    rm -rf File-Which-1.22.tar.gz File-Which-1.22

RUN for i in \
    https://github.com/BioInf-Wuerzburg/perl5lib-Fastq.git \
    https://github.com/BioInf-Wuerzburg/perl5lib-Fasta.git \
    https://github.com/thackl/perl5lib-Jellyfish.git \
    https://github.com/thackl/perl5lib-Kmer.git \
    https://github.com/BioInf-Wuerzburg/perl5lib-Verbose.git \
    https://github.com/thackl/perl5lib-Sam.git; \
    do \
       git clone ${i} gitclone && \
       mv gitclone/lib/* . && \
       rm -rf gitclone; \
    done

# update the path in reper.conf
RUN /reper/update_exe_path.sh /reper/reper.conf

WORKDIR /data

RUN chmod -R a+rwX $reperDir

ENTRYPOINT ["reper"]
