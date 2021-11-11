FROM node:14-alpine3.14

WORKDIR /src

ADD package.json package-lock.json ./
RUN npm ci install

ADD . ./
RUN npm run build

EXPOSE 3000
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
#ENV NODE_ENV=production

CMD ["npm", "run", "start"]