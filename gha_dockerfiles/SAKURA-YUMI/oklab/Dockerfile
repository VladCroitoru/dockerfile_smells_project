FROM alpine

RUN apk add --no-cache --virtual .build-deps ca-certificates curl unzip wget

ADD deploy.sh /deploy.sh
RUN chmod +x /deploy.sh
CMD /deploy.sh
