FROM golang:1.4-onbuild

ADD rawdns.json /etc/rawdns.json

CMD ["go-wrapper", "run", "/etc/rawdns.json"]
