FROM python:3.8
ENV PYTHONUNBUFFERED 0

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
RUN pip install -e .[development]

RUN mkdir /tox
ENV TOX_WORK_DIR='/tox'
