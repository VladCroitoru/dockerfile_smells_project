FROM phusion/baseimage

WORKDIR /root

RUN apt-get clean && apt-get update

# Install wget and build tools
RUN apt-get install -y wget build-essential

# Install `multilib` for 32-bit support that SML/NJ requires.
RUN apt-get install -y gcc-multilib g++-multilib

# rlwrap improves the experience inside the REPL
RUN apt-get install rlwrap

# Get the source
RUN wget http://smlnj.cs.uchicago.edu/dist/working/110.78/config.tgz

# Extract the source
RUN gunzip <config.tgz | tar xf -

# Modify the configured targets, in order to build the heap2adm program
RUN sed -i /root/config/targets -e "s/\#request heap2asm/request heap2asm/g"

# Compile
RUN config/install.sh

# Modify heap2exec to build 32 bit binaries, as it needs to link against the
# supplied 32 bit SML runtime
RUN sed -i /root/bin/heap2exec -e "s/CC=cc/CC=\"cc -m32\"/g"

# Add SML binaries to path
ENV PATH /root/bin:$PATH

# Set the entrypoint to the SML compiler/REPL
ENTRYPOINT /root/bin/sml
