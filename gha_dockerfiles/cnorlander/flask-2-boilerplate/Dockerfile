FROM ubuntu:20.10
ENV TZ=America/Vancouver
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone 
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip
VOLUME /deploy
WORKDIR /deploy
COPY requirements.txt .
RUN pip3 install setuptools
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["/usr/local/bin/gunicorn", "-b", ":8080", "flask-boilerplate:app", "--log-level=info", "--workers=5", "-t 30", "--worker-class=gthread", "--reload"]
