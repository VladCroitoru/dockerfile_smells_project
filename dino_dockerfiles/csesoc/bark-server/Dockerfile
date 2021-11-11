FROM python:2

WORKDIR /app
VOLUME /app/data

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
      && apt-get install -y libldap2-dev libsasl2-dev slapd ldap-utils \
      && pip install pipenv

# Install dependencies into their own layer so they are cached between code changes
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . .

ENV ENV=production
EXPOSE 8080

CMD ["gunicorn", "-c", "gunicorn.py", "wsgi:app"]
