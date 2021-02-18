FROM ubuntu:18.04

ENV TZ=Europe/Oslo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN \
    apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y wget && \
    apt-get install -y gnupg2 && \
    apt-get install -y git-all && \
    apt-get install -y libssl-dev && \
    apt-get install -y make && \
    apt-get install -y libsnappy-dev

RUN \
    apt-get update && \
    wget https://packages.erlang-solutions.com/erlang-solutions_2.0_all.deb && \
    dpkg -i erlang-solutions_2.0_all.deb &&\
    wget https://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc && \
    apt-key add erlang_solutions.asc

RUN \
    apt-get update && \
    apt-get install -y erlang

WORKDIR /root/
RUN \
    mkdir src && \
    cd src && \
    git clone https://github.com/vernemq/vernemq.git

WORKDIR /root/src/vernemq
RUN make rel; exit 0
RUN make rel

RUN mv ./_build/default/rel/vernemq ~/vernemq
ENV PATH="~/vernemq/bin:$PATH"

WORKDIR /root
COPY /configuration /root/vernemq/etc

ENV VERNEMQ_USER=$VERNEMQ_USER
ENV VERNEMQ_PASSWORD=$VERNEMQ_PASSWORD

CMD /root/vernemq/bin/vernemq start && /bin/bash