FROM ubuntu:latest

COPY . /root/project_tools/
RUN chmod +x /root/project_tools/startup.sh
RUN apt-get update && apt-get install -y git nmap python3 python3-pip
RUN pip3 install pipenv
RUN cd /root/project_tools && pipenv install
RUN cd /root/project_tools/Dashboard
RUN export FLASK_APP=run
CMD /root/project_tools/startup.sh
EXPOSE 5000
