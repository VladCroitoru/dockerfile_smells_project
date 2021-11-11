FROM debian:jessie-slim

RUN apt-get update && \
    apt-get install -y curl apt-transport-https python-setuptools gunicorn && \
    curl -sL https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh > /usr/sbin/wait-for-it.sh && \
    chmod +x /usr/sbin/wait-for-it.sh && \
    curl -sL http://download.gluster.org/pub/gluster/glusterfs/3.9/rsa.pub | apt-key add - && \
    echo deb http://download.gluster.org/pub/gluster/glusterfs/3.9/LATEST/Debian/jessie/apt jessie main > /etc/apt/sources.list.d/gluster.list && \
    apt-get update && \
    apt-get install -y glusterfs-server && \
    curl -sL https://github.com/aravindavk/glusterfs-rest/archive/master.tar.gz | tar xz && \
    cd glusterfs-rest-master && python setup.py install && cd .. && \
    glusterrest install ; \
    glusterrest useradd root -g glusteradmin -p root


HEALTHCHECK CMD curl -sLi root:root@localhost:9000/api/1.0/volumes | grep '"ok": true' || exit 1

EXPOSE 24007 24008 49152 38465 38466 38467

COPY start.sh .
CMD ./start.sh