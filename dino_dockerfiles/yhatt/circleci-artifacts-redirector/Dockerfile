FROM node:6.11.3-alpine
LABEL maintainer "Yuki Hattori <yukihattori1116@gmail.com>"

ENV CIRCLECI_ARTIFACTS_REDIRECTOR_PORT 80
WORKDIR /app
COPY index.js package.json yarn.lock /app/
RUN yarn install --production

EXPOSE 80
CMD ["node", "index.js"]
