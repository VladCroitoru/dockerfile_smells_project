#
# SMT Solvers Dockerfile
#
# https://github.com/aggelgian/smt-solvers
#

# Select OS.
FROM debian:jessie

RUN apt-get update && apt-get install -y --no-install-recommends \
  wget unzip libgomp1 \
  && cd /opt \
  && wget --no-check-certificate https://github.com/Z3Prover/bin/raw/master/releases/z3-4.4.1-x64-debian-8.2.zip \
  && unzip z3-4.4.1-x64-debian-8.2.zip \
  && rm z3-4.4.1-x64-debian-8.2.zip \
  && ln -s /opt/z3-4.4.1-x64-debian-8.2/bin/z3 /usr/bin/z3 \
  && wget http://cvc4.cs.nyu.edu/builds/x86_64-linux-opt/unstable/cvc4-2016-04-20-x86_64-linux-opt \
  && mv cvc4-2016-04-20-x86_64-linux-opt /usr/bin/cvc4 \
  && chmod +x /usr/bin/cvc4 \
  && apt-get remove -y wget unzip \
  && rm -rf /var/lib/apt/lists/*

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
