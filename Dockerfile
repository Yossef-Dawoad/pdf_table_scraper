FROM python:3.11
# 
WORKDIR /code


COPY ./requirements.prod.txt /code/requirements.txt

# Update the package list and install OpenJDK 8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk

# set java env variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m spacy download en_core_web_sm



COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--workers", "2", "--host", "0.0.0.0", "--port", "8000"]