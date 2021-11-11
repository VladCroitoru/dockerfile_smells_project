FROM node
ENV NPM_CONFIG_LOGLEVEL warn
EXPOSE 3001

#
# Sometimes the host user's id doesn't align with the container user's id.
# If there are any permission errors, this is one likely cause
#
# RUN usermod -u 1001 node

USER node
ENV HOME=/home/node

WORKDIR $HOME

ENV PATH $HOME/app/node_modules/.bin:$PATH

ADD package.json $HOME
RUN npm install --production

CMD ["node", "./app.js"]
