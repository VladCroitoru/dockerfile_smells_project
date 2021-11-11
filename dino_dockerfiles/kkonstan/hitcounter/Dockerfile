FROM python:2.7

RUN pip install -q flask redis
COPY hitcounter.py .

CMD python hitcounter.py

EXPOSE 80
