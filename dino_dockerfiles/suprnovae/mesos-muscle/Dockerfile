FROM garland/mesosphere-docker-mesos-master

RUN alias docker=docker -H /var/run/docker.sock

ENTRYPOINT ["mesos-slave"]
