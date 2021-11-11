FROM node:6.10-alpine
COPY upload-to-s3.js /usr/bin/
RUN apk update && apk add --no-cache bash zip && chmod 755 /usr/bin/upload-to-s3.js
