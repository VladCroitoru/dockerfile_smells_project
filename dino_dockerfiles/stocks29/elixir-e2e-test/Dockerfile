FROM marceldegraaf/elixir

RUN sudo apt-get install -y build-essential xvfb libxss1 libappindicator1 libindicator7 unzip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
RUN sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN sudo apt-get install -y nodejs google-chrome-stable
RUN wget -N http://chromedriver.storage.googleapis.com/2.20/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN chmod +x chromedriver
RUN sudo mv -f chromedriver /usr/local/share/chromedriver
RUN sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
RUN sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
