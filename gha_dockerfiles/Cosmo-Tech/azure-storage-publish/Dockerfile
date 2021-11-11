FROM node:16.2.0-alpine3.11
COPY package.json package.json
RUN npm install
COPY src/ src/
CMD node .
