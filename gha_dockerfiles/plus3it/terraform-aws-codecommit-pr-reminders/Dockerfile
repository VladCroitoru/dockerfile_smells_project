FROM plus3it/tardigrade-ci:0.19.3

COPY ./src/requirements.txt /src/requirements.txt

RUN python -m pip install --no-cache-dir \
  -r /src/requirements.txt
