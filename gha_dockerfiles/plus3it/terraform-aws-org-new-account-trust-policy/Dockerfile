FROM plus3it/tardigrade-ci:0.19.3

COPY ./lambda/src/requirements.txt /lambda/src/requirements.txt
COPY ./lambda/tests/requirements_dev.txt /lambda/tests/requirements_dev.txt
COPY ./tests/requirements_test.txt /tests/requirements_test.txt
COPY ./requirements_common.txt /requirements_common.txt

RUN python -m pip install --no-cache-dir \
    -r /lambda/src/requirements.txt \
    -r /lambda/tests/requirements_dev.txt \
    -r /tests/requirements_test.txt
