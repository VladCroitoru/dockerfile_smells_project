FROM node:14-alpine as builder

ARG GATSBY_API_BASE_URL=http://localhost:4000
ARG GATSBY_BASE_URL=https://invoicesapp.peraltafedericomanuel.com

ENV GATSBY_API_BASE_URL=$GATSBY_API_BASE_URL
ENV GATSBY_BASE_URL=$GATSBY_BASE_URL

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

RUN yarn --pure-lockfile

COPY . .

RUN npm run build

FROM amazon/aws-cli

COPY --from=builder /usr/src/app .

ENTRYPOINT []

RUN chmod +x ./scripts/run.sh

CMD ["./scripts/run.sh"]