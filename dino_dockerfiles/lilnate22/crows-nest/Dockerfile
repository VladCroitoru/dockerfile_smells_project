FROM python:latest
MAINTAINER Nate Fonseka
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["main.py"]
