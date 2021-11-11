FROM python:3.6

EXPOSE 8000

RUN apt-get update && \
    apt-get install -y libpq-dev python-dev gcc g++ libxslt-dev libtiff5-dev \
                       libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev \
                       libwebp-dev tcl8.6-dev tk8.6-dev python-tk
ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR /app

# Idem for requirements.txt
COPY requirements.txt /app

RUN pip install -r requirements.txt

# Then copy the rest of the app
COPY . /app

ENV DATABASE_URL ''
ENV DJANGO_SETTINGS_MODULE portailva.settings
ENV WSGI_APP portailva.wsgi
ENV APP_DEBUG False
ENV MAILGUN_API_KEY ''
ENV DEFAULT_FROM_EMAIL 'no-reply@example.com'
ENV SITE_URL 'http://portail.example.com'
ENV API_URL 'http://portail.example.com/api'
ENV SECRET_KEY '%8r$1anftcza)6)uth+ij(2o)si0)l^8o4=t!7^c_0_sz%1gkz'

VOLUME /app/staticfiles
VOLUME /app/mediafiles

RUN chmod +x /app/bash/run-prod.sh
CMD /app/bash/run-prod.sh