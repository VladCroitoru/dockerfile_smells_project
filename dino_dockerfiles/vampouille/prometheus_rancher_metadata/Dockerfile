FROM python:3.4

RUN pip install Flask

ADD rancher_metadata.py /opt/

ENV FLASK_APP /opt/rancher_metadata.py 

EXPOSE 5000

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]

