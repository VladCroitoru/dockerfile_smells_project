FROM node:alpine
COPY gk.js /gatekeeper/gk.js
RUN npm install restify
WORKDIR /gatekeeper
EXPOSE 8080
ENTRYPOINT ["node", "gk.js"]

