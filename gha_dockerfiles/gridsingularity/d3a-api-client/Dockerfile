FROM python:3.8

ADD . /app

WORKDIR /app

# TODO remove in the frame of D3ASIM-3093:
RUN pip install -U pip==20.2.4

RUN pip install -e .

ENTRYPOINT ["python"]
