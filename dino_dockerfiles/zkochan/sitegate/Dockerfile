FROM risingstack/alpine:3.3-v5.7.0-3.1.0

MAINTAINER Zoltan Kochan, zoltan.kochan@gmail.com

WORKDIR /src

# Install packages
COPY package.json /src/package.json
RUN npm install --production

# Make everything available for start
COPY . /src

EXPOSE 3000
CMD ["npm", "start"]
