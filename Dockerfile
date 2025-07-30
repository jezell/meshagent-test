FROM meshagent/python-sdk-slim:latest

RUN apt-get install -y curl

COPY . /src

WORKDIR /src
ENTRYPOINT [ "python3", "main.py" ] 

