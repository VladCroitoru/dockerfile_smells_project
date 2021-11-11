FROM node:alpine
LABEL AUTHOR "Dave Sperling <dsperling@smithmicro.com>"

RUN npm install uglify-js -g

ENTRYPOINT [ "uglifyjs" ]
