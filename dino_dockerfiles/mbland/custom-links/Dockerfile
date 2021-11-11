FROM node:10.0.0-alpine
MAINTAINER Mike Bland "mbland@acm.org"
WORKDIR /opt/custom-links
COPY package.json package-lock.json ./
RUN npm install --production
COPY . ./
RUN apk add --no-cache bash curl git jq && ./go null
EXPOSE 3000
CMD [ "/opt/custom-links/go", "serve", "/etc/custom-links.conf" ]
