# Dockerfile for docker-skink

FROM ubuntu:bionic

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    git \
    graphviz \
    locales \
    mercurial \
    python-pip \
    python3-pip \
    software-properties-common \
    subversion \
    wget \
    unzip

# Locale setup, needed for perl

RUN locale-gen en_US.UTF-8

# Install java

RUN apt-get update && apt-get install -y \
   openjdk-8-jdk

# Install sbt
# http://www.scala-sbt.org/1.x/docs/Installing-sbt-on-Linux.html

RUN echo 'deb https://dl.bintray.com/sbt/debian /' >> /etc/apt/sources.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \
    apt-get update && apt-get install -y \
       sbt

# Install clang

RUN cd /usr/src && \
    wget -q http://releases.llvm.org/7.0.0/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz && \
    tar xvJf clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz && \
    ln -s /usr/src/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04/bin/clang /usr/local/bin/clang && \
    ln -s /usr/src/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04/bin/opt /usr/local/bin/opt

# Install z3, latest and 4.5.0

RUN cd /usr/src && \
    wget -q https://github.com/Z3Prover/z3/releases/download/Z3-4.8.5/z3-4.8.5-x64-ubuntu-16.04.zip && \
    unzip z3-4.8.5-x64-ubuntu-16.04.zip && \
    mv z3-4.8.5-x64-ubuntu-16.04/bin/z3 /usr/local/bin/z3

RUN cd /usr/src && \
    wget -q https://github.com/Z3Prover/z3/releases/download/z3-4.5.0/z3-4.5.0-x64-ubuntu-14.04.zip && \
    unzip z3-4.5.0-x64-ubuntu-14.04.zip && \
    mv z3-4.5.0-x64-ubuntu-14.04/bin/z3 /usr/local/bin/z3-4.5.0

# Install Yices

RUN add-apt-repository -y ppa:sri-csl/formal-methods && \
    apt-get install -y yices2

# Install Mathsat

RUN cd /usr/src && \
    wget -q 'http://mathsat.fbk.eu/download.php?file=mathsat-5.5.4-linux-x86_64.tar.gz' -O mathsat-5.5.4-linux-x86_64.tar.gz && \
    tar zxvf mathsat-5.5.4-linux-x86_64.tar.gz && \
    mv mathsat-5.5.4-linux-x86_64/bin/mathsat /usr/local/bin/mathsat

# Install CVC4

RUN cd /usr/local/bin && \
    wget https://github.com/CVC4/CVC4/releases/download/1.7/cvc4-1.7-x86_64-linux-opt -O cvc4-1.7-x86_64-linux-opt && \
    chmod +x cvc4-1.7-x86_64-linux-opt && \
    ln -s cvc4-1.7-x86_64-linux-opt cvc4

# Install Boolector
# Uses HEAD of master since we need the "echo" flush fix that was added after 3.0.0 release

RUN cd /usr/src && \
    apt-get install -y cmake && \
    git clone https://github.com/boolector/boolector && \
    cd boolector && \
    ./contrib/setup-lingeling.sh && \
    ./contrib/setup-btor2tools.sh && \
    ./configure.sh && \
    cd build && \
    make && \
    ln -s /usr/src/boolector/build/bin/boolector /usr/local/bin/boolector

# Install benchexec, including sources to get mergeBenchmarkSets.py

RUN cd /usr/src && \
    wget -q 'https://github.com/sosy-lab/benchexec/releases/download/1.19/benchexec_1.19-1_all.deb' -O benchexec_1.19-1_all.deb && \
    apt install -y --install-recommends ./benchexec_1.19-1_all.deb && \
    wget -q 'https://github.com/sosy-lab/benchexec/releases/download/1.19/BenchExec-1.19.tar.gz' -O BenchExec-1.19.tar.gz && \
    tar zxvf BenchExec-1.19.tar.gz && \
    ln -s BenchExec-1.19 benchexec

# Install SV-COMP configuration
# Link to / so /sv-comp paths in bench script work

RUN cd /usr/src && \
    wget -q 'https://github.com/sosy-lab/sv-comp/archive/svcomp19.tar.gz' -O svcomp19.tar.gz && \
    tar zxvf svcomp19.tar.gz && \
    ln -s /usr/src/sv-comp-svcomp19 /sv-comp

# For cutting-edge version, use this instead:
# RUN cd /usr/src && \
#     git clone --depth 1 https://github.com/sosy-lab/sv-comp.git && \
#     ln -s /usr/src/sv-comp /sv-comp

# Install sv-benchmarks for SV-COMP and cutting-edge version
# Link to / so /sv-benchmarks paths in SV-COMP work

RUN cd /usr/src && \
      git clone --branch svcomp19 --depth 1 https://github.com/sosy-lab/sv-benchmarks.git && \
      ln -s /usr/src/sv-benchmarks /sv-benchmarks

# For cutting-edge version, use this instead:
# RUN cd /usr/src && \
#     git clone --depth 1 https://github.com/sosy-lab/sv-benchmarks.git && \
#     ln -s /usr/src/sv-benchmarks /sv-benchmarks

# Install CPAchecker

RUN cd /usr/local/bin && \
    wget https://cpachecker.sosy-lab.org/CPAchecker-1.7-unix.tar.bz2 && \
    tar xvjf CPAchecker-1.7-unix.tar.bz2 && \
    ln -s CPAchecker-1.7-unix CPAchecker

# Install fshell-witness2test

RUN cd /usr/src && \
    apt-get install -y libc6-dev-i386 && \
    git clone https://github.com/tautschnig/fshell-w2t.git && \
    pip install pycparser && \
    cd fshell-w2t && \
    wget https://codeload.github.com/eliben/pycparser/zip/master -O pycparser-master.zip && \
    unzip pycparser-master.zip && \
    cp -rf /usr/src/fshell-w2t/* /usr/local/bin && \
    chmod +x /usr/local/bin/process_witness.py /usr/local/bin/test-gen.sh /usr/local/bin/TestEnvGenerator.pl

# Build, test and assemble a skink-like project so we preload dependencies

COPY skinklike /usr/src/skinklike
RUN cd /usr/src/skinklike && \
    sbt clean run assembly

# Setup skink-specific stuff
# When running locally for benchexec, Skink working dir will be mounted
# at /skink. Link Test.set to the sv-benchmarks so it can be run relative
# to there.

RUN mkdir /skink && \
    ln -s /skink/Test.set /usr/src/sv-benchmarks/c/Test.set
    # ln -s /skink/Test.set /usr/src/sv-benchmarks-svcomp18/c/Test.set

WORKDIR /skink
