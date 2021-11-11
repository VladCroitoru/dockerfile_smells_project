FROM python:3.6-alpine as basis

RUN apk update && apk --no-cache add postgresql-dev gcc musl-dev

RUN pip install cython

RUN mkdir -p /usr/src/app/requirements
WORKDIR /usr/src/app

RUN python3 -m venv /usr/src/venv
ENV VIRTUAL_ENV="/usr/src/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD . /usr/src/app
RUN pip install -r requirements/requirements.txt

FROM python:3.6-alpine

COPY --from=basis /usr/src/venv /usr/src/venv
COPY --from=basis /usr/src/app /usr/src/app

RUN apk update && apk --no-cache add libpq

ENV VIRTUAL_ENV="/usr/src/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH="/usr/src/app"
WORKDIR /usr/src/app

EXPOSE 5000

CMD ["sh", "./docker/entrypoint.sh"]
