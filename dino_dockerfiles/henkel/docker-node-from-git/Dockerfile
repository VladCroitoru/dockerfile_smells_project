FROM node:alpine

RUN apk add --update bash git openssh-client && rm -rf /var/cache/apk/*
RUN yarn global add serve

USER node
WORKDIR /home/node
COPY launch.sh /home/node

ENTRYPOINT [ "./launch.sh" ]
CMD [ "yarn start" ]
