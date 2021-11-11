FROM mongo:3.6

RUN apt-get update && apt-get install -y python3-dev

COPY bootstrap.sh /bootstrap.sh
COPY mongodCodeGen.py /mongodCodeGen.py

WORKDIR /

ENTRYPOINT [ "/bootstrap.sh" ]

CMD [ ]
