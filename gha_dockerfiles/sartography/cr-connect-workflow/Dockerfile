FROM sartography/cr-connect-python-base

WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN set -xe \
  && pipenv install --dev \
  && apt-get remove -y gcc python3-dev libssl-dev \
  && apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/* \
  && useradd _gunicorn --no-create-home --user-group

COPY . /app/
WORKDIR /app
