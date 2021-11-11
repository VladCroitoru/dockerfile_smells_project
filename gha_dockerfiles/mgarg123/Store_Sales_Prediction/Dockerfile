FROM python:3.9

LABEL maintainer="manish manish.garg771@gmail.com"

#RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

#EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]