# syntax = docker/dockerfile:1.0-experimental
FROM centos:7
ARG dirac_version=v7r1p45

RUN yum install -y wget
RUN mkdir /root/dirac_ui
RUN wget -np -O /root/dirac_ui/dirac-install https://raw.githubusercontent.com/DIRACGrid/DIRAC/integration/Core/scripts/dirac-install.py
RUN chmod u+x /root/dirac_ui/dirac-install

WORKDIR /root/dirac_ui
RUN /root/dirac_ui/dirac-install -r $dirac_version
RUN rm -f /root/dirac_ui/dirac-install
RUN --mount=type=secret,id=proxy,dst=/tmp/x509up_u0 . /root/dirac_ui/bashrc && dirac-configure -F -S GridPP -C dips://dirac01.grid.hep.ph.ic.ac.uk:9135/Configuration/Server -I

WORKDIR /root
COPY startup.sh /root/startup.sh

CMD ["/bin/bash", "--init-file", "/root/startup.sh"]
