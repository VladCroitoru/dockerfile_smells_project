FROM python:3.6

WORKDIR /app

RUN apt-get update && apt-get install -y python-wand

RUN pip install requests cssutils bs4 wand pyopenssl

RUN echo 0 > updatefile
RUN mkdir downloads/

ADD . /app/

CMD ["python", "/app/main.py"]
