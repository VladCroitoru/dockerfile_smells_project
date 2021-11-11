# NEEDS SOME IMPROVEMENTS, MAINLY TO DO WITH THE
# SPEEDCONTROL BRANCH USED AND CONFIG SETTINGS

FROM node:10
WORKDIR /home/node/app
RUN chown -R node:node /home/node/app
# Install some packages to install NodeCG.
RUN npm install bower -g && npm install nodecg-cli -g
USER node
RUN nodecg setup
# Install latest nodecg-speedcontrol.
RUN nodecg install speedcontrol/nodecg-speedcontrol
# Copy over this bundle's files and fully build it.
WORKDIR /home/node/app/bundles/esa-layouts
USER root
RUN chown -R node:node /home/node/app/bundles/esa-layouts
USER node
COPY --chown=node:node package*.json ./
RUN npm install
COPY --chown=node:node . .
RUN npm run build
# Run NodeCG.
WORKDIR /home/node/app
EXPOSE 9090
CMD [ "nodecg", "start" ]
