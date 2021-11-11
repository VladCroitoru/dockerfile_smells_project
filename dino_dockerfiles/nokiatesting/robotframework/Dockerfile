FROM python:3.6
ENV ROBOT_HOME=/usr/src/robot
WORKDIR /usr/src/robot
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
VOLUME /usr/src/robot
CMD ["python3", "-m", "robot"]
