FROM fedora:21
MAINTAINER Aaron Weitekamp <aweiteka@redhat.com>

RUN yum install -y python-pip python-devel gcc
ADD requirements.txt /uatframework/
RUN pip install -r /uatframework/requirements.txt
ADD features /uatframework/features
ADD steps /uatframework/steps
ADD environment.py /uatframework/environment.py
LABEL RUN="docker run -it -v $HOME/.ssh:/root/.ssh -v /path/to/UATFramework/resources.json:/uatframework/resources.json -v /path/to/UATFramework/config:/uatframework/config aweiteka/uatframework"
WORKDIR /uatframework
ENTRYPOINT ["/usr/bin/behave"]
