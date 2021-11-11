FROM node:14-alpine
WORKDIR /usr/src/app

ENV VUE_APP_API_URL=/

RUN apk --update add git less openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

RUN git clone https://github.com/UWAMakers/access-frontend.git
RUN cd access-frontend && yarn && yarn build
RUN cd ../
RUN git clone https://github.com/UWAMakers/access-api.git
RUN mv ./access-api/* . 2> /dev/null; mv ./access-api/.* . 2> /dev/null; rmdir ./access-api
RUN yarn
RUN cp -r access-frontend/dist/* ./public
RUN rm -rf access-frontend

EXPOSE 3030
CMD ["yarn", "start"]

