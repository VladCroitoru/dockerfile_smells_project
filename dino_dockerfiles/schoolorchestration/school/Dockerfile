FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code/ansible
WORKDIR /code

ADD requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY *.yml /code/
COPY ./roles/ /etc/ansible/roles/
COPY ./group_vars /code/group_vars
COPY ./includes /code/includes
COPY ./scripts /code/scripts
COPY ./inventory/digital_ocean.py /etc/ansible/inventory/digital_ocean.py
COPY ./library/ /etc/ansible/library/
