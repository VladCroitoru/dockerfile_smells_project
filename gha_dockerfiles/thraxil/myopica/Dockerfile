FROM thraxil/django.base:2020-09-26-83678bbd1abe
COPY requirements.txt /app/requirements.txt
RUN /ve/bin/pip3 install -r /app/requirements.txt && touch /ve/sentinal
WORKDIR /app
COPY . /app/
RUN VE=/ve/ MANAGE="/ve/bin/python3 manage.py" NODE_MODULES=/node/node_modules make test
EXPOSE 8000
ENV APP myopica
ENTRYPOINT ["/run.sh"]
CMD ["run"]
