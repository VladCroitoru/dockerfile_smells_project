FROM fedora:30
LABEL MAINTAINER Bradley Leonard <bradley@stygianresearch.com>
LABEL description="This container will run the boinc-client."

# install boinc
RUN dnf -y update && \
    dnf -y install compat-libstdc++-296.i686 compat-libstdc++-33.i686 compat-libstdc++-33.x86_64 && \
    dnf -y install boinc-client && \
    dnf clean all

EXPOSE 31416

#WORKDIR /var/lib/boinc

#USER boinc

#ENTRYPOINT ["boinc"]

# create directories
RUN mkdir /scripts

# add the startup.sh
ADD startup.sh /scripts/startup.sh
RUN chmod 755 /scripts/startup.sh

CMD ["/scripts/startup.sh"]
#CMD ["/bin/bash"]
