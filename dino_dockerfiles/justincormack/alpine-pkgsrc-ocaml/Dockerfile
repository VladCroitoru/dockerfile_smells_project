FROM justincormack/alpine-pkgsrc:latest

MAINTAINER Justin Cormack

ENV                                                                                     \
  OPAMYES=true                                                                          \
  CAML_LD_LIBRARY_PATH="/root/.opam/system/lib/stublibs:/usr/pkg/lib/ocaml/stublibs"    \
  MANPATH="/root/.opam/system/man:"                                                     \
  PERL5LIB="/root/.opam/system/lib/perl5"                                               \
  OCAML_TOPLEVEL_PATH="/root/.opam/system/lib/toplevel"                                 \
  PATH=/root/.opam/system/bin:$PATH

COPY aspcud /usr/local/bin/

COPY profile /root/.profile
COPY shinit /root/.shinit
COPY ocamlinit /root/.ocamlinit

RUN cd /usr/pkgsrc/lang/camlp4                         \
     && bmake && bmake install && bmake clean-depends

RUN wget https://github.com/ocaml/opam/releases/download/1.2.2/opam-full-1.2.2.tar.gz

RUN tar xzvf opam-full-1.2.2.tar.gz             \
    && cd opam-full-1.2.2                       \
    && make cold                                \
    && make install                             \
    && opam init --comp=4.02.3

RUN opam install ocamlfind

CMD ["sh"]
