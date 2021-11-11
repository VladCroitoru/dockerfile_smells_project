FROM python:3-alpine
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
RUN pip install tornado
EXPOSE 8080
CMD ["python", "ws_app.py"]

