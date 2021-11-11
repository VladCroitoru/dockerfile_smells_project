FROM python:3.6 as packages
RUN pip install pipenv
COPY Pipfile Pipfile.lock /tmp/
RUN cd /tmp && pipenv lock --requirements --dev > all-requirements.txt
RUN pip wheel --wheel-dir=/tmp/all-wheelhouse -r /tmp/all-requirements.txt

RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip wheel --wheel-dir=/tmp/wheelhouse -r /tmp/requirements.txt

FROM python:3.6 as testing
COPY --from=packages /tmp/all-requirements.txt /tmp/requirements.txt
COPY --from=packages /tmp/all-wheelhouse /tmp/wheelhouse

RUN pip install --no-index --find-links=/tmp/wheelhouse -r /tmp/requirements.txt \
    && mkdir -p testing/reports

COPY . /testing/
WORKDIR /testing

FROM python:3.6-alpine3.7
COPY --from=packages /tmp/requirements.txt /tmp/requirements.txt
COPY --from=packages /tmp/wheelhouse /tmp/wheelhouse

RUN echo "manylinux1_compatible = True" >> /usr/local/lib/python3.6/site-packages/_manylinux.py \
    && pip install --no-index --find-links=/tmp/wheelhouse -r /tmp/requirements.txt \
    && rm -rf /tmp/wheelhouse

WORKDIR /usr/src/app
COPY . .