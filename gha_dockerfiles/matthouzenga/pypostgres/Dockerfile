FROM registry.access.redhat.com/ubi8/python-38

WORKDIR /app
COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["app.py"]
