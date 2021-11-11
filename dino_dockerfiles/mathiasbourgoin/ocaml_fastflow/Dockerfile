FROM debian:jessie

MAINTAINER Mathias Bourgoin

RUN apt-get update && \
  apt-get install -y sudo pkg-config git build-essential \
          m4  aspcud rsync \
          curl ocaml \
          ocaml-native-compilers camlp4-extra \
          libffi-dev emacs g++ opam subversion  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  useradd -ms /bin/bash spoc && echo "spoc:spoc" | \
    chpasswd && adduser spoc sudo


WORKDIR /home/spoc
RUN svn checkout svn://svn.code.sf.net/p/mc-fastflow/code/ff fastflow/ff
ADD src ocaml_fastflow/src
RUN chown -R spoc ocaml_fastflow

USER spoc
CMD /bin/bash
WORKDIR /home/spoc
COPY .bashrc /home/spoc/.bashrc

RUN opam init -a --root /home/spoc/.opam --comp 4.02.3

RUN eval `opam config env` && \
 opam update && \
 opam install -y camlp4.4.02+1 ctypes ocp-indent \
              ctypes-foreign ocamlfind ocamlfind && \
 opam pin -y add camlp4 4.02+1

RUN rm -rf SPOC &&  \
  git clone -b proto_fastflow https://github.com/mathiasbourgoin/SPOC.git && \
  eval `opam config env` && \
  cd SPOC/Spoc && make install && \
  cd ../SpocLibs/Sarek && make install

RUN mkdir /home/spoc/emacs_install
COPY docker/emacs-pkg-install.el  /home/spoc/emacs_install/emacs-pkg-install.el
COPY docker/emacs-pkg-install.sh  /home/spoc/emacs_install/emacs-pkg-install.sh

WORKDIR /home/spoc/emacs_install

RUN sh ./emacs-pkg-install.sh auto-complete && \
  sh ./emacs-pkg-install.sh company && \
  sh ./emacs-pkg-install.sh company-irony

RUN eval `opam config env`&& opam install -y merlin tuareg ocp-indent

COPY .emacs /home/spoc/.emacs
WORKDIR /home/spoc/
