FROM clojure

RUN apt-get update && apt-get install -y gcc
ADD drip /bin/
RUN /bin/drip
