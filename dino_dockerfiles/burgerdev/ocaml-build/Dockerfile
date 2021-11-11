FROM ocaml/opam:alpine-3.6_ocaml-4.06.0_flambda

USER root

RUN apk --no-cache add vim m4 ncurses

COPY --from=docker:17.12 /usr/local/bin/docker /usr/local/bin/docker

USER opam

RUN cd opam-repository && git pull origin master >/dev/null && cd ..

RUN opam update && opam install -y ocamlfind odoc ounit sexplib cmdliner logs fmt jbuilder mparser

