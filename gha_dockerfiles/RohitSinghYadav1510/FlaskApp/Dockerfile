FROM python:3.9.4

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt /usr/src/app/

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Bundle app source
COPY . /usr/src/app


#ENTRYPOINT ["python3"]

#CMD ["app.py"]

EXPOSE 5000
