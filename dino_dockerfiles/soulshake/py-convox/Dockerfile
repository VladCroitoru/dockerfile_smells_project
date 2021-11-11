FROM python:2.7
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN pip install --upgrade pip

WORKDIR /src/
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . /src/
RUN pip install .
ENTRYPOINT ["py-convox"]
