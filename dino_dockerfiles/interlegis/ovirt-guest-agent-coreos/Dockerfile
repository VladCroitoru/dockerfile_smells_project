FROM centos

LABEL summary="The oVirt Guest Agent" \
      io.k8s.description="The ovirt-guest-agent is providing information about the virtual machine and allows to restart / shutdown the machine via the oVirt Portal." \
      io.k8s.display-name="oVirt Guest Agent" \
      license="ASL 2.0" \
      architecture="x86_64"

ADD logger_conf /root/logger_conf

RUN yum install epel-release -y --setopt=tsflags=nodocs; yum -y --setopt=tsflags=nodocs install ovirt-guest-agent-common
RUN cat /root/logger_conf >> /etc/ovirt-guest-agent.conf && rm /root/logger_conf

COPY ovirt-container-shutdown.sh prep.sh /usr/local/bin/
COPY run.sh /usr/bin/

RUN /bin/bash /usr/local/bin/prep.sh
RUN chmod a+x /usr/local/bin/ovirt-*.sh /usr/bin/run.sh

CMD /bin/bash /usr/bin/run.sh
