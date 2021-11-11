FROM python:3.8 AS builder
LABEL maintainer="dudola.daniel@itk.ppke.hu"

ENV LANG=C.UTF-8
ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT

RUN pip install pipenv

WORKDIR /build

COPY Pipfile Pipfile.lock ./

RUN PIP_USER=1 PYTHONUSERBASE=$PYROOT pipenv install --system --deploy

#                           .ÄÄÄ-.
#                          (___/\ \
#        ,                 (|^ ^ ) )    At this point, the dependencies
#       /(                _)_\=_/  (    are built in the builder container.
# ,..__/ `\          ____(_/_ ` \   )
#  `\    _/        _/---._/(_)_  `\ (   Copy dependencies to final image.
#    '--\ `-.__..-'    /.    (_), |  )
#        `._        ___\_____.'_| |__/
#           `~----"`   `-.........'
FROM python:3.8

ENV LANG=C.UTF-8

RUN dpkg --add-architecture i386 \
    && apt-get update -q \
    && apt-get install -y -q mariadb-server \
    && mkdir -p /usr/src/app \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install gunicorn

ENV PYROOT /pyroot
ENV PYTHONPATH $PYROOT/lib/python:$PATH
ENV PYTHONUSERBASE $PYROOT

COPY --from=builder $PYROOT/lib/ $PYROOT/lib/
COPY . /usr/src/app/psindb

WORKDIR /usr/src/app/psindb

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
CMD ["bash", "entrypoint.sh"]

EXPOSE 8000