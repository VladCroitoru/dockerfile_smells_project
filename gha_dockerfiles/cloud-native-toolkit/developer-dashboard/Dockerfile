FROM registry.access.redhat.com/ubi8/nodejs-12:1-59
RUN echo ${HOME}
RUN whoami
RUN pwd

ENV NPM_CONFIG_PREFIX=${HOME}/.npm-global
ENV PATH=$PATH:${HOME}/.npm-global/bin

RUN mkdir -p ${HOME}/app/client && \
    mkdir -p ${HOME}/app/server && \
    mkdir -p ${HOME}/app/public

# Install npm packages
COPY --chown=default:root . ${HOME}/app
RUN cd ${HOME}/app; npm install && npm run build

ENV NODE_ENV production
ENV PORT 3000

EXPOSE 3000/tcp

WORKDIR ${HOME}/app

CMD ["npm", "start"]



