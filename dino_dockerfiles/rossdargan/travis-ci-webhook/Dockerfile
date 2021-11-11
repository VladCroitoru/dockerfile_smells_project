FROM node:7.10.0
# replace this with your application's default port
EXPOSE 7777
COPY index.js /usr/src/app/
COPY package.json /usr/src/app
WORKDIR /usr/src/app/
RUN npm install
ENV WEBHOOK_PATH /travis
HEALTHCHECK CMD curl --fail http://localhost:7777/check || exit 1
CMD ["node","index.js"]
