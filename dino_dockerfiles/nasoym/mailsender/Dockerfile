FROM nasoym/bash_socat_server:1.0.2
MAINTAINER Sinan Goo

RUN apk update && apk --no-cache add heirloom-mailx

ADD attach /handlers/attach
ADD send /handlers/send

ENTRYPOINT ["./run.sh"]
CMD ["-r /handlers", "-d /handlers/default", "-c"]

