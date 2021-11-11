FROM python:2-alpine

#use gunicorn
RUN pip install gunicorn==19.6.0

#install requirements
COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app/
RUN pip install -r requirements.txt
COPY . /usr/src/app/

EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/gunicorn"]

CMD ["-w","1","-b","0.0.0.0:5000","--threads","1","application:app","--access-logfile","/dev/stdout","--error-logfile","/dev/stdout"]
