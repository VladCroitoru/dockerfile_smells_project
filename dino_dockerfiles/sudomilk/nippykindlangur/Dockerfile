FROM python:3.5-alpine
MAINTAINER Michael Anthony <mailertaylor+docker@gmail.com>

#setup curl for healthcheck
RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

#setup flask app
WORKDIR /hello
COPY app.py ./app.py
COPY requirements.txt ./requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]
EXPOSE 8080
ENTRYPOINT ["./app.py"]

HEALTHCHECK --interval=5s --timeout=10s \
  CMD curl -w %{http_code} --output /dev/null http://0.0.0.0:8080/hello \
      | grep 200 \
      || exit 1
