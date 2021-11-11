# Based on https://github.com/plone/volto/blob/master/entrypoint.sh
FROM node:12-stretch-slim

COPY . /opt/frontend/
WORKDIR /opt/frontend/

# Update apt packages
RUN runDeps="openssl ca-certificates patch git" \
 && apt-get update \
 && apt-get install -y --no-install-recommends $runDeps \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && chown -R node /opt/frontend/ \
 && cp jsconfig.json.tpl jsconfig.json \
 && mkdir -p /opt/frontend/src/addons \
 && rm -rf /opt/frontend/src/addons/* \
 && npm install -g mrs-developer

USER node

ARG MAX_OLD_SPACE_SIZE=8192
ENV NODE_OPTIONS=--max_old_space_size=$MAX_OLD_SPACE_SIZE

RUN cd /opt/frontend \
 && RAZZLE_API_PATH=VOLTO_API_PATH RAZZLE_INTERNAL_API_PATH=VOLTO_INTERNAL_API_PATH yarn \
 && RAZZLE_API_PATH=VOLTO_API_PATH RAZZLE_INTERNAL_API_PATH=VOLTO_INTERNAL_API_PATH yarn build \
 && rm -rf /home/node/.cache

EXPOSE 3000 3001 4000 4001

ENTRYPOINT ["/opt/frontend/entrypoint-prod.sh"]
CMD ["yarn", "start:prod"]
USER root
