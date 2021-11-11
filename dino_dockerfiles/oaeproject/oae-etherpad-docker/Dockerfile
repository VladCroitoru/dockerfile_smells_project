#
# Copyright 2017 Apereo Foundation (AF) Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
#     http://opensource.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.
#

#
# Setup in two steps
#
# Step 1: Build the image
# $ docker build -f Dockerfile -t oae-etherpad:latest .
# Step 2: Run the docker
# $ docker run -it --name=etherpad --net=host oae-etherpad:latest
#

FROM node:10-alpine
LABEL Name=OAE-Etherpad
LABEL Author=ApereoFoundation
LABEL Email=oae@apereo.org

#
# Install etherpad
#
ENV ETHERPAD_VERSION 1.6.3
ENV ETHERPAD_PATH /opt/etherpad

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh \
    && apk --no-cache add curl git su-exec \
    && addgroup -S -g 1001 etherpad \
    && adduser -S -u 1001 -G etherpad -G node etherpad \
    && curl -sLo /etherpad.tar.gz https://github.com/ether/etherpad-lite/archive/${ETHERPAD_VERSION}.tar.gz \
    && mkdir -p /opt \
    && tar -xz -C /opt -f /etherpad.tar.gz \
    && mv /opt/etherpad-lite-${ETHERPAD_VERSION} ${ETHERPAD_PATH} \
    && rm -f /etherpad.tar.gz \
    && sed -i -e "93 s,grep.*,grep -E -o 'v[0-9]\.[0-9](\.[0-9])?')," ${ETHERPAD_PATH}/bin/installDeps.sh \
    && sed -i -e '96 s,if.*,if [ "${VERSION#v}" = "$NEEDED_VERSION" ]; then,' ${ETHERPAD_PATH}/bin/installDeps.sh \
    && ${ETHERPAD_PATH}/bin/installDeps.sh \
    && rm -rf /tmp/*

# Set workdir for all commands below
WORKDIR ${ETHERPAD_PATH}

COPY settings.json settings.json
RUN chown -R etherpad:etherpad .

# Install ep_headings module
RUN npm install ep_headings

# Install ep_comments module
RUN npm install ep_page_view \
  && git clone https://github.com/oaeproject/ep_comments.git node_modules/ep_comments_page \
  && cd node_modules/ep_comments_page \
  && npm install

# Etherpad OAE plugin
RUN cd node_modules \
  && git clone https://github.com/oaeproject/ep_oae \
  && cd ep_oae \
  && npm install

# CSS changes
RUN rm node_modules/ep_headings/templates/editbarButtons.ejs && cp node_modules/ep_oae/static/templates/editbarButtons.ejs node_modules/ep_headings/templates/editbarButtons.ejs
RUN rm src/static/custom/pad.css && cp node_modules/ep_oae/static/css/pad.css src/static/custom/pad.css

# Must add the same key as config.js
RUN echo "13SirapH8t3kxUh5T5aqWXhXahMzoZRA" > APIKEY.txt
RUN echo "cocoxixi" > SESSIONKEY.txt

# Install PM2
RUN npm install --global pm2

# Set the right permissions
RUN chown -R etherpad:etherpad settings.json var
RUN chmod 755 settings.json

EXPOSE 9001

# Running with PM2
CMD ["sh", "-c", "pm2 start --restart-delay=3000 node_modules/ep_etherpad-lite/node/server.js && pm2 logs"]
