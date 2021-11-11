FROM ralphie02/devuan:wheezy
LABEL maintainer="Ralph Azucena"

RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" \
  > /etc/apt/sources.list.d/ansible.list \
  && apt-get update \
  && apt-get install -y --force-yes --no-install-recommends ansible \
  && rm -rf /var/lib/apt/lists/* \
  && rm -Rf /usr/share/doc \
  && rm -Rf /usr/share/man \
  && apt-get autoremove -y \
  && apt-get autoclean \
  && apt-get clean
