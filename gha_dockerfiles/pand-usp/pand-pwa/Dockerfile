FROM node:14

WORKDIR /opt/app

ENV HOST=0.0.0.0
ENV PORT=8080

COPY . ./
RUN yarn install

ENTRYPOINT [ "yarn", "dev" ]

