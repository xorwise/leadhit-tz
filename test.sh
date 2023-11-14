#!/bin/bash

# Входные данные для проверки
input_data=(
    "full_name=michael&email=michael@gmail.com&phone_number=+7 900 999 99 99"
    "full_name=alice&email=alice@gmail.com&phone_number=+1 123 456 78 90"
    # Добавьте другие входные данные, если нужно
)

# Цикл для проверки каждого набора входных данных
for data in "${input_data[@]}"
do
    echo "Checking input data: $data"

    # Отправка POST-запроса с помощью curl
    curl -X POST -d "$data" http://127.0.0.1:8000/get_form
    echo "------------------------------------"
done
