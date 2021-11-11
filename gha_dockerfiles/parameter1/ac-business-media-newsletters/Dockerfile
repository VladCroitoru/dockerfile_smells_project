FROM node:10.15 as build
WORKDIR /root
ENV NODE_ENV production
ARG TENANT

ADD package.json yarn.lock /root/
ADD packages /root/packages
ADD tenants/$TENANT /root/tenants/$TENANT
RUN yarn --production --pure-lockfile

WORKDIR /root/tenants/$TENANT

FROM node:10.15-alpine
ENV NODE_ENV production
ENV PORT 80
ARG TENANT
COPY --from=build /root /root
WORKDIR /root/tenants/$TENANT
ENTRYPOINT [ "node", "index.js" ]
