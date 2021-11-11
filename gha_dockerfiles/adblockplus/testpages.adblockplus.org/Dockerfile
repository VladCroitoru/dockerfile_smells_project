# Copyright (c) 2019-present eyeo GmbH
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

FROM node:12-buster-slim

RUN apt-get update
RUN apt-get install -y wget git unzip

# Non-headless Chromium requires xvfb-run
RUN apt-get install -y libgtk-3-0 libxt6 xvfb libnss3 libxss1 libgconf-2-4 libasound2 libgbm1

# CMS and Jinja2 require Python 2.7
RUN apt-get install -y python
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python get-pip.py

RUN pip install Jinja2

# Sitescripts require spawn-fcgi, python-flup and python-m2crypto
RUN apt-get install -y spawn-fcgi python-flup python-m2crypto nginx

# nginx config
ENV DOMAIN=local.testpages.adblockplus.org
COPY test/etc /etc
RUN rm /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/sites-available/default
RUN cd /etc/nginx && openssl req -x509 -newkey rsa:4096 \
  -keyout ${DOMAIN}_key.pem \
  -out ${DOMAIN}_cert.pem \
  -days 365 -nodes -subj '/CN=$DOMAIN'

# spawn-fcgi config
RUN touch /var/run/500-multiplexer_spawn-fcgi.pid

# Build sitescripts
RUN git clone https://gitlab.com/eyeo/devops/legacy/sitescripts.git

# Build CMS
RUN git clone https://github.com/adblockplus/cms.git
RUN pip install -r cms/requirements.txt

# Build tests
COPY package.json testpages.adblockplus.org/package.json
RUN cd testpages.adblockplus.org --init && npm install

COPY . testpages.adblockplus.org

# Generate test pages files
ENV SITE_URL=https://$DOMAIN:5000
RUN mkdir -p /var/www/$DOMAIN
RUN PYTHONPATH=cms python -m cms.bin.generate_static_pages testpages.adblockplus.org /var/www/$DOMAIN

# Unpack custom extension
ARG EXTENSION_FILE=""
RUN if [ "$EXTENSION_FILE" != "" ]; then unzip -q testpages.adblockplus.org/$EXTENSION_FILE -d testpages.adblockplus.org/testext; fi

ENV BROWSER="Firefox \(latest\)"
ENV TESTS_SUBSET=""
ENV SKIP_EXTENSION_DOWNLOAD=""

ENTRYPOINT ./testpages.adblockplus.org/test/entrypoint.sh
