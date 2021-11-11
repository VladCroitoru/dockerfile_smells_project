FROM node:15-alpine

WORKDIR /src

COPY package.json package-lock.json /src/
RUN npm ci

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]

LABEL org.label-schema.vcs-url="https://github.com/cyverse-de/sonora"
