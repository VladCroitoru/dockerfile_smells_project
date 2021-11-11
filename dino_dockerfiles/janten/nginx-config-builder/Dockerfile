FROM python:3.6-alpine

RUN pip install jinja2
RUN mkdir /builder
WORKDIR /builder
ADD nginx.template /builder/nginx.template
ADD build.py /builder/build.py

CMD ["python3", "/builder/build.py"]