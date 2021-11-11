FROM python:3.6-stretch
ADD . /var/tbg/
WORKDIR "/var/tbg/"
RUN ["pip", "install", "-qr", "/var/tbg/requirements.txt"]
EXPOSE 8080
ENTRYPOINT ["make", "run"]