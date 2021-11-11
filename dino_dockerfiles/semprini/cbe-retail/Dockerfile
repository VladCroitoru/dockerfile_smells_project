# Start with a Python image.
FROM uroybd/python3-psycopg2-alpine
#FROM python:alpine


# Set default required environment variables
ENV PYTHONUNBUFFERED 1

ENV DBENGINE sqlite3
ENV DBNAME /code/dblocal.sqlite3
ENV DBHOST None
ENV DBPORT None
ENV DBUSER None
ENV DBPASSWORD None

ENV SUNAME super 
ENV SUEMAIL super@super.com
ENV SUPASS super

ENV MQHOST None
ENV MQUSER None
ENV MQPASSWORD None
ENV MQRESTSERVER '127.0.0.1'
ENV MQRESTPORT 8000

# Install some necessary things.
RUN apk update
RUN apk add swig 
RUN apk add openssl-dev 
RUN apk add dpkg-dev 
RUN apk add netcat-openbsd 
RUN apk add git
#RUN apk add py-pip
#RUN apk add postgresql-dev
#RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/main py3-psycopg2
#RUN cp -R /usr/lib/python3.6/site-packages/psycopg2 /usr/local/lib/python3.6/site-packages/

# Install dependencies not in requirements.txt
#RUN pip install -U pip

# Copy all our files into the image.
RUN git clone https://github.com/Semprini/cbe-retail.git /cbe-retail
WORKDIR /cbe-retail
RUN pip install -Ur requirements.txt

# Collect our static media
RUN python manage.py collectstatic --noinput

# Specify the command to run when the image is run.
RUN ["chmod", "+x", "/cbe-retail/manage_run.sh"]
CMD ["/cbe-retail/manage_run.sh"]
