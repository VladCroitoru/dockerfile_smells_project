FROM golang:alpine

WORKDIR /go/src/app
COPY . .

RUN go-wrapper download
RUN go-wrapper install

#Example osm server. Override this environment variable with a list of
#space-separated osm instances:
ENV OSMIM_OSM_SERVERS="http://demo.openspeedmonitor.org/"

EXPOSE 80

CMD ["go-wrapper", "run"]
