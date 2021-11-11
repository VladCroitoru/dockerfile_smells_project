FROM debian:latest

RUN apt-get update -y && apt-get install openssh-client -y

# Add non-root user
RUN useradd user
RUN mkdir /home/user
RUN chown user:user /home/user -R
USER user

