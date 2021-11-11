FROM alpine
MAINTAINER wuman

ENV WKDIR /workspace
RUN apk add --no-cache nodejs nodejs-npm
RUN npm install express
RUN mkdir ${WKDIR}
WORKDIR ${WKDIR}
COPY asset/app.js ${WKDIR}
EXPOSE 3000
ENTRYPOINT ["node","/workspace/app.js"]
