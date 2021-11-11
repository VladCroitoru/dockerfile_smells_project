# reduced python as base image
FROM python:3.8-slim-buster 

# set a directory for the app
WORKDIR /usr/src/app 

# copy all the files to the container
COPY . . 

# install german language support for locales
RUN apt-get update && apt-get install -y locales-all

# pip install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port 8501 since flask runs on this port
EXPOSE 8501 

# command that is run when container is started
CMD ["streamlit", "run", "./app.py"] 
