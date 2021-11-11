FROM python:3-slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME AlexaInterrogator
CMD ["python","app.py"]
