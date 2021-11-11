FROM node:16.9-alpine3.14
RUN apk add python2
RUN apk add build-base

#RUN addgroup app && adduser -S -G app app
#USER app

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 3001
CMD ["npm", "start"]

##RUN addgroup app && adduser -S -G app app
##USER app
#RUN mkdir -p /app/node_modules
#
#WORKDIR /app
#COPY package*.json ./
#
#
#
##RUN addgroup app && adduser -S -G app app
##USER app
##USER app
#RUN npm install
##COPY --chown=app:app . .
#COPY . .
#
#RUN npm run build
#
#CMD ["npm", "start"]
#
#
#
#
##EXPOSE 3001
##
##CMD ["npm", "run", "start"]
#
#
#
