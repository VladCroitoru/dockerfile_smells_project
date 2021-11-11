FROM alpine:edge
RUN apk update
RUN apk add g++ gcc make cmake git bash
COPY glob.patch .
RUN patch -p0 < glob.patch
RUN rm glob.patch
RUN mkdir /app
WORKDIR /app/
