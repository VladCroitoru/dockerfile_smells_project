FROM node:alpine

WORKDIR /app
COPY package.json ./
RUN yarn
COPY ./ ./
USER 1000
CMD ["yarn", "start"]
