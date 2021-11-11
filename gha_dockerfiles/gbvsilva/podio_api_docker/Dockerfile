FROM python:3.8-alpine

WORKDIR /opt/podio_api

RUN apk update
RUN apk add --no-cache py3-pip python3-dev git

RUN git clone https://github.com/podio/podio-py.git
RUN cd podio-py && python setup.py install

RUN pip install --no-cache-dir mysql-connector-python requests

ADD podio_api.py /opt/podio_api/podio_api.py

RUN apk del git && rm -rf /var/cache/apk/*

CMD ["/opt/podio_api/podio_api.py"]
ENTRYPOINT ["python3"]