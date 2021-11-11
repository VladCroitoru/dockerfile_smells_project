FROM ocaml/dev:release-ubuntu-14.04_ocaml-4.02.3
MAINTAINER canopy
ENV OPAMYES 1
RUN sudo apt-get update
RUN sudo apt-get -yy install npm
RUN sudo npm install -g less browserify
RUN cd /home/opam/opam-repository; git pull && opam update; cd -
RUN opam upgrade
RUN opam update
RUN sudo ln -s `which nodejs` /usr/bin/node
ADD package.json README.md config.ml /src/
WORKDIR /src
ADD tls /src/tls
RUN sudo chown -R opam:opam /src; sudo chmod -R 700 /src
ENV TMP /tmp
RUN opam config exec -- mirage configure --no-assets-compilation
COPY . /src
ADD assets /src/assets
RUN sudo chown -R opam:opam /src; sudo chmod -R 700 /src
RUN opam config exec -- mirage configure --no-opam --no-depext
RUN opam config exec -- make
EXPOSE 8080
ENTRYPOINT ["opam", "config", "exec", "--", "./mir-canopy"]