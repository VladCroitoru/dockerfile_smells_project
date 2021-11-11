FROM golang:1.13-stretch as builder

# build go-cfdg
WORKDIR /app/user
COPY . /app/user
RUN go build -o go-cfdg


FROM heroku/heroku:18

# install dependencies
RUN apt-get update \
	&& apt-get -y --no-install-recommends install libpng-dev\
	&& rm -rf /var/cache/apt/archives/*.deb

COPY . /app/user
COPY --from=builder /app/user/go-cfdg /app/user

WORKDIR /app/user
RUN cp -p cfdg-v3.2.2 cfdg \
	&& chmod +x cfdg \
	&& mkdir -p /app/usr/local/bin \
	&& cp cfdg /app/usr/local/bin
ENV PATH /app/usr/local/bin:$PATH

ENV PORT 3000
EXPOSE 3000

CMD ./go-cfdg