FROM ubuntu
MAINTAINER Simon Johansson <simon@simonjohansson.com>

# DEPS
RUN apt-get update && apt-get install  -y \
  wget=1.15-1ubuntu1.14.04.1 \
  build-essential=11.6ubuntu6 \
  m4=1.4.17-2ubuntu1 

# ENV
ENV SCHEME_VERSION mit-scheme-9.2
ENV SCHEME_TAR ${SCHEME_VERSION}-x86-64.tar.gz

# GET
WORKDIR /tmp
RUN wget http://ftp.gnu.org/gnu/mit-scheme/stable.pkg/9.2/${SCHEME_TAR}
RUN wget http://ftp.gnu.org/gnu/mit-scheme/stable.pkg/9.2/md5sums.txt
RUN cat md5sums.txt | awk '/${SCHEME_TAR}/ {print}' | tee md5sums.txt
RUN tar xf ${SCHEME_TAR} 

# BUILD
WORKDIR /tmp/${SCHEME_VERSION}/src
RUN cd /tmp/${SCHEME_VERSION}/src
RUN ./configure && make && make install

# CLEAN
WORKDIR /tmp/
RUN rm -rf ${SCHEME_VERSION} ${SCHEME_TAR} md5sums.txt
RUN apt-get remove -y wget build-essential m4
RUN apt-get -y autoremove

# WORKENV
VOLUME ["/work"]
WORKDIR /work
