FROM openshift/base-centos7
MAINTAINER Francois Dickey <francois@dickey.com>

ENV BUILDER_VERSION 1.0

LABEL io.k8s.description="S2I Builder image for compiling applications with Makefile" \
      io.k8s.display-name="Makefile S2I builder 1.0" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,makefile,c,c++,gcc,g++"

LABEL io.openshift.s2i.scripts-url=image:///usr/local/sti

COPY ./sti/bin/ /usr/local/sti

RUN yum install -y ncurses-devel uuid-devel libuuid-devel libxml2-devel sqlite-devel bison jansson-devel && \
    mkdir -p /opt/src && chmod -R a+rwX /opt/app-root && \
    mkdir -p /opt/app-root && chmod -R a+rwX /opt/app-root && \
    chown -R 1001:1001 /opt/app-root && \
    chown -R 1001:1001 /opt/src

USER 1001

CMD ["usage"]
