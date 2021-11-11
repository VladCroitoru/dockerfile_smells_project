FROM python:2.7
MAINTAINER Stratos Xakoustos <stratouklos@gmail.com>

RUN pip install --upgrade pip 

RUN pip install robotframework

RUN pip install robotframework-databaselibrary

RUN pip install robotframework-httplibrary

RUN pip install robotframework-selenium2library

RUN pip install robotframework-anywherelibrary

RUN pip install robotframework-sshlibrary

RUN pip install https://github.com/robotframework/Rammbock/archive/master.zip

RUN pip install https://github.com/bulkan/robotframework-difflibrary/archive/master.zip 

RUN pip install robotframework-faker

RUN pip install robotframework-ftplibrary

RUN apt-get install curl -y

RUN useradd -m -d /home/robot -s /bin/bash -U robot
