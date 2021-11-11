FROM python:3-slim
RUN apt-get update && apt-get --force-yes install -y vim gcc && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /warning

ADD . /warning

RUN pip install -r requirements.txt

EXPOSE 9090

CMD ["python", "warning.py"]
