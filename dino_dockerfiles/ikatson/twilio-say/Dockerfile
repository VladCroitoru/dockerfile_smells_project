FROM ubuntu:14.04

RUN apt-get update && apt-get install -y --no-install-recommends python-pip

ADD ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD ./ /src/

CMD ["python", "/src/main.py"]
