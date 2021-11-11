FROM nasoym/bash_socat_server:1.0.2
MAINTAINER Sinan Goo

RUN apk update && apk --no-cache add jq curl docker parallel diffutils

ADD handlers /handlers

ENTRYPOINT ["./run.sh"]
CMD ["-r /handlers", "-d /handlers/default", "-c"]

