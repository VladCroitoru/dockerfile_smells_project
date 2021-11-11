FROM node:14.16.1-alpine as builder
RUN apk update
RUN apk add git
ADD ./ /var/www/bicineabbiamo/
WORKDIR /var/www/bicineabbiamo
RUN yarn --production --ignore-engines

FROM node:14.16.1-alpine
LABEL maintainer Massimiliano Cannarozzo <massi@massi.dev>
WORKDIR /var/www/bicineabbiamo
COPY --from=builder /var/www/bicineabbiamo .
ENV NODE_ENV=production
ENV PORT=80
EXPOSE 80
CMD ["yarn", "start"]
