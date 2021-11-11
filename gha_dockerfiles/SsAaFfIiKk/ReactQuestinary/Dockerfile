FROM alpine

#RUN apk add --update nodejs nodejs-npm
RUN apk add --update nodejs npm
# RUN npm install -g http-server
WORKDIR /app
# COPY . /app/
# RUN cd /app && npm install --pure-lockfile
COPY . .
RUN npm install
RUN npm run build
RUN npm install -g serve
# RUN serve -s build
CMD serve -l 7373 -s build
# EXPOSE 7373
# ENV HOST 0.0.0.0
# CMD npm start