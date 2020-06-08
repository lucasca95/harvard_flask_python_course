FROM python:3

RUN apt update
RUN apt install libpq-dev

RUN mkdir /www
ADD requeriments.txt /www/requeriments.txt
RUN pip install -r /www/requeriments.txt

WORKDIR /www/

# Nombre del archivo ejecutable Flask
ENV FLASK_APP airline1.py
# Activar modo debug para que la app se reinicie al detectar un cambio
ENV FLASK_DEBUG 1


ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=3333" ]