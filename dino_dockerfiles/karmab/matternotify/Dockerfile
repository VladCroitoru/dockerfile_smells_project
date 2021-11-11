FROM centos
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

RUN yum -y install centos-release-scl && yum -y install rh-python35 && LD_LIBRARY_PATH=/opt/rh/rh-python35/root/usr/lib64 /opt/rh/rh-python35/root/usr/bin/pip install mattermostdriver && rm -rf /var/cache/yum

ADD notify.py /usr/bin

RUN chmod o+x /usr/bin/notify.py
ENV LD_LIBRARY_PATH /opt/rh/rh-python35/root/usr/lib64

ENTRYPOINT ["/usr/bin/notify.py"]
