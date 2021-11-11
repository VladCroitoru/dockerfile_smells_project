FROM python:alpine
MAINTAINER Marco Sousa <marcomsousa+docker @ gmail.com>

RUN pip install flask

ADD hello.py /tmp/hello.py

EXPOSE 5000

CMD ["python","/tmp/hello.py"]
