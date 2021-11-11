FROM ocaml/opam:alpine-3.4_ocaml-4.03.0
RUN opam depext -ui -y -j 2 github tls cmdliner fmt
COPY . /home/opam/src
RUN sudo chown -R opam /home/opam/src
RUN rm -f /home/opam/src/*.native
WORKDIR /home/opam/src
RUN opam config exec -- ocamlbuild -use-ocamlfind list_issues.native
