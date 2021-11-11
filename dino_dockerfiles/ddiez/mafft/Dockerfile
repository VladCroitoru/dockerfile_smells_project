FROM debian:testing
MAINTAINER Diego Diez <diego10ruiz@gmail.com>

ENV VERSION=7.407

## Install MAFFT.
RUN apt-get update && \
    apt-get install -y build-essential curl && \
    curl https://mafft.cbrc.jp/alignment/software/mafft-$VERSION-with-extensions-src.tgz > /tmp/mafft-$VERSION-with-extensions-src.tgz && \
    cd /tmp && tar zxvf mafft-$VERSION-with-extensions-src.tgz && \
    cd /tmp/mafft-$VERSION-with-extensions/core && \
    sed -e "s/^PREFIX = \/usr\/local/PREFIX = \/opt/" Makefile > Makefile.tmp && \
    mv Makefile.tmp Makefile && \
    make clean && make && make install && \
    cd /tmp && rm -rf mafft-$VERSION-with-extensions && \
    apt-get purge -y build-essential curl && \
    apt-get autoremove -y

## Set up environment.
# Add /opt/bin to PATH.
ENV PATH /opt/bin:$PATH

# Set user.
RUN useradd -ms /bin/bash biodev
RUN echo 'biodev:biodev' | chpasswd
USER biodev
WORKDIR /home/biodev
