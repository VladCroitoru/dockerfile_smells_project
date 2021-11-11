# Nereid Project
#
# VERSION	3.2.0.1

FROM openlabs/tryton:3.2
MAINTAINER Prakash Pandey <prakash.pandey@openlabs.co.in>

RUN apt-get -y update

# * Setup psycopg2 since you want to connect to postgres
#   database
RUN apt-get -y -q install python-dev libpq-dev python-gevent python-psycopg2 gunicorn

# Setup the module since it is a required for this
# custom setup
ADD . /opt/nereid-project/
WORKDIR /opt/nereid-project/
RUN pip install -r requirements.txt

VOLUME /var/lib/trytond

# Remove the existing trytond.conf
RUN rm /etc/trytond.conf

EXPOSE 	8000 9000
CMD ["-b", "0.0.0.0:9000", "-", "-k", "gevent", "-w", "4", "application:app"]
ENTRYPOINT ["gunicorn"]
