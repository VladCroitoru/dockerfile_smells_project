FROM node:15-alpine

# Prepare app directory
WORKDIR /home/node/app
COPY package*.json /home/node/app/
COPY .snyk /home/node/app/

# Set up local user to avoid running as root
RUN chown -R node:node /home/node/app
USER node

# Install app dependencies
RUN npm ci

# Bundle app source code
COPY --chown=node:node . /home/node/app/

RUN npm run build

# Bind to all network interfaces so that it can be mapped to the host OS
ENV HOST=0.0.0.0 PORT=3000

EXPOSE ${PORT}
CMD [ "node", "-r", "dotenv/config", "." ]
