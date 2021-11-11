FROM python:2.7.14-alpine3.7

RUN pip install web.py redis

# Add shell script
COPY addition.py /

CMD ["python", "/addition.py"]

