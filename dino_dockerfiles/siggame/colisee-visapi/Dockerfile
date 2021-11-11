FROM node:latest

ADD . visapi
WORKDIR visapi

RUN npm run setup
RUN npm run build

CMD ["npm", "run", "quick-start"]