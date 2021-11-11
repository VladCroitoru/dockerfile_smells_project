FROM python:2.7-alpine3.7

# Add shell script
COPY addition.py /

RUN pip install web.py redis

CMD ["python", "/addition.py"]