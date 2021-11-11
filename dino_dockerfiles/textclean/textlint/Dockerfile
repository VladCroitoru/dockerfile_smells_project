FROM textclean/node-base
MAINTAINER nickg
WORKDIR /tmp
RUN /bin/true \
  && npm install -g textlint \
  && npm install -g textlint-rule-max-number-of-lines \
  && npm install -g textlint-rule-max-comma \
  && npm install -g textlint-rule-no-exclamation-question-mark \
  && npm install -g textlint-rule-ng-word \
  && npm install -g textlint-rule-no-dead-link \
  && npm install -g textlint-rule-report-node-types \
  && npm install -g textlint-rule-unexpanded-acronym \
  && npm install -g textlint-rule-rousseau \
  && npm install -g textlint-rule-alex \
  && npm install -g textlint-rule-write-good \
  && npm install -g textlint-rule-en-max-word-count \
  && npm cache clean 
ENTRYPOINT [ "/usr/bin/textlint" ]

# Note:
#   
#   npm install -g textlint-rule-no-todo
#     not useful
#   npm install -g textlint-rule-editorconfig 
#     for interfacing with another program
#   npm install -g textlint-rule-spellchecker 
#     requires python
#   npm install -g textlint-rule-ginger 
#     commericial service
#
