#Take latest ubuntu and add Python on it
FROM python:latest

#The dir in which we want to be
WORKDIR /root

#Now we add a sample text file
ADD atextfile.txt /root 
ADD .nanorc /root
ADD flask_test.py /root


#We need nano and there's no docker repository on it so let's install them
RUN apt-get update -y
RUN apt-get install nano screen -y
RUN pip install flask

#We run the bash, if we needed some other command we separate them by commas. 
CMD ["bash"]

