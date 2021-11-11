FROM alpine:3.6
RUN apk add --update nodejs nodejs-npm && npm install npm@latest -g
COPY package.json .
#install production dependencies also sets NODE_ENV="production" 
RUN npm install --production
COPY ./dist ./dist
COPY ./courses ./courses
COPY server.js .
EXPOSE 3000
CMD NODE_ENV="production" node server.js