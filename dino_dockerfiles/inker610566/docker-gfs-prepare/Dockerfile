FROM dorowu/ubuntu-desktop-lxde-vnc
RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz | tar zxvf - -C /bin
RUN pip install --upgrade selenium google-api-python-client
COPY register.py /root/Desktop/
RUN chmod +x /root/Desktop/register.py
