from mysql

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install awscli
RUN mkdir -p /backup/data

ADD run /backup/run
WORKDIR /backup

ENTRYPOINT ["./run"]
CMD ['backup']
