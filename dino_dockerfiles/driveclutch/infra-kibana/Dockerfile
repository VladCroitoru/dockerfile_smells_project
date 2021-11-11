FROM kibana:4.5
MAINTAINER david@driveclutch.com

RUN apt-get update && apt-get install -y netcat

COPY kibana.yml /opt/kibana/config/
COPY entrypoint.sh /entrypoint.sh

RUN kibana plugin --install elastic/sense

CMD ["/entrypoint.sh"]
