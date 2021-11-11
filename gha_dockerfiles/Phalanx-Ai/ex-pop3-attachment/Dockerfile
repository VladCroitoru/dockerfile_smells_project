FROM quay.io/keboola/docker-custom-python:latest

COPY . /code/

ENV PYTHONIOENCODING utf-8

COPY . /code/

RUN pip install flake8
RUN pip install -r /code/requirements.txt

WORKDIR /data/

CMD ["python", "-u", "/code/main.py"]
