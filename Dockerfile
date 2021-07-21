# syntax=docker/dockerfile:1

FROM python:3.9.6-slim

WORKDIR /usr/src/dev/python-sudoku

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["./solve_sudoku.py"]

CMD ["--help"]
