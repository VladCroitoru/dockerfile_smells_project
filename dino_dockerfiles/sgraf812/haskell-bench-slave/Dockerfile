FROM ubuntu:16.04
MAINTAINER Sebastian Graf <sgraf1337@gmail.com>

#
# Mostly stolen from https://github.com/AlexeyRaga/ghc-docker-dev/blob/master/Dockerfile,
# refined with auxiliary tools like stack, cloben and feed-gipeda
#

## disable prompts from apt
ENV DEBIAN_FRONTEND noninteractive

## custom apt-get install options
ENV OPTS_APT        -y  --no-install-recommends

## hvr's custom GHCs <3
RUN apt-get update && apt-get install ${OPTS_APT} software-properties-common
RUN add-apt-repository -y ppa:hvr/ghc

## stack <3
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 575159689BEFB442
RUN echo 'deb http://download.fpcomplete.com/ubuntu xenial main' | tee /etc/apt/sources.list.d/fpco.list

## Download all dependencies necessary for a successful GHC build
RUN apt-get update \
 && apt-get install ${OPTS_APT} \
            wget bzip2 xz-utils git libtool \
            patch less autoconf automake make \
            llvm libgmp-dev g++ python ncurses-dev \
            ghc-8.0.1 cabal-install-1.24 stack \
            time ohcount libfile-slurp-perl libipc-run-perl \
            vim-tiny \
 && apt-get clean

# Locale stuff which does all kinds of things
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

RUN useradd -m -d /home/bench -s /bin/bash bench
# No idea what this is doing, but looks dangerous
# RUN echo "ghc ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/ghc && chmod 0440 /etc/sudoers.d/ghc
USER bench
ENV HOME /home/bench
WORKDIR ${HOME}

# GHC benchmark script until it's in master
ADD benchmark.sh ${HOME}/benchmark.sh
ADD log2csv ${HOME}/log2csv
RUN chmod 755 ${HOME}/benchmark.sh ${HOME}/log2csv

# PATH for stack builds, cabal builds, apt-get ghc and apt-get cabal
ENV PATH ${HOME}/.local/bin:${HOME}/.cabal/bin:/opt/ghc/8.0.1/bin:/opt/cabal/1.24/bin:${PATH}

RUN cabal update \
 && cabal install -j alex happy \
 && cabal install -j html regex-compat # for GHC benchmarks

RUN stack setup # leaving setup separate for now, because it currently takes really long
RUN stack install cloben --install-ghc

# feed-gipeda isn't yet on stackage, we'll have to compile from source for the time being
RUN git clone https://github.com/sgraf812/feed-gipeda
WORKDIR ${HOME}/feed-gipeda

RUN stack install --install-ghc

WORKDIR ${HOME}
RUN rm -rf feed-gipeda .stack-work
