FROM python:alpine
COPY . /flask-devops-proj
WORKDIR /flask-devops-proj
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","flaskApp.py"]
