FROM python:2.7

MAINTAINER Ken Sheedlo <ovrkenthousand@gmail.com>

ENV FAR_CONFIG /srv/far/config/config.json
ENV PYTHONUNBUFFERED true

# Note: Debian installs Node.js as the "nodejs" package.
# Normally this would be fine, but it also installs
# the binary as /usr/bin/nodejs instead of /usr/bin/node,
# which breaks Bower. To correct this problem, we have the
# line beginning with "update-alternatives".
#
# For more information, refer to the following blog post:
#
#   http://antler.co.za/2014/04/install-node-js-npm-on-debian-stable-wheezy-7/
#
RUN apt-get update \
  && apt-get -y install \
    nodejs \
    npm \
    xmlsec1 \
  && update-alternatives --install /usr/bin/node nodejs /usr/bin/nodejs 100 \
  && rm -rf /var/lib/apt/lists/*

RUN npm install -g bower

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /srv/far
COPY . /srv/far/
WORKDIR /srv/far/
RUN bower install --allow-root

VOLUME /srv/far/keys
VOLUME /srv/far/config
WORKDIR /srv/far/src/far

EXPOSE 5000
CMD ["gunicorn", \
  "-b", "0.0.0.0:5000", \
  "-k", "eventlet", \
  "--limit-request-line=8190", \
  "-R", \
  "-w", "1", \
  "far:app"]
