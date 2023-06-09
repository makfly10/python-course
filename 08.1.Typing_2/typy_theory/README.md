## TYPY THEORY

`typing` `TypeVar` `Co/Contra` `Protocol` `Generic`

### Условие

В файле `Problems.pdf` находится 10 задач. В файлике `theory.py` нужно написать, на каких строчках mypy будет ругаться и почему.
Для каждой задачи вернуть словарь, где ключом является номер строчки с ошибкой, а значением - причина ошибки.

Например, если б задача выглядела так
```python
# Problem example
[1] a = "hello"
[2] a += 1
[3] a = 10
```
то в функцию вам нужно было бы написать что-то подобное:
```python
def problem_example():
    return {
        2: "Операция сложения для int и str не определена. В Runtime вылетела бы ошибка",
        3: "Нельзя делать переприсвоение переменной неконсистентным типом. Это может привести к TypeError при вызове методов, которые ниже по коду работают с изначальным типом"
    }
```

### Как подходить к решению

У этой задачи по понятным причинам закрытые тесты. Вначале попытайтесь решить сами, как мы делали на лекции. 
Отправьте в систему, там вам напишет, какие задачи вы решили неправильно.
Попробуйте сами найти ошибки. Если совсем не удастся, то только тогда перепечатывайте себе задачу и разбирайтесь

Удостоверьтесь, что у вас mypy версии 0.910

```bash
$ ~/.pyenv/versions/shad_env/bin/mypy --version
mypy 0.910
```

Чтобы запускать mypy в jupyter-ноутбуке, посмотрите Readme в папке с лекциями.
