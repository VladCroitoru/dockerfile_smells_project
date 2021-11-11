FROM ubuntu:latest

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  python \
  python-setuptools \
  python-pip \
  python-dev \
  build-essential \
  git \
  vim

RUN mkdir webhook

ADD . webhook/

WORKDIR webhook

RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["./start.sh"]
