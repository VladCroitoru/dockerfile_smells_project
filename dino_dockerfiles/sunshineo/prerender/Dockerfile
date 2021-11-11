FROM node:6.3.1

ENV PORT 80
EXPOSE 80

ENV ENABLE_S3 false
ENV AWS_ACCESS_KEY_ID **replace*me**
ENV AWS_SECRET_ACCESS_KEY **replace*me**
ENV AWS_REGION **replace*me**
ENV S3_BUCKET_NAME **replace*me**

WORKDIR /prerender/

ADD package.json ./
RUN npm install

ADD lib ./lib
ADD index.js ./
ADD server.js ./

CMD ["node", "server.js"]