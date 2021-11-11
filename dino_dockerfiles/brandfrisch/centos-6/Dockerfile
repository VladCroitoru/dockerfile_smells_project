FROM centos:6
MAINTAINER Martin Diederich <martin.diederich@gmail.com>

# set env vars
ENV container docker
ENV LC_ALL C

# install
RUN yum -y update
RUN yum -y install epel-release

# install typical requirements for testing
RUN yum -y install ca-certificates python python-httplib2 sudo unzip curl net-tools nc

# install goss
RUN curl -L https://github.com/aelsabbahy/goss/releases/download/v0.2.6/goss-linux-amd64 -o /usr/local/bin/goss
RUN chmod +rx /usr/local/bin/goss

# install docker-detect-proxy.sh
RUN curl -L https://raw.githubusercontent.com/mdicloud/docker-helper/master/docker-detect-proxy.sh -o /usr/local/bin/docker-detect-proxy.sh
RUN chmod +rx /usr/local/bin/docker-detect-proxy.sh

# cleanup
RUN yum clean all

# finally run script on startup
ENTRYPOINT ["/usr/local/bin/docker-detect-proxy.sh"]
CMD ["/bin/bash"]
