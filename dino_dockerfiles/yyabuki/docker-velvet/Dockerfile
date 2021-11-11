FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
# a bit modified Michael Barton's Dockerfile, Procfile and run files.

ENV PACKAGES make gcc g++ python r-base-core wget libc6-dev zlib1g-dev
RUN apt-get update -y && apt-get install -y --no-install-recommends ${PACKAGES}

ENV ASSEMBLER_DIR /tmp/assembler
ENV ASSEMBLER_URL https://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz
ENV ASSEMBLER_BLD make 'MAXKMERLENGTH=100' && mv velvet* /usr/local/bin/ && rm -r ${ASSEMBLER_DIR}

ENV KMER_GENIE_DIR /tmp/kmergenie
ENV KMER_GENIE_URL http://kmergenie.bx.psu.edu/kmergenie-1.6741.tar.gz
ENV KMER_GENIE_BLD make && make install

RUN mkdir ${ASSEMBLER_DIR}
RUN cd ${ASSEMBLER_DIR} &&\
    wget --no-check-certificate ${ASSEMBLER_URL} --output-document - |\
    tar xzf - --directory . --strip-components=1 && eval ${ASSEMBLER_BLD}


RUN mkdir ${KMER_GENIE_DIR}
RUN cd ${KMER_GENIE_DIR} && \
    wget --no-check-certificate ${KMER_GENIE_URL} --output-document - |\
    tar xzf - --directory . --strip-components=1 && eval ${KMER_GENIE_BLD}

ADD run /usr/local/bin/
ADD adaptive /usr/local/bin/
ADD Procfile /

ENTRYPOINT ["run"]
