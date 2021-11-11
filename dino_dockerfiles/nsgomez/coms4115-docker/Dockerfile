FROM debian:stretch
MAINTAINER Nelson Gomez <nelson.gomez@columbia.edu>

# Make sure container is up-to-date
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/backports.list
RUN apt-get update
RUN apt-get -y upgrade

# Install dependencies for MicroC
RUN apt-get -y install ocaml m4 cmake pkg-config git opam
RUN apt-get -t stretch-backports -y install llvm-5.0-dev
RUN apt-get -y install llvm-5.0 llvm-5.0-runtime

# Use a separate user for OPAM. OPAM complains if it's run as root,
# and probably for good reason.
RUN useradd -m opam -s /bin/bash
USER opam

# Initialize OPAM
RUN opam init
RUN eval `opam config env`
RUN echo '. ~/.opam/opam-init/init.sh > /dev/null 2> /dev/null || true' >> $HOME/.bashrc
COPY .ocamlinit $HOME/.ocamlinit

# Set up basic compiler build dependencies
RUN opam install llvm.5.0.0

# Set up test coverage
RUN opam install bisect_ppx ocveralls
USER root
RUN apt-get -y install curl
USER opam
