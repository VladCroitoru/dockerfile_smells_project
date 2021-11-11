FROM phenoscape/owlery

MAINTAINER Robbie - Virtual Fly Brain <rcourt@ed.ac.uk>

ENV OWLURL=https://github.com/VirtualFlyBrain/VFB_owl/blob/Current/src/owl/vfb.owl.gz?raw=true

COPY application.conf /srv/conf/application.conf

USER root

COPY startup.sh /startup.sh

RUN chmod +x /startup.sh

USER $APP_USER

ENTRYPOINT ["/startup.sh"]
