FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN apt-get update \
	&& apt-get install -y postgresql-client-11\
	binutils\
	libproj-dev\
	gdal-bin\
	gettext\
	libgettextpo-dev

RUN pip install -U pip

RUN mkdir /code
WORKDIR /code

# Install the python dependencies that this project uses:
COPY requirements /code/requirements
RUN pip install -r requirements/dev.txt

COPY . /code/
