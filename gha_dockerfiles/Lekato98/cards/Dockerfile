FROM node:14
ENV NODE_ENV production
ENV PORT 3000

WORKDIR /app

COPY ./build /app/build
COPY ./src/public /app/build/public
COPY ./package.json /app/package.json
COPY ./package-lock.json /app/package-lock.json

RUN npm install --production

CMD ["npm", "run", "start:prod"]
