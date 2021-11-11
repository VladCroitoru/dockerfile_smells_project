#from alpine in theory because we are using an alpine distro, pip3 and python3
# SHOULD be included in this alpine package if we do not require other packages
# included in the apk-get ubuntu package manager, then the blow lines will be
# sufficent
FROM alpine:3.6
# add ubuntu pyhton3 update package to alpine distro
RUN apk add --update python3

#the below addes ALL files in current directory inside a new
# folder called flaskapp
# NODE: ADD . /flaskapp and ADD . flaskapp/ are all teh same thing
ADD . flaskapp





COPY requirements.txt /flaskapp/requirements.txt
RUN pip3 install -U pip setuptools wheel
#change to the dierctroy for pip to find the external lib to use and install
WORKDIR flaskapp
RUN pip3 install -r /flaskapp/requirements.txt


#COPY requirements.txt /OBAMA/
#ADD requirements.txt /TRUMP/

#COPY app.py /src
#COPY engines /src/engines
#COPY docker-compose.yml /src
#CMD python3 /src/app.py
#WORKDIR flaskapp
CMD python3 app.py
