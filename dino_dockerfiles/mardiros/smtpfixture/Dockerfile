from python:2

MAINTAINER Guillaume Gauvrit <guillaume@gauvr.it>

RUN apt-get update
RUN apt-get install -y python-twisted

ADD . /srv/smtpfixture

WORKDIR /srv/smtpfixture

RUN python setup.py install
RUN python setup.py develop

RUN mkdir /var/lib/smtpfixture
VOLUME  ["/var/lib/smtpfixture"]

WORKDIR /srv/smtpfixture/smtpfixture

CMD ["twistd", "-n", "smtpfixture", "-p", "25", "-m", "/srv/smtpfixture/data"]

