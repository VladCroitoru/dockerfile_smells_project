# set python image
FROM python:3  

# set working directory
WORKDIR /usr/src/app  

# install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy source code
COPY . .

# execute the script, default to Honeywell zone 0 if runtime parameters are not provided
#CMD ["supervise.py", "honeywell", "0"]
#ENTRYPOINT ["python3"]
ENTRYPOINT ["python3", "-m", "supervise"]
CMD ["honeywell", "0"]
