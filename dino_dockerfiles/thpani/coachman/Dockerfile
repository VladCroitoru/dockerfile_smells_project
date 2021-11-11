FROM ocaml/opam2

# update opam
RUN opam update
RUN cd ..

# update apt
RUN sudo apt-get update

# install coachman
ARG CACHEBUST=1
RUN git clone https://github.com/thpani/coachman.git
RUN opam pin add -n coachman coachman
RUN opam depext coachman
RUN opam install coachman ounit
ENV LD_LIBRARY_PATH /home/opam/.opam/4.05.0/lib/z3:$LD_LIBRARY_PATH
WORKDIR /home/opam/coachman
