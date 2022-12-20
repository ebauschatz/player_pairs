FROM python:alpine3.17
WORKDIR /home/emily/player_pairs
COPY . .
CMD ["python3", "main.py"]