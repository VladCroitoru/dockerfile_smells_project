FROM node:10.24 as build
WORKDIR /root
ENV NODE_ENV production
ARG SITE

ADD package.json yarn.lock /root/
ADD packages /root/packages
ADD sites/$SITE /root/sites/$SITE
RUN yarn --production --pure-lockfile

WORKDIR /root/sites/$SITE
RUN node_modules/.bin/basecms-website build

FROM node:10.15-alpine
ENV NODE_ENV production
ENV PORT 80
ARG SITE
COPY --from=build /root /root
WORKDIR /root/sites/$SITE
ENTRYPOINT [ "node", "index.js" ]
