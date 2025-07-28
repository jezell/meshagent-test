FROM meshagent/python-sdk-slim:latest

COPY . /src

WORKDIR /src
ENTRYPOINT [ "python3", "main.py" ] 

