# our base image
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 5000

COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]