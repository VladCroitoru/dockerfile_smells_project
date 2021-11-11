FROM python:2.7-jessie
LABEL maintainer Neil Carpenter <neil@twistlock.com>

# Make sure python has what we need
RUN python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools 
RUN pip install urllib3 ipaddress requests docopt

# Install ncat (which is in nmap) and screen
RUN apt-get update
RUN apt-get install -y nmap screen dnsutils

# Get our exploit code
RUN mkdir struts2
RUN curl -o /struts2/strutsrce.py https://dl.packetstormsecurity.net/1703-exploits/struntsrce.py.txt

# And add the script to run the exploit code
COPY exploit.sh /struts2/exploit.sh
RUN chmod +x /struts2/exploit.sh
COPY exploit_auto.sh /struts2/exploit_auto.sh
RUN chmod +x /struts2/exploit_auto.sh

# Sleep so that the container stays up
# long enough for us to run the exploit
CMD [ "sleep",  "10001"]

