FROM ccnmtl/django.base
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD wheelhouse /wheelhouse
RUN /ve/bin/pip install --no-index -f /wheelhouse -r /wheelhouse/requirements.txt \
    && rm -rf /wheelhouse && touch /ve/sentinal
WORKDIR /app
COPY . /app/
RUN VE=/ve/ MANAGE="/ve/bin/python manage.py" make
EXPOSE 8000
ADD docker-run.sh /run.sh
ENV APP ccdb
ENTRYPOINT ["/run.sh"]
CMD ["run"]
