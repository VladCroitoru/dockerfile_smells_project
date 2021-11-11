FROM node:12
WORKDIR /app
COPY ./speedtest-rest-api/dist/apps/speed-test .
ENV PORT=3333
EXPOSE ${PORT}
RUN npm install --production
RUN npm install reflect-metadata tslib
CMD node ./main.js