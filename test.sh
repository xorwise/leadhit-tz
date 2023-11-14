#!/bin/bash

# Правильные данные для шаблона Contact Information
curl -X POST "http://127.0.0.1:8000/get_form?full_name=Michael%20Sitnikov&phone_number=%2B7%20900%20999%2099%2099&email=michael@gmail.com"
echo
echo 

# Правильные данные для шаблона Event Registration, дата в двух форматах DD.MM.YYYY и YYYY-MM-DD
curl -X POST "http://127.0.0.1:8000/get_form?event_name=Comi-Con&participant_email=michael@gmail.com&event_date=22.11.2023"
echo
curl -X POST "http://127.0.0.1:8000/get_form?event_name=Comi-Con&participant_email=michael@gmail.com&event_date=2023-11-22"
echo
echo 

# Правильные данные для шаблона Feedback Form
curl -X POST "http://127.0.0.1:8000/get_form?feedback_text=lorem%20ipsum%20dolor&rating=5&feedback_date=23.11.2023"
echo
echo 

# Данные, для которых нет подходящих шаблонов
curl -X POST "http://127.0.0.1:8000/get_form?some_key=some_value"
echo
echo 

# Данные, когда ключей во входных данных больше, чем в шаблоне Contact Information
curl -X POST "http://127.0.0.1:8000/get_form?full_name=Michael%20Sitnikov&phone_number=%2B7%20900%20999%2099%2099&email=michael@gmail.com&extra_key=extra_value"
echo
echo 

# Данные, которые не проходят валидацию даты
curl -X POST "http://127.0.0.1:8000/get_form?event_name=Comi-Con&participant_email=michael@gmail.com&event_date=22.11:2023"
echo
echo 

# Данные, которые не проходят валидацию телефона (нет пробела после +7)
curl -X POST "http://127.0.0.1:8000/get_form?full_name=Michael%20Sitnikov&phone_number=%2B7900%20999%2099%2099&email=michael@gmail.com"
echo 
echo 

# Данные, которые не проходят валидацию почты (нет точки)
curl -X POST "http://127.0.0.1:8000/get_form?event_name=Comi-Con&participant_email=michael@gmailcom&event_date=22.11.2023"
echo
