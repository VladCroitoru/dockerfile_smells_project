FROM mtangaro/docker-galaxycloud-full

MAINTAINER ma.tangaro@ibiom.cnr.it

ENV container docker

RUN echo "localhost" > /etc/ansible/hosts

ADD install_tools.sh /usr/local/bin/install-tools

RUN chmod +x /usr/local/bin/install-tools 

RUN wget https://raw.githubusercontent.com/indigo-dc/Galaxy-flavors-recipes/devel/galaxy-epigen/galaxy-ngs-base.yml -O /tmp/tools.yml

RUN /usr/local/bin/install-tools GALAXY_ADMIN_API_KEY /tmp/tools.yml && \
    /export/_conda/bin/conda clean --tarballs --yes > /dev/null

# This overwrite docker-galaxycloud CMD line
CMD /bin/mount -t cvmfs elixir-italy.galaxy.refdata /refdata/elixir-italy.galaxy.refdata; /usr/local/bin/galaxy-startup; /usr/bin/sleep infinity
