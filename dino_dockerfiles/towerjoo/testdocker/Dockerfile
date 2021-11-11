#FROM zhutao/lh:1.0 
FROM ubuntu
EXPOSE 8000
RUN apt-get update && apt-get install -y python-pip && apt-get install -y git && \
    mkdir www && cd www && git clone https://github.com/towerjoo/testdocker && \
    cd testdocker && pip install -r requirements.txt && python manage.py migrate

CMD ["python", "/www/testdocker/manage.py", "runserver", "0.0.0.0:8000"]
