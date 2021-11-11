#Inspired by https://codefresh.io/docs/docs/learn-by-example/nodejs/react/ and
#https://github.com/statisticsnorway/dapla-react-reference-app/blob/master/Dockerfile
FROM nginx:1-alpine

RUN apk add --no-cache nodejs yarn
RUN yarn global add @beam-australia/react-env

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY /build /usr/share/nginx/html
COPY .env docker-entrypoint.sh /var/

ENTRYPOINT ["sh", "/var/docker-entrypoint.sh"]

EXPOSE 8180

CMD ["nginx", "-g", "daemon off;"]
