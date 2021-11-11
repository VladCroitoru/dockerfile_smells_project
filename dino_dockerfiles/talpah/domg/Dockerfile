FROM python:3

EXPOSE 80

ENV PYTHONUNBUFFERED=1

WORKDIR /home/user/application

COPY . /home/user/application

RUN pip install -r requirements.txt

CMD ["/home/user/application/start.sh"]
