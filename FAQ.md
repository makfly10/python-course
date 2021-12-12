# Frequently Asked Questions

Для упрощения жизни и атмосферы в чатике - ответы на некоторые общие вопросы вынесены сюда. 


### Q: Локально проходят все тесты, а на сервере ошибки 

<details><summary><b>A: [под спойлером]</b></summary>

В рервую очередь нужно проверить, что вы запускате тесты и линтеры с учётом файла конфигурации (`setup.cfg`).  
Есть 2 варианта как запусть тесты и линтеры 
* Можно запускать из корня проекта, тогда файл подцепится автоматически
  ```shell
  python -m flake8 ./path/to/the/task
  python -m mypy ./path/to/the/task
  python -m pytest ./path/to/the/task
  ```
* Можно запускать из любой директории, но нужно указать файл ручками
  ```shell
  python -m flake8 --config ../../setup.cfg task_name
  python -m mypy --config-file ../../setup.cfg task_name
  python -m pytest -c ../../setup.cfg task_name
  ```
</details>
