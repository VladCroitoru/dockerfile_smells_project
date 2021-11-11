FROM python:3.9
 
WORKDIR /parking_system
COPY . .
 
RUN pip3 install -r requirements.txt
 
CMD [ "python3", "-m" , "parking_system", "example_input.txt"]