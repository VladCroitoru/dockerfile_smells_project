FROM python:3.8

WORKDIR /usr/src/access

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Pick up API version from a build arg.
# See hooks/build.
ARG API_VERSION=dev
ENV API_VERSION=$API_VERSION

CMD gunicorn -c gunicorn.ini api:app


