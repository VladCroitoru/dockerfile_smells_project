FROM python:3.8
# create app directory
RUN mkdir -p /app
# using app directory
WORKDIR /app
#install required libraries
RUN apt update && apt install -y libffi-dev libopus-dev ffmpeg
# copy requirements txr
COPY requirements.txt requirements.txt
# install app dependencies
RUN pip install -r requirements.txt
# copy all project files
COPY . .
# run app
CMD ["python", "-m", "pekora"]