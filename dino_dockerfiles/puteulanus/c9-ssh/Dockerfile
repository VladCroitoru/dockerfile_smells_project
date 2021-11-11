FROM puteulanus/c9-core

RUN yum install -y openssh-clients net-tools
RUN sed -i 's/BASH + " -l"/"ssh -t -p $SSH_PORT $SSH_USER@REMOTE_IP_ADDR \\"clear;$SHELL\\""/' \
  /usr/src/c9sdk/node_modules/vfs-local/localfs.js
ADD init.sh /init.sh

ENV SSH_IP=
ENV SSH_USER root
ENV SSH_PORT 22
ENV WORKSPACE_DIR /workspace
VOLUME /root/.ssh

CMD bash /init.sh
