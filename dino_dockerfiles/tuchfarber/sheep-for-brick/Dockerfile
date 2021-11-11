FROM python:slim
RUN apt-get update && yes | apt-get install gcc
RUN pip install bottle redis passlib py-bcrypt
COPY src /var/www/html/src/
COPY static /var/www/html/static/
COPY templates /var/www/html/templates/
COPY app.py /var/www/html/app.py
ENTRYPOINT ["python", "/var/www/html/app.py"]