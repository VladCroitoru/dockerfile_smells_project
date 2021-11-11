FROM mtangaro/docker-galaxycloud-full

MAINTAINER ma.tangaro@ibiom.cnr.it

ENV container docker

COPY ["playbook.yaml","/"]

RUN ansible-galaxy install indigo-dc.galaxycloud-tools

RUN echo "localhost" > /etc/ansible/hosts

RUN ansible-playbook /playbook.yaml

# This overwrite docker-galaxycloud CMD line
CMD /bin/mount -t cvmfs elixir-italy.galaxy.refdata /refdata/elixir-italy.galaxy.refdata; /usr/local/bin/galaxy-startup; /usr/bin/sleep infinity
