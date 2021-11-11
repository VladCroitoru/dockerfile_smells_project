FROM python:3.9.1
ADD ./UI /python-flask
WORKDIR /python-flask
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir -p models
RUN python download_models.py
EXPOSE 8081
ENTRYPOINT ["python","app.py"]