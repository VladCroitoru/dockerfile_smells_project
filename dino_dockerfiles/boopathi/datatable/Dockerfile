from boopathi/go:latest
maintainer  Boopathi Rajaa <me@boopathi.in>

run go get github.com/boopathi/datatable

workdir /go/src/github.com/boopathi/datatable
add . /go/src/github.com/boopathi/datatable

# Install application
run go get
run go build

# Expose port
expose 4200

entrypoint ./datatable -dbhost $DB_PORT_27017_TCP_ADDR -dbport $DB_PORT_27017_TCP_PORT
