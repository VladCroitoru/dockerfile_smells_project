FROM kkarczmarczyk/node-yarn as build-env

ADD ./ /work

WORKDIR /work

RUN yarn install

RUN yarn build

FROM nginx:alpine

COPY --from=build-env /work/bundle/* /usr/share/nginx/html/
