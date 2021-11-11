FROM python:3.9
EXPOSE 8000
WORKDIR /usr/src
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get -y update && apt-get install -y cron

# copy sourcecode and compiled frontend
COPY . .

CMD ["/usr/src/entrypoint.sh"]
