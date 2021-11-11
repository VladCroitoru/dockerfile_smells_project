FROM mtangaro/docker-galaxycloud

MAINTAINER ma.tangaro@ibiom.cnr.it

ENV container docker

COPY ["playbook.yaml","/"]

# Add script to install tools without ansible
ADD install_tools.sh /usr/local/bin/install-tools
RUN chmod +x /usr/local/bin/install-tools

RUN ansible-galaxy install indigo-dc.cvmfs-client
RUN ansible-galaxy install indigo-dc.galaxycloud-refdata

ADD https://raw.githubusercontent.com/indigo-dc/Reference-data-galaxycloud-repository/master/cvmfs_server_keys/elixir-italy.galaxy.refdata.pub /tmp/elixir-italy.galaxy.refdata.pub

RUN echo "localhost" > /etc/ansible/hosts

RUN ansible-playbook /playbook.yaml

# This overwrite docker-galaxycloud CMD line
CMD /bin/mount -t cvmfs elixir-italy.galaxy.refdata /refdata/elixir-italy.galaxy.refdata; /usr/local/bin/galaxy-startup; /usr/bin/sleep infinity
