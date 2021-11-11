FROM ccnmtl/django.base
ADD wheelhouse /wheelhouse
RUN /ve/bin/pip install --no-index -f /wheelhouse -r /wheelhouse/requirements.txt
WORKDIR /app
COPY . /app/
RUN /ve/bin/flake8 /app/capsim/ --max-complexity=10
RUN /ve/bin/python manage.py test
EXPOSE 8000
ADD docker-run.sh /run.sh
ENV APP capsim
ENTRYPOINT ["/run.sh"]
CMD ["run"]
