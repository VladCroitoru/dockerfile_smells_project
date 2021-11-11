#from official python 2.7 docker build
FROM python:2

#Set working directory to src to run commands
WORKDIR /src

#Add requirements file before install requirements
COPY requirements.txt ./requirements.txt

#Install requirements, including nose2
RUN pip install -r requirements.txt
