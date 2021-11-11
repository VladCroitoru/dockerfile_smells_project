# Dockerfile for marconi, suitable for production
# MONGO_URI should be an env variable set to the URI of your Mongo instance
# MONGO_DATABASE should be an env variable set to the name of your Mongo database
# Forked from https://github.com/bentwire/marconi-simple for Trusty support
FROM		jayofdoom/docker-ubuntu-14.04
MAINTAINER 	Jay Faulkner <jay.faulkner@rackspace.com>

# install requirements
RUN apt-get -y update && apt-get -y install python-pip python-dev git gcc make

# Install marconi, wsgi server, tools
RUN pip install -e git+https://github.com/openstack/marconi#egg=marconi gunicorn

# Install marconi configs
ADD marconi.conf /etc/marconi/
ADD doit.sh /doit.sh

EXPOSE 80

ENTRYPOINT ["/doit.sh"]
