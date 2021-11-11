FROM ubuntu:14.04
MAINTAINER Thomas Heilbronner <thomas.heilbronner@gmail.com>
RUN apt-get update && apt-get install -y\
  python-setuptools\
  python-dev\
  libyaml-dev
RUN easy_install pip
RUN pip install\
  PyYAML\
  python-jenkins\
  jenkins-job-builder\
  jenkins-job-builder-xvnc

