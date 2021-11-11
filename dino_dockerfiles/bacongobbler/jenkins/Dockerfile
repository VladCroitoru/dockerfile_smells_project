FROM jenkinsci/jenkins:2.58

COPY plugins.txt /usr/share/jenkins/plugins.txt

RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt \
  && mkdir -p /usr/share/jenkins/ref/secrets/ \
  && echo "false" > /usr/share/jenkins/ref/secrets/slave-to-master-security-kill-switch
