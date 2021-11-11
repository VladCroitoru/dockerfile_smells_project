FROM node

ADD package.json package.json
RUN npm install
ADD . .

EXPOSE 8080

CMD ["node", "src/simple.js"]
