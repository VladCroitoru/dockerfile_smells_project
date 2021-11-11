FROM jenkins
USER root
RUN apt-get update && apt-get install -yq sudo isc-dhcp-client maven build-essential cmake octave octave-io
RUN apt-get update && apt-get install -yq xvfb

RUN mv /sbin/dhclient /usr/sbin/dhclient
RUN echo "jenkins ALL=(root) NOPASSWD: /usr/sbin/dhclient" >> /etc/sudoers
# RUN echo "jenkins ALL=(root) NOPASSWD: /usr/bin/Xvfb" >> /etc/sudoers
COPY dhcp-jenkins.sh /usr/local/bin/dhcp-jenkins.sh

ENV DISPLAY :0

USER jenkins
ENTRYPOINT ["/usr/local/bin/dhcp-jenkins.sh"]

