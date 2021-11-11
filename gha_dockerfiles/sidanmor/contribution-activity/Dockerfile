FROM ubuntu:16.04

RUN apt update
RUN apt install -y git

RUN git clone https://github.com/sidanmor/contribution-activity.git

RUN cd contribution-activity
RUN echo "# contribution-activity" >> README.md
RUN git add README.md
RUN git config --global user.email "sidanmor@gmail.com"
RUN git commit -m "commit"
RUN git push -u origin master
