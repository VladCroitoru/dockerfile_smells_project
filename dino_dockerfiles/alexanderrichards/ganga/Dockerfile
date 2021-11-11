# syntax = docker/dockerfile:1.0-experimental
ARG dirac_version=v7r1p45
FROM alexanderrichards/dirac_ui:${dirac_version}
ARG ganga_version=8.5.3

RUN yum install -y epel-release
RUN yum install -y python3 root python3-root
RUN python3 -m pip install --upgrade pip setuptools wheel

WORKDIR /root
RUN python3 -m pip install ganga==$ganga_version
RUN echo -e "[DIRAC]\nDiracEnvSource = /root/dirac_ui/bashrc" > /root/.gangarc
RUN echo -e "[Configuration]\nRUNTIME_PATH=GangaDirac" >> /root/.gangarc
RUN yes | ganga -g
RUN mkdir -p /root/.cache/Ganga
RUN echo $ganga_version > /root/.cache/Ganga/.used_versions

COPY startup.sh /root/startup.sh
CMD ["/root/startup.sh"]
