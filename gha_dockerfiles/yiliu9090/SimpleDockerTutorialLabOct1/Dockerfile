FROM python:latest 
#Some starting point (Unix, Windows Server)

#Install numpy 
RUN pip install numpy
RUN pip install pandas
#Build a folder for me to put my file inside 

RUN mkdir /workspace/ 

COPY Code /workspace/

WORKDIR /workspace/ 

ENTRYPOINT ["python", "run.py"]

