FROM alpine:3.11.5

RUN apk --update add python3 py3-twisted
RUN adduser -u 50000 -D -H scrabble
COPY server /server/
RUN chown scrabble /server/log /server/partie
USER scrabble
EXPOSE 12345
WORKDIR /server
CMD ./go_server
