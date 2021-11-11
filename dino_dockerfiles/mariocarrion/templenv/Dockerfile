# vim: set syntax=dockerfile:
FROM golang:1.7.4

COPY Makefile /
WORKDIR /

COPY ./ ./go/src/github.com/MarioCarrion/templenv
RUN make gobuild
CMD ["/bin/bash"]
