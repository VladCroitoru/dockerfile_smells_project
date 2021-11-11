FROM r-base:3.4.0

# Installation of SamTools

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        bzip2 \
        curl \
        zlib1g-dev \
        libncurses5-dev 

ENV SAMTOOLS_VERSION 1.4.1

WORKDIR /root
RUN mkdir samtools \
    && curl -fsSL https://github.com/samtools/samtools/releases/download/$SAMTOOLS_VERSION/samtools-$SAMTOOLS_VERSION.tar.bz2 \
        | tar -jxC samtools --strip-components=1

WORKDIR /root/samtools
RUN ./configure \
    && make all all-htslib \
    && make install install-htslib
    
WORKDIR /

RUN cd 

RUN wget ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.0.5-Linux_x86_64.zip
RUN unzip hisat2-2.0.5-Linux_x86_64.zip

RUN cp hisat2-2.0.5/hisat2* hisat2-2.0.5/*.py /bin



RUN wget http://ccb.jhu.edu/software/stringtie/dl/stringtie-1.3.3b.Linux_x86_64.tar.gz

RUN  tar xvzf stringtie-1.3.3b.Linux_x86_64.tar.gz

RUN  cp stringtie-1.3.3b.Linux_x86_64/stringtie /bin

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("ballgown" );'

RUN Rscript -e 'install.packages("devtools")'

RUN Rscript -e 'devtools::install_github("alyssafrazee/RSkittleBrewer")'

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("genefilter" );'

RUN Rscript -e 'install.packages("dplyr")'

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("DESeq2" );'

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("tweeDEseq" );'

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("EventPointer");'





# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["samtools"]

