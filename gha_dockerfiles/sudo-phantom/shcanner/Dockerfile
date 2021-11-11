FROM kalilinux/kali-rolling
RUN apt-get update && apt-get upgrade -y && apt-get install -y  nmap python3 python3-pip
ADD shcanner.py /
ADD requirements.txt /
ADD scope.txt /
RUN mkdir /reqs
ADD  /reqs ./reqs/weak-ciphers.txt
RUN pip install pystrich
RUN pip install -r requirements.txt
CMD [ "python3", "./shcanner.py" ]
