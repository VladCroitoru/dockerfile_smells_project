from rochacon/golang
maintainer Rodrigo Chacon <rochacon@gmail.com>
run apt-get install -y git && apt-get clean
env GOPATH /usr/local
run go get github.com/rochacon/s3stub
run mkdir -p /srv/s3stub
cmd /usr/local/bin/s3stub -r /srv/s3stub -b :80
expose 80
