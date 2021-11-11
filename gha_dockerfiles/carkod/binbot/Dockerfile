FROM python:3.8
RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3-dev nginx python-setuptools
COPY /web/build/ /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/sites-enabled/default
COPY Pipfile Pipfile.lock start ./
RUN rm -rf .env.local
RUN chmod +x start
RUN pip install --upgrade pip && pip install pipenv gunicorn
RUN pipenv install --system --deploy --ignore-pipfile
COPY api api
CMD ["./start"]

STOPSIGNAL SIGTERM
EXPOSE 80 8006
