FROM ubuntu
USER root

RUN apt-get update \
  && apt-get install -y python python3 python-pip python3-pip python-tk python3-tk wget openssh-server tar vim \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && echo "root:training" | chpasswd \
  && sed -i 's/prohibit-password/yes/' /etc/ssh/sshd_config \
  && mkdir /root/.pycharm_helpers

#ADD ssh.tar /root/
ADD start.sh /
ADD helpers/helpers.tgz /root/.pycharm_helpers
ADD helpers/build.txt /root/.pycharm_helpers

RUN mkdir /root/.ssh \
  && chown -R root:root /root/.ssh \
  && chmod -R 700 /root/.ssh \
  && echo "StrictHostKeyChecking=no" >> /etc/ssh/ssh_config \
  && mkdir /var/run/sshd

EXPOSE 22
CMD service ssh start && bash /start.sh
