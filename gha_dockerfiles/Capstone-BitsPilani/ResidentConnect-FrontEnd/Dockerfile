FROM node:14.16.0-alpine as builder
LABEL version="1.0"
LABEL maintainer = ["agni1984@gmail.com"]

RUN mkdir /app


# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@4.0.3 -g --silent

# add app
COPY . ./

# start app
CMD ["npm", "start"]


#  FROM nginx
#  COPY --from=builder /app/build /usr/share/nginx/html

