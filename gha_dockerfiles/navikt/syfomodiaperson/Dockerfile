FROM node:14-alpine
WORKDIR /syfomodiaperson

COPY server.js package.json ./

COPY node_modules ./node_modules
COPY img ./img
COPY dist ./dist
COPY server ./server

EXPOSE 8080
CMD ["node", "server.js"]
