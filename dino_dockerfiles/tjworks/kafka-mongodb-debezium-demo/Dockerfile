from python:2.7-alpine

USER root
RUN pip install kafka-python
RUN pip install pymongo

COPY ./consumer.py /root

ENTRYPOINT ["python", "/root/consumer.py"]