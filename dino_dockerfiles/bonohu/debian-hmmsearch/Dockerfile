#Docker container for hmmsearch

FROM debian
MAINTAINER Hidemasa Bono, bonohu@gmail.com

# File add
ADD Sod_Cu.hmm Sod_Cu.hmm

# Install packages
RUN apt-get update && \
    apt-get install -y hmmer &&\
    apt-get install -y wget &&\
    rm -rf /var/lib/apt/lists/*
RUN wget ftp://ftp.ensemblgenomes.org/pub/metazoa/release-25/fasta/bombyx_mori/pep/Bombyx_mori.GCA_000151625.1.25.pep.all.fa.gz
CMD ["hmmsearch", "Sod_Cu.hmm", "Bombyx_mori.GCA_000151625.1.25.pep.all.fa.gz"]
