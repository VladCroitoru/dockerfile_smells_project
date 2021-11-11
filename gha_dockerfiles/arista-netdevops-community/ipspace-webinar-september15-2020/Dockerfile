FROM avdteam/base:3.6


WORKDIR /projects
VOLUME ["/projects"]

RUN git clone https://github.com/aristanetworks/ansible-avd.git /ansible-avd
RUN git clone https://github.com/aristanetworks/ansible-cvp.git /ansible-cvp
COPY . /projects

CMD [ "/bin/zsh" ]