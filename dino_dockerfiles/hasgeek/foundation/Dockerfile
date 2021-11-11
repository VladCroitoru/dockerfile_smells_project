FROM ubuntu:14.04

# Configure apt
RUN apt-get update && apt-get install -y build-essential git curl python python-dev python-setuptools software-properties-common python-software-properties libpq-dev libffi-dev libxml2-dev libxslt1-dev pandoc nodejs libjpeg-dev unzip
RUN easy_install-2.7 pip

# add our requirements
ADD requirements.txt /foundation/requirements.txt
ADD build.sh /foundation/build.sh
RUN chmod +x /foundation/build.sh