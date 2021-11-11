FROM python:2-slim

WORKDIR /ns

ADD . /ns

RUN pip install -r requirements.txt

EXPOSE 9090

CMD ["python", "ns.py"]
