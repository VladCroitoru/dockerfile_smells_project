# Standalone antiSMASH build without databases
# VERSION 3.0.4.1

FROM debian:jessie
MAINTAINER cheng gong <1461744165@qq.com>

ENV ANTISMASH_URL="https://bitbucket.org/antismash/antismash/downloads"
ENV ANTISMASH_VERSION="3.0.4"

# set up antiSMASH deb repo
ADD http://dl.secondarymetabolites.org/antismash.list /etc/apt/sources.list.d/antismash.list
ADD http://dl.secondarymetabolites.org/antismash.asc /tmp/
RUN apt-key add /tmp/antismash.asc

# grab all the dependencies
RUN apt-get update && apt-get install -y ncbi-blast+ glimmerhmm tigr-glimmer diamond hmmer2 hmmer hmmer2-compat muscle prodigal fasttree default-jre-headless python-straight.plugin python-pysvg python-helperlibs python-biopython python-pyquery python-backports.lzma python-matplotlib

# Grab antiSMASH
ADD ${ANTISMASH_URL}/antismash-${ANTISMASH_VERSION}.tar.gz /tmp/
# copy antiSMASH tarball form local to image
#copy antismash-${ANTISMASH_VERSION}.tar.gz /tmp/antismash-${ANTISMASH_VERSION}.tar.gz
RUN tar zxvf /tmp/antismash-${ANTISMASH_VERSION}.tar.gz && rm -f /tmp/antismash-${ANTISMASH_VERSION}.tar.gz

ADD instance.cfg /antismash-${ANTISMASH_VERSION}/antismash/config/instance.cfg

# compress the shipped profiles
WORKDIR /antismash-${ANTISMASH_VERSION}/antismash/specific_modules/nrpspks
VOLUME ["/usr/bin/"]
RUN hmmpress abmotifs.hmm && hmmpress dockingdomains.hmm && hmmpress ksdomains.hmm && hmmpress nrpspksdomains.hmm
WORKDIR /antismash-${ANTISMASH_VERSION}/antismash/generic_modules/smcogs/
RUN hmmpress smcogs.hmm

WORKDIR /usr/local/bin
RUN ln -s /antismash-${ANTISMASH_VERSION}/run_antismash.py

VOLUME ["/input", "/output", "/databases", "/share"]
WORKDIR /

ENTRYPOINT ["/bin/bash"]
