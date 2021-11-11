FROM fedora:23

ADD http://download.opensuse.org/repositories/isv:ownCloud:desktop/Fedora_23/isv:ownCloud:desktop.repo /etc/yum.repos.d/isv:ownCloud:desktop.repo
RUN dnf install -y owncloud-client && dnf clean all

ADD startup.sh /startup.sh

ENTRYPOINT [ "/startup.sh" ]
