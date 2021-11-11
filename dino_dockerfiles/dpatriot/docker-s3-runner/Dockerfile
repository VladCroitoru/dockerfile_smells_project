FROM dpatriot/docker-awscli-java8
MAINTAINER Shago Vyacheslav <v.shago@corpwebgames.com>

ADD run.sh /opt/
RUN chmod +x /opt/run.sh

# Define working directory.
WORKDIR /opt

ENTRYPOINT ["./run.sh"]

CMD [""]
