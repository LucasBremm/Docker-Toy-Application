FROM python:3-alpine

RUN apk update && \
    apk add nodejs npm curl

WORKDIR /usr/src/app

RUN curl https://raw.githubusercontent.com/eficode/wait-for/master/wait-for -o wait-for.sh && \
    chmod +x wait-for.sh

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod -x umid.py

CMD ./wait-for.sh rabbitmq:5672 -- python ./umid.py