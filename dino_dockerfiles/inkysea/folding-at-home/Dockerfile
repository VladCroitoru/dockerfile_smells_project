# Folding@home

FROM vmware/photon


RUN tdnf -y install chkconfig ;\
    tdnf -y install procps-ng ;\
    tdnf -y install sed ;\
    tdnf -y install shadow ;\
    rpm -ivh --nodeps https://fah.stanford.edu/file-releases/public/release/fahclient/centos-5.3-64bit/v7.4/fahclient-7.4.4-1.x86_64.rpm

ADD config.xml /etc/fahclient/
ADD start.sh /etc/fahclient/
RUN chown fahclient:root /etc/fahclient/config.xml

CMD  sh /etc/fahclient/start.sh