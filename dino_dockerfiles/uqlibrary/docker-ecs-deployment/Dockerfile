FROM uqlibrary/centos:210511

RUN \
 curl -o /root/ecs-deployment https://raw.githubusercontent.com/uqlibrary/docker-ecs-deployment/master/ecs-deployment && \
 chmod a+x /root/ecs-deployment

WORKDIR /root

ENTRYPOINT ["/root/ecs-deployment"]
