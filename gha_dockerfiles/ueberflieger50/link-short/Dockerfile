FROM node:17
WORKDIR /link-short
COPY package*.json ./
RUN npm ci
COPY . .
# ENV SESSION_SECRET=Your-Session-Secret
VOLUME [ "/link-short/server/data" ]
CMD ["npm", "start"]
