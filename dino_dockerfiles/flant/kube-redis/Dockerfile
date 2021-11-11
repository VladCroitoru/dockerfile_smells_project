FROM redis:3.2
MAINTAINER Flant OJSC <vasily.marmer@flant.ru>

RUN mkdir -p /etc/pod-info
RUN touch /etc/pod-info/labels
RUN apt-get update && apt-get install -y jq curl

WORKDIR /app
ADD . /app
RUN chmod +x /app/sidecar.sh
CMD /app/sidecar.sh
