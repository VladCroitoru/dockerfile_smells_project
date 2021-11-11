FROM quay.io/ibmgaragecloud/node:lts-stretch as build
WORKDIR /app
COPY . .
RUN npm install
## Change npm build to npm ci, to install the same version from package
RUN npm ci
EXPOSE 3000
CMD [ "npm", "start" ]
