FROM redhat/ubi8:8.4
RUN dnf install -y https://dev.mysql.com/get/mysql80-community-release-el8-1.noarch.rpm
RUN dnf install -y python3-devel mysql
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip3 install -r requirements.txt
ADD . /app/
CMD ["flask", "run"]
