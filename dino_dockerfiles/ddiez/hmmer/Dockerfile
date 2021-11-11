FROM debian:testing
LABEL maintainer Diego Diez <diego10ruiz@gmail.com>

ENV VERSION=3.2.1

## Install HMMER.
#  1. Get dependencies.
#  2. Download HMMER source.
#  3. Unpack, compile and install.
#  4. Cleanup source and dependencies.
RUN apt-get update && \
    apt-get install -y gcc make curl && \
    # build.
    curl http://eddylab.org/software/hmmer/hmmer-$VERSION.tar.gz > /tmp/hmmer-$VERSION.tar.gz && \
    cd /tmp && tar zxvf hmmer-$VERSION.tar.gz && \
    cd /tmp/hmmer-$VERSION && \
    ./configure --prefix /opt && \
    make && \
    make install && \
    # clean up.
    cd /tmp && \
    rm -rf /tmp/hmmer-$VERSION && \
    rm hmmer-$VERSION.tar.gz && \
    apt-get clean -y && \
    apt-get purge -y gcc make curl && \
    apt-get autoremove -y

## Set up environment.
# Add /opt/bin to PATH.
ENV PATH /opt/bin:$PATH

# Set user.
RUN useradd -ms /bin/bash biodev
RUN echo 'biodev:biodev' | chpasswd
USER biodev
WORKDIR /home/biodev

CMD ["/bin/bash"]
