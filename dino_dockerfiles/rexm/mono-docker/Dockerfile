FROM ubuntu:14.04
MAINTAINER Rex Morgan <rex@rexmorgan.net> (@rexm)

RUN apt-get update -y -q
RUN apt-get -y -q install mono-devel
RUN mozroots --import --sync
