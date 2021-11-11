FROM node:14.18.0-alpine

ENV USER node
ENV USER_ID 1000
ENV GROUP node
ENV NAME hocs-frontend

RUN mkdir -p /app && \
    chown -R ${USER}:${GROUP} /app

WORKDIR /app
COPY . /app
COPY /build /app/build
RUN npm  --loglevel warn install --production --no-optional

USER ${USER_ID}

EXPOSE 8080

CMD npm start
