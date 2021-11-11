FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y && apt-get update
RUN apt install g++-10 -y
RUN add-apt-repository ppa:deadsnakes/ppa -y && apt install python3.8 -y
RUN apt-get install make -y
RUN apt-get install git -y
RUN apt install python3-pip -y
RUN python3.8 -m pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y curl wget zsh cmake
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" -y
RUN apt-get install direnv; echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
RUN echo "export HISTFILE=/workspaces/Rubik-s-Cube-Solver/.zsh_history" >> ~/.zshrc
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# RUN apt-get install valgrind -y
# RUN apt-get install python -y
ENTRYPOINT /bin/zsh