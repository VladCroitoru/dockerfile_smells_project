FROM node:14-alpine

ENV PATH /app/node_modules/.bin:$PATH
ENV CHOKIDAR_USEPOLLING=true
WORKDIR /app
COPY package.json .
COPY yarn.lock .
RUN yarn install --frozen-lockfile
RUN npm rebuild node-sass
COPY . .

ENV HOST 0.0.0.0
EXPOSE 3000
CMD ["yarn", "dev"]
