FROM alpine:3.7 AS build

RUN apk add --no-cache gcc g++ musl-dev make
RUN wget http://www.live555.com/liveMedia/public/live555-latest.tar.gz
RUN tar -xzf live555-latest.tar.gz
WORKDIR live
RUN ./genMakefiles linux
RUN make
RUN make install

FROM alpine:3.7
RUN apk add --no-cache libstdc++
COPY --from=build /live /bin/live
WORKDIR /bin/live
