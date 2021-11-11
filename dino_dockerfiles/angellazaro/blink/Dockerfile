FROM arm32v7/node:9.4.0-stretch

COPY package.json ./
COPY start.js ./
COPY piTest ./
RUN npm install
CMD ["npm", "start"]
