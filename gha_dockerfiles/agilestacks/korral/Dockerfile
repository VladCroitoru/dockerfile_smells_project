FROM node:12.18-alpine3.12

LABEL maintainer="Arkadi Shishlov <arkadi@agilestacks.com>"

RUN mkdir /app
WORKDIR /app

ENV NODE_ENV $NODE_ENV
COPY package.json package-lock.json LICENSE README.md /app/
RUN npm -q install --only=prod && npm -q cache clean --force
COPY korral /app/
COPY src/ /app/src/

ENTRYPOINT [ "/app/korral" ]
CMD ["export", "--check"]
