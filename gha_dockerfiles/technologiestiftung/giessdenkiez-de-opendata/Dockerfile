# use Python version 3.8
FROM python:3.8.1-slim-buster as base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

FROM base as builder

# Install pip requirements
COPY requirements.txt /app/
RUN cd /app/ && python -m pip install --no-warn-script-location --prefix=/install -r requirements.txt

FROM base as app
COPY --from=builder /install /usr/local

COPY . /app/

# run script
CMD ["python", "/app/main.py"]
