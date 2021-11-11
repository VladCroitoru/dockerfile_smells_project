FROM ubuntu:xenial
ENV container docker
LABEL maintainer="Stephen Dunne"

RUN apt-get update \
  && apt-get install -y \
     python-software-properties software-properties-common \
     apt-transport-https \
  && rm -rf /var/lib/apt/lists/* \
  && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
  && apt-get clean

RUN add-apt-repository -y ppa:ansible/ansible \
  && apt-get update \
  && apt-get install -y \
     ansible python-pip git \
  && pip install ansible-lint \
  && rm -rf /var/lib/apt/lists/* \
  && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
  && apt-get clean

RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

RUN systemctl set-default multi-user.target

STOPSIGNAL SIGRTMIN+3
#ENTRYPOINT ["/lib/systemd/systemd", "--system", "--unit=multi-user.target"]
ENTRYPOINT ["/sbin/init"]
