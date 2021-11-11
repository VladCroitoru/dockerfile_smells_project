FROM python:2.7
MAINTAINER Mike Dougherty <mike.dougherty@gmail.com>

WORKDIR /usr/src/app
ENTRYPOINT ["/usr/local/bin/pydonethis"]

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

USER nobody
