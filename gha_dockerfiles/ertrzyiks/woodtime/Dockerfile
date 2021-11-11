FROM node:16-alpine3.11

ENV PORT=80 NODE_ENV=production
EXPOSE 80
COPY . /app
WORKDIR /app
RUN yarn install --immutable-cache --immutable

ENTRYPOINT ["yarn"]
CMD ["workspace", "api", "start:prod"]
