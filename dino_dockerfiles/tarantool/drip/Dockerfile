FROM python:2

COPY . /opt/drip

RUN pip install -r /opt/drip/requirements.txt

WORKDIR /opt/drip

ENV DRIP_DOCKER_SOCKET=/var/run/docker.sock \
    DRIP_ROUTE_TAG=1 \
    DRIP_METRIC=1 \
    DRIP_NEXT_HOP=127.0.0.1 \
    DRIP_AUTH_TYPE=md5 \
    DRIP_NEIGHBOR=127.0.0.1 \
    DRIP_NETWORKS=bridge

CMD python drip.py \
    --route-tag $DRIP_ROUTE_TAG \
    --metric $DRIP_METRIC \
    --next-hop $DRIP_NEXT_HOP \
    --auth-type $DRIP_AUTH_TYPE \
    --neighbor $DRIP_NEIGHBOR \
    $DRIP_NETWORKS
