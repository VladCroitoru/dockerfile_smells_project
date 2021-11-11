FROM node:10-alpine as build
COPY . /src
WORKDIR /src
RUN yarn && yarn build
RUN ls -lag

FROM nginx:stable-alpine
COPY --from=build /src/build/ /usr/share/nginx/html
COPY --from=build /src/dbdoc/ /usr/share/nginx/html/dbdoc
CMD ["nginx", "-g", "daemon off;"]
