FROM node:12.18.3

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

USER node

RUN npm install -g vsce
RUN npm install -g lock-treatment-tool
