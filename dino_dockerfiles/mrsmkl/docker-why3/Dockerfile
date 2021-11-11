
FROM ubuntu:16.04
MAINTAINER Sami Mäkelä

ENV PATH="/opt/Isabelle2016/bin:/opt/pvs:${PATH}"

RUN apt-get update && \
  apt-get install -y coq wget gcc ocaml menhir libmenhir-ocaml-dev libcoq-ocaml-dev libzarith-ocaml-dev\
                     libocamlgraph-ocaml-dev unzip liblablgtksourceview2-ocaml-dev\
                     libzip-ocaml-dev vim libxtst6

RUN mkdir src && cd src && \
  wget https://alt-ergo.ocamlpro.com/download_manager.php?target=alt-ergo-static-1.01-x86_64 -O alt-ergo && \
  chmod 755 alt-ergo && \
  mv alt-ergo /usr/bin && \
  wget https://github.com/Z3Prover/bin/raw/master/releases/z3-4.4.1-x64-ubuntu-14.04.zip && \
  unzip z3-4.4.1-x64-ubuntu-14.04.zip && \
  cp z3-4.4.1-x64-ubuntu-14.04/bin/z3 /usr/bin && \
  wget http://cvc4.cs.nyu.edu/builds/x86_64-linux-opt/cvc4-1.4-x86_64-linux-opt -O cvc4 && \
  chmod 755 cvc4 && \
  mv cvc4 /usr/bin

RUN cd opt && \
  dpkg --add-architecture i386 && \
  apt-get update && \
  apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 && \
  wget https://isabelle.in.tum.de/dist/Isabelle2016_app.tar.gz && \
  tar xf Isabelle2016_app.tar.gz && \
  echo '/usr/local/lib/why3/isabelle' >> /opt/Isabelle2016/etc/components

RUN cd opt && mkdir pvs && cd pvs && \
  wget 'http://pvs.csl.sri.com/cgi-bin/download.cgi?file=pvs-6.0-ix86_64-Linux-allegro.tgz&accept=I%20accept' -O pvs-allegro.tgz && \
  tar xf pvs-allegro.tgz && \
  ./bin/relocate

RUN cd src && \
  wget http://www.cs.miami.edu/~tptp/CASC/J8/SystemsSources/Vampire---4.1.tgz && \
  tar xf Vampire---4.1.tgz && \
  cp ./Vampire---4.1/vampire /usr/local/bin

RUN cd src && \
  wget https://gforge.inria.fr/frs/download.php/file/36133/why3-0.87.2.tar.gz && \
  tar xf why3-0.87.2.tar.gz && \
  cd why3-0.87.2 && \
  ./configure && \
  make && \
  make install && \
  why3 config --detect

RUN mv /usr/bin/coqc /usr/bin/coqc_orig && \
echo '#!/usr/bin/env bash\n\
coqc_orig -R /usr/local/lib/why3/coq-tactic/ Why3 -R /usr/local/lib/why3/coq/ Why3 $@'\
  >> /usr/bin/coqc && \
  chmod +x /usr/bin/coqc
