FROM java:8-jre-alpine

ENV RDECK_BASE=/opt/rundeck RDECK_VERSION=2.11.3 RDECK_SHA=4dcd7d4575aa0dab86ba064907c3a9e45d4d31f1
ENV RDECK_EC2_PLUGIN=1.5.5 RDECK_ANSIBLE_PLUGIN=2.4.0 RDECK_SLACK_PLUGIN=1.1

RUN apk add --no-cache \
      py-pip python-dev musl-dev \
      gcc libffi-dev openssl-dev \
      wget linux-headers bind-tools \
      git openssh-client ca-certificates make \
  && update-ca-certificates \
  && mkdir -p ${RDECK_BASE}/libext \
  && wget -O ${RDECK_BASE}/rundeck.jar \
         http://dl.bintray.com/rundeck/rundeck-maven/rundeck-launcher-${RDECK_VERSION}.jar \
  && echo "${RDECK_SHA}  ${RDECK_BASE}/rundeck.jar" | sha1sum -c \
  && wget -P ${RDECK_BASE}/libext \
         https://github.com/rundeck-plugins/rundeck-ec2-nodes-plugin/releases/download/v${RDECK_EC2_PLUGIN}/rundeck-ec2-nodes-plugin-${RDECK_EC2_PLUGIN}.jar \
  && wget -P ${RDECK_BASE}/libext \
         https://github.com/Batix/rundeck-ansible-plugin/releases/download/${RDECK_ANSIBLE_PLUGIN}/ansible-plugin-${RDECK_ANSIBLE_PLUGIN}.jar \
  && wget -P ${RDECK_BASE}/libext \
         https://github.com/rundeck-plugins/slack-incoming-webhook-plugin/releases/download/v${RDECK_SLACK_PLUGIN}/slack-incoming-webhook-plugin-${RDECK_SLACK_PLUGIN}.jar \
  && pip install boto paramiko PyYAML Jinja2 httplib2 six ansible awscli shade

EXPOSE 4440

VOLUME [ "/etc/ansible", \
         "${RDECK_BASE}/etc", \
         "${RDECK_BASE}/var/logs", \
         "${RDECK_BASE}/server/logs", \
         "${RDECK_BASE}/server/config" ]

CMD [ "java","-jar","/opt/rundeck/rundeck.jar" ]
