FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /api_test
WORKDIR /api_test

# Install dependencies
ADD requirements.txt /api_test/
RUN pip install -r requirements.txt

# Copy source - TODO: Create .dockerignore
ADD . /api_test/

