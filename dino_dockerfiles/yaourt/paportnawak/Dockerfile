FROM alpine:3.6 AS build
RUN apk update && \
    apk add --update alpine-sdk
RUN mkdir /app
WORKDIR /app
COPY main.c  /app
RUN mkdir bin
RUN gcc -Wall main.c -o bin/hello

FROM alpine:3.6
COPY --from=build /app/bin/hello /app/hello
CMD /app/hello