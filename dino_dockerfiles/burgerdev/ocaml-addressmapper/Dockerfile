FROM ocaml/opam2:alpine-3.8-ocaml-4.06 AS build

RUN sudo apk --no-cache add m4 ncurses

RUN opam update && opam install -y ocamlfind odoc ounit sexplib cmdliner logs fmt jbuilder mparser

ADD --chown=opam:nogroup . /src

WORKDIR /src

RUN eval `opam config env` && jbuilder build

FROM alpine

COPY --from=build /src/_build/default/bin/main.exe  /mapper

EXPOSE 30303

ENTRYPOINT ["/mapper", "-i"]
