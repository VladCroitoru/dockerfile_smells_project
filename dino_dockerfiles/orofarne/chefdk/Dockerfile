FROM chef/chefdk:2.4.6

RUN apt-get update && apt-get install nano locales git --yes

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen

ENV EDITOR=nano
ENV LC_ALL=en_US.UTF-8
