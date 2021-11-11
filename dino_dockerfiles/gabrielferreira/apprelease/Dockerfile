FROM python:2.7

RUN mkdir -p /var/www/html
WORKDIR /var/www/html
COPY requirements.txt /var/www/html/

RUN apt-get update -y \
	&& apt-get install -y git \
		mysql-client \
		libmysqlclient-dev \
		python-dev \
		sqlite3 \
		gettext \
		gcc \
		postgresql-client \
		libpq-dev \
		--no-install-recommends \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir -r requirements.txt

COPY . /var/www/html/

VOLUME /var/www/html
EXPOSE 80
EXPOSE 443
EXPOSE 8080
WORKDIR /var/www/html
ONBUILD RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
