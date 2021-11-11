FROM node:14-alpine

ENV NODE_ENV production
ENV PORT 5000

COPY --chown=node:node ./projects/playground/public /home/node/app

WORKDIR /home/node/app

RUN yarn global add serve

USER node

EXPOSE 5000

CMD ["serve", "-l", "5000"]
