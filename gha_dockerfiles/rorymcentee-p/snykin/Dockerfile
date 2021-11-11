FROM registry.access.redhat.com/ubi8/nodejs-10:1-51

COPY package*.json ./

RUN npm ci --only=production

COPY . .

EXPOSE 3000
CMD ["node", "app.js"]
