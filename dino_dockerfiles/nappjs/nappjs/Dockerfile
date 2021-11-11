FROM node:8.9.0-alpine

EXPOSE 80
ENV DATABASE_URL sqlite://:memory:
ENV REST_API_PATH /

WORKDIR /code

RUN apk --update add gcc g++ make python git && yarn global add nappjs

ENTRYPOINT [ ]
CMD [ "nappjs", "start" ] 