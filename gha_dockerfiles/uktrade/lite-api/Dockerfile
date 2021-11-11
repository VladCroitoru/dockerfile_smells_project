FROM python:3.7-slim
WORKDIR /app
RUN apt-get update --fix-missing
RUN apt-get install -y libpq-dev gcc \
  build-essential python3-dev python3-pip python3-setuptools python3-wheel \
  python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
  libffi-dev shared-mime-info swig
RUN pip3 install pipenv
ADD Pipfile* /app/
RUN pipenv install --dev --system --deploy
RUN pip3 install endesive==1.5.9
ADD . /app
