# MeInGym training exercise service

Микросервис с АПИ для получения оценки времени на выполнение упражнения для проекта MeInGym

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```shell
flask --app src/app run --port 5001 --debug
```

## Проверка
```shell
jq -c '.' examples/example1.json examples/example2.json > examples/example.jsonl
curl -X POST http://127.0.0.1:5001/predict -H "Content-Type: application/jsonl" -i --data-binary @examples/example.jsonl
```