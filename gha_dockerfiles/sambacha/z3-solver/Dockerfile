FROM debian:buster AS solvers

ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

# Setup system
RUN apt-get update && apt-get install -y -qq --no-install-recommends \
      wget \
      unzip \
      curl \
      git \
      gcc g++ \
      make cmake autoconf gperf patch file \
      default-jre \
      python2.7-dev python-sympy \
      libgmp-dev libffi6 \
      libboost-program-options-dev libboost-iostreams-dev \
      libboost-test-dev libboost-thread-dev libboost-system-dev \
      libreadline-dev flex bison automake libtool \
      libedit-dev libreadline-dev

WORKDIR /downloads

# Install Z3 4.8.8
RUN wget --quiet https://github.com/Z3Prover/z3/releases/download/z3-4.8.8/z3-4.8.8-x64-ubuntu-16.04.zip
RUN unzip z3*.zip
RUN cp z3-*/bin/z3      /usr/local/bin/
RUN cp z3-*/bin/libz3.* /usr/local/lib/
RUN cp z3-*/include/*   /usr/local/include/

# Install CVC4 1.8
RUN wget --quiet https://github.com/CVC4/CVC4/releases/download/1.8/cvc4-1.8-x86_64-linux-opt
RUN chmod +x cvc4* && cp cvc4* /usr/local/bin && ln -s /usr/local/bin/cvc4-* /usr/local/bin/cvc4


# Build opensmt from GitHub (Latest version)
RUN git clone -b master https://github.com/usi-verification-and-security/opensmt.git
RUN cd opensmt && \
    mkdir build && \
    cd build && \
    cmake -DCMAKE_BUILD_TYPE=Release -DPRODUCE_PROOF=ON .. && \
    make && \
    make install

RUN useradd -m solvers && chown -R solvers:solvers /home/solvers
USER solvers
WORKDIR /home/solvers
