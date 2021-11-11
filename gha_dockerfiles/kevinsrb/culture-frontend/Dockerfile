FROM node
RUN apt-get update -qq && apt-get install -y build-essential
WORKDIR /usr/react_app
ENV PATH /usr/react_app/node_modules/.bin:$PATH
COPY package*.json ./
COPY yarn.lock ./
RUN yarn add node-sass
RUN yarn
COPY . .
COPY .env .
CMD ["yarn", "start"]
EXPOSE 3000