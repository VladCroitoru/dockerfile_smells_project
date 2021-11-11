FROM simonalpha/ncbi-blast-docker

ENV BLASTDB /opt/blastdb

# check latest version from http://www.clustal.org/omega/
ARG CLUSTAL_VER=clustalo-1.2.4-Ubuntu-x86_64


RUN apt-get update && apt-get install -y --no-install-recommends wget ca-certificates \
    && apt-get clean \
    && rm /var/lib/dpkg/info/*

WORKDIR /opt/blastdb

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/16SMicrobial.tar.gz && tar xzvf 16SMicrobial.tar.gz && rm 16SMicrobial.tar.gz

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/swissprot.tar.gz && tar xzvf swissprot.tar.gz && rm swissprot.tar.gz

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/taxdb.tar.gz && tar xzvf taxdb.tar.gz && rm taxdb.tar.gz

RUN wget http://www.clustal.org/omega/${CLUSTAL_VER} \
    && chmod 755 ${CLUSTAL_VER} \
    && mv ${CLUSTAL_VER} /usr/bin/clustalo

WORKDIR /blast

RUN wget https://s3-us-west-2.amazonaws.com/veri-analizi/test.fa \
    && wget https://s3-us-west-2.amazonaws.com/veri-analizi/garfield.fa \
    && wget https://s3-us-west-2.amazonaws.com/veri-analizi/human_swissprot.fa \
    && wget https://s3-us-west-2.amazonaws.com/veri-analizi/ecoli_swissprot.fa \
    && wget https://s3-us-west-2.amazonaws.com/veri-analizi/Ecoli-cds.fa \
    && wget https://s3-us-west-2.amazonaws.com/veri-analizi/human_ensembl_transcripts.fa.gz \
    && wget https://s3-us-west-2.amazonaws.com/veri-analizi/human_ensembl_proteins.fa.gz \
    && wget https://s3-us-west-2.amazonaws.com/veri-analizi/all_human_viruses.fa \
    && wget https://s3-us-west-2.amazonaws.com/veri-analizi/human_ensembl_transcripts_50.fa
