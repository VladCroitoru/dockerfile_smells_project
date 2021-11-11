FROM debian:stable
MAINTAINER <Gabriel Falcão gabriel@nacaolivre.org>

RUN apt-get update
RUN apt-get install -y python-setuptools openssh-client git
RUN easy_install pip

ADD . /tumbler
WORKDIR /tumbler
RUN python setup.py install

# Expose
EXPOSE  5000

# Run
CMD ["tumbler", "run", "--host", "0.0.0.0", "--port", "5000", "angularjs/routes.py"]
