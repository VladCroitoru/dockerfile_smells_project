FROM ruby:2.2

RUN gem install dmarkow-right_aws --source http://gems.github.com
RUN wget https://raw.github.com/lathanh/s3nukem/master/s3nukem \
    && chmod 755 s3nukem

ENTRYPOINT ["ruby", "s3nukem"]
