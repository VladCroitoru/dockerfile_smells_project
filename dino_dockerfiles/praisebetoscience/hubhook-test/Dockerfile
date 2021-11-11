FROM python:alpine

WORKDIR /src
ADD . .

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt 
    
EXPOSE 3000
CMD ["/src/wsgi.py"]
