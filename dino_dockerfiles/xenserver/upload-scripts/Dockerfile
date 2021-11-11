FROM ocaml/opam2:debian-9-ocaml-4.04

RUN sudo apt-get update && sudo apt-get install -y createrepo s3cmd && sudo apt-get clean

RUN mkdir tmp/
RUN mkdir tmp/src/

# update the opam-repository
WORKDIR ./opam-repository
RUN git pull
RUN opam update


# First copy the opam file, and install the build dependencies - this way we
# will only install the build dependencies when the opam file changes.
COPY opam /tmp/

WORKDIR /tmp

# check the OPAM-related files for errors
RUN opam lint

RUN opam pin add -y --no-action update_xs_yum .

RUN opam install -y opam-depext && opam depext -y update_xs_yum

RUN opam install -y --deps-only update_xs_yum


# Copy the source code and some additional build files and build the program,
# now that we have all the build dependencies. If only the source code changes,
# then we won't reinstall the build deps again, docker will start building the
# image from this point, and reuse the layer containing the build deps.
COPY _tags Makefile update_xs_yum.install /tmp/
COPY src/update_xs_yum.ml /tmp/src/
# Remove leftover ocamlfind init files that ocamlbuild would complain about
RUN make clean

RUN opam install -y update_xs_yum
