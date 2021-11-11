FROM crossbario/crossbar:cpy3-18.3.1

ADD .crossbar/config.json /node/.crossbar/config.json

EXPOSE 8080

ENTRYPOINT ["crossbar", "start", "--cbdir", "/node/.crossbar"]
