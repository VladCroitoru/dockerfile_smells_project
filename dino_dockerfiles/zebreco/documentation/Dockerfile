FROM outeredge/edge-docker-php:7.1.5

ENV APPLICATION_ENV dev

RUN pip install mkdocs mkdocs-material pygments pymdown-extensions

COPY . /var/www/

RUN mv mkdocs.conf /etc/supervisor/conf.d/ && mkdocs build

CMD ["/var/www/run.sh"]
