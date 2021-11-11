FROM centos:7

RUN INSTALL_PKGS="docker-1.10.3 git jq" && \
    rpm -ihv https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum install -y $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all

LABEL io.k8s.display-name="APPUiO Docker Builder" \
      io.k8s.description="This is the APPUiO Docker Builder."

ENV HOME=/root
COPY build.sh /tmp/build.sh
CMD ["/tmp/build.sh"]
