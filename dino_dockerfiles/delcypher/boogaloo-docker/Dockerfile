FROM ubuntu:14.04
MAINTAINER Dan Liew <daniel.liew@imperial.ac.uk>

# Add PPA for Z3 4.3.1
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C504E590 && \
    echo 'deb http://ppa.launchpad.net/delcypher/boogaloo-smt/ubuntu trusty main' > /etc/apt/sources.list.d/smt.list && \
    apt-get update

# Setup Z3
RUN apt-get -y install z3=4.3.1-0~trusty1

# Mercurial and a proper text editor
RUN apt-get -y --no-install-recommends install mercurial ca-certificates vim

# FIXME: This pulls in lots of depdencies, not sure we need them all
RUN apt-get -y install cabal-install

RUN useradd -m boogaloo
USER boogaloo
WORKDIR /home/boogaloo


# Build haskell Z3 bindings
RUN hg clone https://bitbucket.org/wests/z3-haskell && \
    cd z3-haskell && \
    cabal update

# We need to patch this fork the Z3 bindings because
# it tries to use mtl-2.2.1 but that is in conflict with
# Boogaloo's dependencies
# FIXME: Z3's haskell bindings warn against using mtl-2.1
#        we should fix Boogaloo's dependencies instead
ADD hack_mtl_version.patch /home/boogaloo/z3-haskell/
RUN cd /home/boogaloo/z3-haskell/ && \
    hg update 223ff74eb1a33ef2e7af877bb463c443a73c500d && \
    hg import --no-commit hack_mtl_version.patch && \
    cabal install

# Build Boogaloo and patch it
#
RUN hg clone https://bitbucket.org/nadiapolikarpova/boogaloo && \
    cd boogaloo && \
    hg update 8077c1ad47cd73703a434e289a8adeba360b5233

# This patch is based on f8ac7985ff661278435c9cabc5ca5dce749c50bb
# but with the Z3 changes removed because they cause segfaults
ADD builtin_attribute_boogaloo.patch /home/boogaloo/boogaloo/

# This patch is straight from the boogaloo repo and it fixes a bug handling
# functions with nameless arguments
ADD c11cc364a7f60baa36bfb77a39733a7a3957a692.patch /home/boogaloo/boogaloo/

RUN cd boogaloo/ && \
    hg import --no-commit builtin_attribute_boogaloo.patch c11cc364a7f60baa36bfb77a39733a7a3957a692.patch && \
    cabal install

# Run Boogaloo tests
RUN cd boogaloo && \
    ghc Tests.hs && \
    ./Tests

# Put Boogaloo in PATH
RUN echo 'PATH=/home/boogaloo/.cabal/bin:$PATH' >> ~/.bashrc
