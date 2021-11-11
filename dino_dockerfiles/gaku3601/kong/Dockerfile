FROM kong:0.13.1-alpine
RUN apk update && apk upgrade && apk add postgresql-client
ADD ./start.sh /start.sh
CMD sh /start.sh
