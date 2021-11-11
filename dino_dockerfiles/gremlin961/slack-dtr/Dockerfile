FROM python:3.6.3-alpine
RUN mkdir /database
COPY ./ /
RUN pip install -r requirements.txt
ENV FLASK_APP /run.py
CMD python -m flask run --host=0.0.0.0 --port=80
