FROM ivotron/jq:1.5

RUN apk --no-cache add python bc py-yaml

ADD . /root/

WORKDIR /data

ENTRYPOINT ["/root/to_csv.py"]
