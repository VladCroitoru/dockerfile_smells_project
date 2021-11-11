FROM registry.access.redhat.com/ubi8/ubi-minimal:8.4-208


ARG ocpythonlibver=0.12.1


RUN microdnf install -y python39 tar gzip && microdnf clean all

RUN pip3 install "setuptools>=40.3.0" urllib3 chardet requests

RUN \
  cd /tmp && \
  curl -s -LO https://github.com/openshift/openshift-restclient-python/archive/v${ocpythonlibver}.tar.gz && \
  tar xvzf v${ocpythonlibver}.tar.gz && \
  cd openshift-restclient-python-${ocpythonlibver} && \
  python3 setup.py install

RUN  pip3 install prometheus_client paramiko pyyaml boto3 slackclient && mkdir /openshift-python

CMD [ "/bin/sh" ]

