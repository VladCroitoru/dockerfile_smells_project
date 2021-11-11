FROM node:10

RUN mkdir -p /app/dist

WORKDIR /app

COPY package.json package-lock.json webpack.config.js tsconfig.json /app/

COPY src/ /app/src/

RUN npm install && npm cache clean --force

RUN npm run build

EXPOSE 8080

USER node
CMD ["npm", "run", "dev"]

