FROM mono:6
RUN apt-get update
RUN apt-get install -y wget unzip
RUN wget https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN ln -s $PWD/chromedriver /usr/local/bin/chromedriver
