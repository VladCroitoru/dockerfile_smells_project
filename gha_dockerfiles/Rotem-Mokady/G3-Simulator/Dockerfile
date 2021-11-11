FROM mcr.microsoft.com/oryx/python-3.7:latest

# general updates
RUN apt-get update -y

# set a new current working directory
WORKDIR /opt

# add only relevant directories to Docker environment
ADD app ./app/
ADD calculations ./calculations/
ADD configs ./configs/

# add only relevant files to Docker environment
ADD run.py ./
ADD .gitignore ./
ADD requirements.txt ./

# install version specifiers python packages and then remove requirements
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf ./requirements.txt

# export app to host's network
# EXPOSE 80

# run webapp
ENTRYPOINT ["python", "run.py"]