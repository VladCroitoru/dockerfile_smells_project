FROM node:8.12-alpine

RUN adduser -S www-data

RUN apk add --no-cache make gcc g++ python bash git curl ca-certificates
RUN sed 's|mozilla\/AddTrust_External_Root.crt|#mozilla\/AddTrust_External_Root.crt|g' -i /etc/ca-certificates.conf
RUN update-ca-certificates -f -v

WORKDIR /var/www
ADD . .
RUN yarn && yarn cache clean

EXPOSE 19199

CMD ["npm", "start"]
