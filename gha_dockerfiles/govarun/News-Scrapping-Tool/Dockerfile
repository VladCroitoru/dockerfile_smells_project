FROM python:3.6.7-slim
#set working directory
WORKDIR /app
#copy the contents of current directory into the container at /app
ADD . /app
#install required packages
RUN pip install -r requirements.txt
#make port 80 available to the world for communication
EXPOSE 80
#run app.py when container launches
CMD ["python","app.py"]