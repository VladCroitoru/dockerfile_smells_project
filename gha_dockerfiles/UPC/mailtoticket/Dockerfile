FROM python:3.7

WORKDIR /usr/src/app
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -yy libsasl2-dev libldap2-dev
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "mailtoticket.py" ]
