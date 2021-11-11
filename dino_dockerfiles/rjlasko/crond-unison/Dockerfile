FROM rjlasko/minikron:0.6
MAINTAINER rjlasko

ENV OCAML_VERSION "4.06.1"
ENV UNISON_VERSION "2.51.2"

COPY fsroot /
RUN /bin/sh /tmp/build.sh && \
	rm -rf /tmp/*
