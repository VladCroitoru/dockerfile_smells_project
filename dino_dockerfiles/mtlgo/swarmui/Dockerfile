FROM mhart/alpine-node

WORKDIR /src
ADD . .

# for native dependencies, and extra tools
# RUN apk add --no-cache make gcc g++ python
RUN apk add --no-cache git

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]