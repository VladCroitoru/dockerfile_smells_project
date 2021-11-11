FROM mhart/alpine-node:15 as build

ARG SITE=boilerplate

ARG ROLE

ARG ENV_MODE
ENV ENV_MODE $ENV_MODE

ARG DATABASE_URL
ENV DATABASE_URL $DATABASE_URL

ARG SUDO_PASSWORD
ENV SUDO_PASSWORD $SUDO_PASSWORD

# ARG endpoint
# ENV endpoint $endpoint

# ARG PUBLIC_URL
# ENV PUBLIC_URL $PUBLIC_URL

RUN apk add bash 
RUN apk add mc 
RUN apk add curl 
RUN apk add python2
RUN apk add python3
RUN apk add make 
RUN apk add g++
RUN apk add git 

# RUN apk add --upgrade --no-cache vips-dev build-base \
#   --repository https://alpine.global.ssl.fastly.net/alpine/v3.10/community/

WORKDIR /www/${SITE}/

COPY ./ .

# Установку зависимостей нельзя переносить в entrypoint,
# потому что тот скрипт срабатывает уже тогда, когда контейнер создан и заменен имеющийся (если уже был запущен)
RUN yarn install --ignore-engines

# Deploy prisma migrations into database
RUN yarn prisma:deploy

RUN yarn generate
RUN yarn generate:types

RUN if [ "$ENV_MODE" = "production" ] ; then yarn build ; fi
