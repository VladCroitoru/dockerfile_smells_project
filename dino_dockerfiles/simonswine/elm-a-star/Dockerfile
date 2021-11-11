FROM node:9.2.0

WORKDIR /app/

RUN npm install create-elm-app@1.9.1
ENV PATH=/app/node_modules/.bin:$PATH

COPY elm-package.json .
RUN elm-app install -y

COPY public ./public
COPY src ./src
RUN elm-app build

FROM nginx:1.13.7
COPY --from=0 /app/build /usr/share/nginx/html
