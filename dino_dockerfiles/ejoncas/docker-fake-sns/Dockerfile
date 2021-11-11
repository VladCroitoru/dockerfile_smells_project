FROM ruby:2.1

RUN git clone https://github.com/ejoncas/fake_sns
RUN cd fake_sns && bundle install

EXPOSE 9292

ENTRYPOINT [ "fake_sns", "-p", "9292"]
