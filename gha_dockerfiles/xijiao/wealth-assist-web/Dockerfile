# pull official base image
FROM node:16-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

COPY . ./
RUN yarn add global expo-cli && yarn 

# start app
CMD ["expo", "start", "--web"]
