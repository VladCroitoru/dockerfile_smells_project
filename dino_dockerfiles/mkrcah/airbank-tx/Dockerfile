FROM khozzy/selenium-python-chrome

USER root
RUN pip install -I click

USER chrome
ADD download.py /app/
WORKDIR /app

ENTRYPOINT ["xvfb-daemon-run", "python" , "download.py"]
