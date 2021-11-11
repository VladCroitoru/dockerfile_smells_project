FROM ubuntu:latest AS download
ADD download.sh /
RUN bash /download.sh

FROM centos:centos6 AS build
ARG MAKE_J
RUN rm -f /etc/yum.repos.d/*.repo
ADD *.repo /etc/yum.repos.d/
RUN yum install -y centos-release-scl && yum install -y devtoolset-7
ADD build.sh /
COPY --from=download /download /build
RUN scl enable devtoolset-7 /build.sh

FROM centos:centos6
COPY --from=build /usr/local /usr/local
