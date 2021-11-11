FROM python:3

EXPOSE 8080

# Setup environment, ARG are only available during the build.
ENV PYTHONUNBUFFERED 1
ARG SECRET_KEY=none
ARG ALLOWED_HOSTS=localhost
ARG DATABASE_URL=sqlite:///db.sqlite3

RUN apt-get update \
	&& apt-get -y install ruby-sass nginx \
	# Install pip2 for supervisor and supervisor-stdout \
	&& apt-get install -y python-pip \
	&& pip2 install supervisor supervisor-stdout \
	# Remove repo metadata to keep layer size down \
	&& rm -rf /var/lib/apt/lists/*

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY manage.py /app/
COPY finger /app/finger/
COPY fingerweb /app/fingerweb/
COPY services /app/services/
WORKDIR /app

RUN adduser --no-create-home --gecos FALSE --disabled-password finger \
	# Get rid of warnings \
	&& touch /app/.env \
	&& sed -i "s/XXX_BUILD_DATE_XXX/`date +'%F %T'`/" /app/fingerweb/settings.py \
	# compilestatic requires an database, hence migrate. \
	&& /app/manage.py migrate \
	# Compile static resources \
	&& /app/manage.py compilestatic \
	&& /app/manage.py collectstatic --noinput \
	# Clean up, make directories and fix permissions \
	&& rm /app/*.sqlite3 \
	&& rm /app/*.txt \
	&& mkdir /app/logs \
	&& chown -R finger:finger /app

ADD conf/nginx.conf /etc/nginx/nginx.conf
ADD conf/supervisord.conf /etc/supervisor/
ADD conf/supervisor/ /etc/supervisor/conf.d/

CMD ["supervisord", "-nc", "/etc/supervisor/supervisord.conf"]
