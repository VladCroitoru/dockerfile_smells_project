FROM centos:7

MAINTAINER Donald Simpson <donaldsimspon@gmail.com>

# YUM update, install & clean
RUN yum update -y && yum groupinstall -y "Development Tools" && yum clean all

# Add primesum
RUN mkdir /primesum
ADD https://dl.bintray.com/kimwalisch/primesum/primesum-1.0.tar.gz /primesum

# Unpack, build, check & install
RUN cd /primesum \
    && tar zxvf primesum-1.0.tar.gz \
    && /bin/rm /primesum/primesum-1.0.tar.gz \
    && cd /primesum/primesum-1.0 \
    && ./build.sh \
    && make check \
    && make install 

# Add Tini
ENV TINI_VERSION v0.10.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Run primesum under Tini
# These args can be overridden at run time
CMD ["primesum", "1e14", "--threads=4", "--time"]
