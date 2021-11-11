# Galaxy - UbuntuFlavorDemo2
#
# VERSION       0.1

FROM bgruening/galaxy-stable

MAINTAINER Mau Mauleon, maumauleon@gmail.com

ENV GALAXY_CONFIG_BRAND UbuntuFlavorDemo2
ENV GALAXY_DOCKER_ENABLED True
ENV GALAXY_DOCKER_VOLUMES_FROM ''

#RUN add-tool-shed --url 'http://testtoolshed.g2.bx.psu.edu/' --name 'Test Tool Shed'
RUN add-tool-shed --url 'http://toolshed.g2.bx.psu.edu/' --name 'Main Tool Shed'

# Install myTools
ADD mytools.yaml $GALAXY_ROOT/my-tools.yml
RUN install-tools $GALAXY_ROOT/my-tools.yml

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
