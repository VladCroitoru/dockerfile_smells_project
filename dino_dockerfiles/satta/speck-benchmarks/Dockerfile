FROM debian:jessie

MAINTAINER ss34@sanger.ac.uk

RUN apt-get update -yy
RUN apt-get install build-essential bioperl python3-biopython curl wget unzip --yes --force-yes

ADD https://bootstrap.pypa.io/get-pip.py /tmp/get_pip.py
RUN chmod +x /tmp/get_pip.py && python /tmp/get_pip.py
RUN pip install gffutils

ADD https://github.com/genometools/genometools/archive/master.zip /opt/genometools-master.zip
RUN cd /opt && \
    unzip genometools-master.zip && \
    cd /opt/genometools-master && \
    make amalgamation=yes -j3 cairo=no curses=no && \
    make amalgamation=yes -j3 cairo=no curses=no install && \
    cd / && \
    rm -rf /opt/genometools-master*

RUN mkdir -p /opt/genomes && \
    cd /opt/genomes && \
    wget -r -nv -nd -np -A "*.noseq.gff3.gz" ftp://ftp.sanger.ac.uk/pub/project/pathogens/gff3/CURRENT/ && \
    wget -r -nv -nd -np -A "*.genome.fasta.gz" ftp://ftp.sanger.ac.uk/pub/project/pathogens/gff3/CURRENT/ && \
    gunzip *genome.fasta.gz

RUN cd /opt/genomes && \
    find . -name '*.genome.fasta' -exec gt encseq encode -showstats {} \;

RUN cd /opt && \
    curl http://www.sequenceontology.org/software/GAL_Code/GAL_0.2.2.tar.gz | tar xzv
RUN cd /opt/GAL_0.2.2 && \
    perl Build.PL && \
    ./Build installdeps && \
    ./Build install

RUN apt-get install time --yes --force-yes

ADD . /opt/scripts

ENV GT_RETAINIDS yes
ENV PERL5LIB /opt/GAL_0.2.2/lib:$PERL5LIB
