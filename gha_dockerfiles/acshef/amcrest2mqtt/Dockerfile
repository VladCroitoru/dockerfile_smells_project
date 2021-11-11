FROM python:3.9-alpine as base
FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /
RUN pip install --no-warn-script-location --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY amcrest2mqtt /amcrest2mqtt
COPY app.py /
WORKDIR /

CMD [ "python", "-u", "app.py" ]
