FROM node:12

ENV PORT 3000
ADD . /ts-prisma-boilerplate

WORKDIR /ts-prisma-boilerplate
RUN yarn && yarn build

CMD ["node", "dist"]