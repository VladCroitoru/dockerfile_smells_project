# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#
# nginx-ssl-proxy
#
# VERSION   0.0.1

FROM nginx

MAINTAINER Evan Brown <evanbrown@google.com>

RUN rm /etc/nginx/conf.d/*.conf

WORKDIR /usr/src

ADD start.sh /usr/src/
ADD nginx/nginx.conf /etc/nginx/
ADD nginx/proxy*.conf /usr/src/

ENTRYPOINT ./start.sh

# https://letsencrypt.org/howitworks/#installing-lets-encrypt
#ADD https://github.com/letsencrypt/letsencrypt/archive/master.zip /opt/letsencrypt
ADD letsencrypt /opt/letsencrypt

# Does a lot of package installations that we don't want at runtime.
# Prints a "No installers" error but that's normal.
RUN cd /opt/letsencrypt \
  && ./letsencrypt-auto; exit 0

RUN ln -s /root/.local/share/letsencrypt/bin/letsencrypt /usr/local/bin/letsencrypt

# Commented out because we don't really want defaults
#ENV cert_domains
#ENV cert_email
#ENV LETSENCRYPT_ENDPOINT

ADD start-cert.sh /usr/src/
