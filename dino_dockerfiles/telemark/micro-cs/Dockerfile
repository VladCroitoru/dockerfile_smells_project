FROM mhart/alpine-node:10 as base
WORKDIR /usr/src
COPY package.json package-lock.json /usr/src/
RUN npm i --production
COPY . .

FROM mhart/alpine-node:base-10
WORKDIR /usr/src
COPY --from=base /usr/src .
ENV SERVER_PORT 3000
ENV CS_URL http://portalcode.t-fk.no/scripts/customer.exe?_sf=0&action=safeParse&includeId=ticket-endpoint
ENV CS_KEY asecretpassword
ENV tokenKey Gibberish, jibberish, jibber-jabber and gobbledygook
EXPOSE ${SERVER_PORT}
CMD ["node", "./node_modules/.bin/micro"]