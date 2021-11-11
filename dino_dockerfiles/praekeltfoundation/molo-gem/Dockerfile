ARG MOLO_VERSION=7
FROM praekeltfoundation/molo-bootstrap:${MOLO_VERSION}-onbuild

COPY site-redir-www-nonwww.conf /etc/nginx/conf.d/site-redir-www-nonwww.conf

ENV DJANGO_SETTINGS_MODULE=gem.settings.docker \
    CELERY_APP=gem

RUN LANGUAGE_CODE=en SECRET_KEY=compilemessages-key django-admin compilemessages && \
    SECRET_KEY=collectstatic-key django-admin collectstatic --noinput && \
    SECRET_KEY=compress-key django-admin compress

CMD ["gem.wsgi:application", "--timeout", "1800"]
