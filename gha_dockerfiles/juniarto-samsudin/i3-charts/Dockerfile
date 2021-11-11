FROM python:latest
RUN pip install flask flask-blueprint waitress requests simplejson scipy
WORKDIR C:/app
COPY i3-charts .
#CMD ["flask", "run","--host=0.0.0.0"]
CMD ["python", "waitress_server.py"]
