FROM ubuntu:18.04  AS base
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y cmake gcc g++ git libsasl2-dev libssl-dev libsnappy-dev make pkg-config tar wget python3
RUN apt-get upgrade -y

RUN wget https://dl.google.com/go/go1.16.4.linux-amd64.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.4.linux-amd64.tar.gz 
RUN export PATH=\$PATH:/usr/local/go/bin
FROM base AS build
COPY --from=base /usr/local/go/ /usr/local/go/
ENV PATH="/usr/local/go/bin:${PATH}"
RUN go version

RUN mkdir /app
ADD . /app
WORKDIR /app/src
RUN go build -o main .
CMD ["/app/src/main"]