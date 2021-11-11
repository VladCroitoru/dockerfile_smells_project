# pull official base image
FROM node:14.17-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
# ENV PATH /app/node_modules/.bin:$PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY yarn.lock ./
COPY package*.json ./

RUN yarn
RUN yarn add global react-scripts@4.0.3
# RUN npm run start

# add app
COPY . .

EXPOSE 80

# start app
CMD ["yarn", "start"]
