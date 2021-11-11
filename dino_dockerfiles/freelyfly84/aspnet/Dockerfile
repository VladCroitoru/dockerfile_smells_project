FROM mono:4.0
RUN apt-get update; apt-get -y install mono-xsp4
ADD . /app/
WORKDIR /app
COPY ./src .
EXPOSE 80
ENTRYPOINT ["xsp4", "--port=80", "--nonstop"]
