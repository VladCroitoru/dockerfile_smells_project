FROM avsm/docker-opam:ubuntu-trusty-4.02.1
MAINTAINER Thomas Gazagnaire <thomas@gazagnaire.org>
RUN opam switch --no-switch run -A system
ADD .opam-config-exec /usr/bin/opam-config-exec
RUN sudo chmod 755 /usr/bin/opam-config-exec
ADD .mirage-configure /usr/bin/mirage-configure
RUN sudo chmod 755 /usr/bin/mirage-configure
ADD .mirage-build /usr/bin/mirage-build
RUN sudo chmod 755 /usr/bin/mirage-build
RUN opam install mirage --switch=run
RUN opam install mirage
WORKDIR /home/opam
ADD packages/ dockage/packages/
RUN sudo chown -R opam dockage
RUN opam remote add dockage dockage
RUN opam update
RUN /bin/bash -c "opam install -v -j 1 `ls dockage/packages | tr '\n' ' '`"
ENTRYPOINT ["/usr/bin/opam-config-exec"]
CMD ["bash"]
