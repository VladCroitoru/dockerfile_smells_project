# MIT License
# Copyright (c) 2017 - 2020 Fabian Wenzelmann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# NOTE: This file was largely inspired by tvelocity/etherpad-lite:
# https://github.com/tvelocity/dockerfiles/blob/master/etherpad-lite/entrypoint.sh

FROM node:15.1.0-alpine3.12
MAINTAINER Fabian Wenzelmann <fabianwen@posteo.eu>

ENV ETHERPAD_VERSION=1.8.6
ENV NODE_ENV=production

WORKDIR /opt/

RUN apk add --no-cache curl \
  && apk add --no-cache --virtual .build-deps \
    gzip \
  && curl -SL \
    https://github.com/ether/etherpad-lite/archive/${ETHERPAD_VERSION}.zip \
    > etherpad.zip && unzip -q etherpad && rm etherpad.zip  \
  &&  mv etherpad-lite-${ETHERPAD_VERSION} etherpad-lite \
  && cd etherpad-lite \
  && bin/installDeps.sh \
  && apk del .build-deps

WORKDIR etherpad-lite
RUN rm settings.json && ln -s var/settings.json settings.json
RUN ln -s var/APIKEY.txt APIKEY.txt && ln -s var/SESSIONKEY.txt SESSIONKEY.txt

VOLUME /opt/etherpad-lite/var

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 9001

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bin/run.sh", "--root"]
