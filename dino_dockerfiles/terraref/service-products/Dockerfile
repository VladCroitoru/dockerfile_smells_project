FROM python:2.7
MAINTAINER Jeff Terstriep <jefft@illinois.edu>

RUN apt-get update && \
    apt-get install -y libgdal-dev

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
RUN pip install -e .

ENV FLASK_APP plot_service/api2.py
ENV CLOWDER_URL https://terraref.ncsa.illinois.edu/clowder
ENV SERVICE_PORT 8080
ENV SERVICE_HOST 0.0.0.0

EXPOSE 8080

CMD flask run -h ${SERVICE_HOST} -p ${SERVICE_PORT}
