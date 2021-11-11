FROM node:9.6-alpine

# environment
ENV HTTP_PORT=3000
ENV NODE_ENV=development

# source code
ADD app /app
RUN chown -R node:node /app

# npm install
USER node
WORKDIR /app
RUN npm install && npm cache clean --force

# here we go!
EXPOSE $HTTP_PORT
CMD ["npm","start"]
