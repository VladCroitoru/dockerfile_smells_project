FROM python:3.7
ENV PYTHONUNBUFFERED 1
# ENV GOOGLE_APPLICATION_CREDENTIALS /home/fmanage/testiam.json
# ADD requirements.txt requirements.txt
COPY ./ /home/fmanage/
WORKDIR /home/fmanage
RUN apt update && apt upgrade -y
RUN pip3 install -r requirements.txt
EXPOSE 8000