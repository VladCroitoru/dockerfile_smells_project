FROM python:3.6-alpine AS compile-image
RUN apk --no-cache add gcc musl-dev
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt --user --ignore-installed --upgrade

FROM python:3.6-alpine AS build-image
COPY --from=compile-image /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . /app
CMD python /app/led_sequence/main.py