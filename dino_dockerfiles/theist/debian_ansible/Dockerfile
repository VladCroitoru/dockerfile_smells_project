FROM debian
MAINTAINER Carlos Peñas
RUN apt-get -y update
RUN apt-get install -y python-dev python-pip libffi-dev python-setuptools pypy-lib libyaml-dev libgnutls-openssl-dev libssl-dev
RUN pip install cffi --upgrade
RUN pip install cryptography --upgrade
RUN pip install ansible

COPY ansible_and_bash.sh /ansible_and_bash.sh
RUN chmod a+x /ansible_and_bash.sh
CMD /ansible_and_bash.sh
