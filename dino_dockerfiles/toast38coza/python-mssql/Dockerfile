FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
	unixodbc \
	unixodbc-dev \
	tdsodbc
RUN apt-get install -y freetds-common freetds-bin freetds-dev
ADD odbcinst.ini /etc/
RUN pip install -U pip
RUN pip install pyodbc==3.0.10 django-pyodbc-azure
