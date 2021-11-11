# Copyright 2020 Hathor Labs
# This software is provided ‘as-is’, without any express or implied
# warranty. In no event will the authors be held liable for any damages
# arising from the use of this software.
# This software cannot be redistributed unless explicitly agreed in writing with the authors.

FROM node:14 AS builder

COPY package.json /app/

RUN cd /app && npm install

COPY . /app/

RUN cd /app && npm run build

FROM node:14-alpine3.13

COPY --from=builder /app/dist/ /app/
COPY --from=builder /app/package.json /app/

RUN cd /app && npm install --production

CMD node /app/index.js
