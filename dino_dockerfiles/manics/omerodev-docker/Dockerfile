FROM centos:centos7
MAINTAINER ome-devel@lists.openmicroscopy.org.uk

RUN yum -y install epel-release git sudo && \
    yum -y install ansible && \
    yum clean all

WORKDIR /opt/install
ADD inventory.yml \
    omerodev-docker.yml \
    requirements.yml \
    /opt/install/
# Updated 2018-08-20
ADD https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/72f0e42e579a3ed3d993b95cb75088114a52bc93/files/docker/systemctl.py /opt/bin/systemctl
RUN ansible-galaxy install -r requirements.yml -p roles
# Update systemd so that it doesn't overwrite our override
RUN yum -y update systemd && \
    ln -sf /opt/bin/systemctl /bin/systemctl && \
    chmod +x /opt/bin/systemctl && \
    # Dodgy hack to get Ansible to recognise systemd https://github.com/ansible/ansible-modules-core/issues/593#issuecomment-144725409 \
    echo -n systemd > /proc/1/comm && \
    ansible-playbook -i inventory.yml omerodev-docker.yml && \
    yum clean all

RUN curl -o /opt/bin/gosu -fsSL \
    https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 && \
    chmod +x /opt/bin/gosu
ADD entrypoint.sh /opt/bin/
ADD omerodev-docker-post.yml /opt/install/

WORKDIR /home/build
RUN mkdir /OMERO && \
    chown build:build /OMERO

EXPOSE 80 443 8080 4061 4063 4064

VOLUME ["/home/build/src", "/OMERO", "/var/lib/pgsql/9.6/data"]

# Set the default command to run when starting the container
ENTRYPOINT ["/opt/bin/entrypoint.sh"]
