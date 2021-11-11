FROM julia:0.6

RUN apt-get update && \
	apt-get install -y \
	build-essential \
	unzip \
	git \
	cmake && \
	apt-get clean

ADD REQUIRE REQUIRE

RUN julia -e 'Pkg.init()' && \
	mv REQUIRE $(julia -e "print(Pkg.dir())") && \
	julia -e 'Pkg.resolve()'
