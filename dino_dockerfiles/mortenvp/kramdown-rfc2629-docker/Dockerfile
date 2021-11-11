# To build an image from this docker file
#
# cd kramdown-rfc2629-docker/
#
# Run:
#
# docker build -t mortenvp/kramdown-rfc2629-docker .
#
# To create a container and and build the rfc-skel exmaple in the
# kramdown-rfc2629 repository.
#
# sudo docker run --name rfc-skel -v ~/dev/rfc-skel/:/rfc mortenvp/kramdown-rfc2629-docker
#
# The container will exit after running make in the mapped folder.
#
# If we want to start it again use:
#
# sudo docker start rfc-skel
#
FROM ubuntu:14.10

MAINTAINER Morten V. Pedersen <morten@mortenvp.com>

RUN apt-get update && apt-get install -y \
  libxml2-dev \
  libxslt-dev \
  libz-dev \
  python-dev \
  python-pip \
  rubygems

# Lets install the kramdown-rfc2629 tool

RUN gem install kramdown-rfc2629

# The following commands will install xml2rfc using pip as described here:
# https://pypi.python.org/pypi/xml2rfc

RUN pip install xml2rfc

# We should expose our RFC markdown code to the container:
#
# docker run -name rfc-something -P -v /home/user/dev/rfc-something:/rfc

WORKDIR /rfc

# We just run make inside the /rfc folder, so make sure your RFC can be
# built using make

CMD make rfc