FROM python:3.5 

MAINTAINER malkazwini@gmail.com

#RDS credentials to be passed at runtime as env vars
ENV rds_endpoint \
	rds_username \
	rds_password \
	rds_dbname 

#Copy App source
COPY /src /home

# install required pip dependancies
RUN pip install -r /home/requirements.txt

#Create DB to initialize the schema 
CMD ["python","/home/db_create.py"]

# Run the application 
ENTRYPOINT ["python", "/home/application.py"]

EXPOSE 4443
