FROM python:alpine

RUN pip install boto3
USER nobody
ENTRYPOINT ["/route53dynip.py"]
ENV PYTHONUNBUFFERED TRUE
COPY route53dynip.py /
