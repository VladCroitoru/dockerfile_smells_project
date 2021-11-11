FROM node:latest


ADD package.json package.json
RUN npm install
ADD . .

EXPOSE 3000
CMD ["node","app.js"]
