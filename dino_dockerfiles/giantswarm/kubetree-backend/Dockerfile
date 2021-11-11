FROM python:2.7-alpine
ENV PYTHON_UNBUFFERED 1
EXPOSE 5000
WORKDIR /app
RUN pip install requests Flask
ADD . /app/
ENTRYPOINT ["python", "service.py"]
