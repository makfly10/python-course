# Тестирование и python

В этой лекции мы познакомимся тестированием на `python` реализовав небольшую кату в по TDD (test-driven developement)

## 1. TDD и каты.

TDD - test-driven developement или разработка через тестирование. Достигается путем соблюдения трех правил:

**Три правила TDD**:

 - Продакшн-код можно писать только для починки падающего теста
 - В тесте нужно писать ровно столько кода, сколько необходимо чтобы он упал. Ошибки компиляции считаются падениями теста.
 - В прод можно написать ровно столько кода, сколько требуется для починки дного падающего теста.


Получается следйющий пайплайн - пишем падающий тест, пишем код чтобы тест не падал, рефакторим код чтобы тесты не падали. Повторяем до сходимости.

Есть пара книжек по теме:

1. [Test Driven Development: By Example 1st Edition](https://www.eecs.yorku.ca/course_archive/2003-04/W/3311/sectionM/case_studies/money/KentBeck_TDD_byexample.pdf)
2. [On Growing Object Oriented Software, Guided by Tests](https://www.amazon.com/Growing-Object-Oriented-Software-Guided-Tests/dp/0321503627)

К прочтению рекомендуется вторая, т.к. она более приближена к разработческим реалиям.

### Каты

![kata.png](attachment:kata.png)

Каты - упражнения по программированию, помогающие отточить навыки путем многократного повторнеия. Концепция взята из японских боевых искусств. Подробнее про них можно почитать в книжке [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)



**Ката Greeter**

Данную кату надо выполнять строго по пунктам, не заглядывая вперед:

- Создайте класс `Greeter`, у которого есть метод `greet` принимающий на вход имя и возвращающий "Hello <имя>".
- Метод `greet` должен убирать лишние пробелы - в начале и в конце имени
- Метод `greet` должен возвращать ошибку если имя - пустая строка (или строка с пробелами)
- Метод `greet` возвращает "Good evening <имя>" если текущее время - 18:00-22:00

## 2. Первый тест

Для автоматизированного тестирования написано много фреймворков на разных языках. Короткий список для python:

* [unittest](https://docs.python.org/3/library/unittest.html)
* [nose2](https://docs.nose2.io/en/latest/)
* [pytest](https://docs.pytest.org/en/latest/)

В рамках лекции мы остановимся на pytset.


```python
# Настраиваем ноутбук
import pytest
import ipytest
ipytest.config(rewrite_asserts=True, magics=True)
__file__ = "Testing.ipynb"
```

### Как pytest находит тесты:

1. Рекурсивно находит все python-файлы в текущей директории
2. Оставляет только файлы вида `test_*.py` и `*_test.py`
3. В этих файлах
  3.1 Находит все функции с префиксом `test`
  3.2 Находит все методв с префиксом `test` внутри классов с префиксом `Test`. У классов не должно быть метода `__init__`
  
Поведение можно модифицировать. [Подробнее в документации](https://docs.pytest.org/en/stable/goodpractices.html#test-discovery)

Напишем минимальный тест 


```python
%%run_pytest[clean] -q

def test_greeter():
    Greeter()
```

    F                                                                        [100%]
    =================================== FAILURES ===================================
    _________________________________ test_greeter _________________________________
    
        def test_greeter():
    >       Greeter()
    E       NameError: name 'Greeter' is not defined
    
    <ipython-input-2-f0bf3d5080f2>:2: NameError
    =========================== short test summary info ============================
    FAILED Testing.py::test_greeter - NameError: name 'Greeter' is not defined
    1 failed in 0.05s


Pytest выдает отчет, в котором можно посмотреть сколько у нас всего тестов, какие из них упали и по какой причине. Теперь сделаем так чтобы тест проходил


```python
class Greeter:
    pass
```


```python
%%run_pytest[clean] -q

def test_greeter():
    Greeter()
```

    .                                                                        [100%]
    1 passed in 0.00s


Еще одна итерация tdd


```python
%%run_pytest[clean] -q

def test_greeter():
    Greeter().greet("Mike")
```

    F                                                                        [100%]
    =================================== FAILURES ===================================
    _________________________________ test_greeter _________________________________
    
        def test_greeter():
    >       Greeter().greet("Mike")
    E       AttributeError: 'Greeter' object has no attribute 'greet'
    
    <ipython-input-5-86bee5d034fc>:2: AttributeError
    =========================== short test summary info ============================
    FAILED Testing.py::test_greeter - AttributeError: 'Greeter' object has no att...
    1 failed in 0.01s



```python
class Greeter:
    def greet(self, name):
        return ""
```


```python
%%run_pytest[clean] -q

def test_greeter():
    Greeter().greet("Mike")
```

    .                                                                        [100%]
    1 passed in 0.00s


Теперь наконец-то напишем нормальный тест, воспользовавшись основной фишкой `Pytest` - `assert`. `Pytest` находит все вызовы `assert` в коде тестов, а затем переписывает этот код так, чтобы в случае падения пользователь мог получить удобный дифф и трейсбек.

- [Демки разных аасертов](https://docs.pytest.org/en/stable/example/reportingdemo.html#tbreportdemo)
- [Цикл статей про то, как это работает](https://www.pythoninsight.com/2018/01/assertion-rewriting-in-pytest-part-1/)


```python
%%run_pytest[clean] -q

def test_greeter():
    assert Greeter().greet("Mike") == "Hello Mike"
```

    F                                                                        [100%]
    =================================== FAILURES ===================================
    _________________________________ test_greeter _________________________________
    
        def test_greeter():
    >       assert Greeter().greet("Mike") == "Hello Mike"
    E       AssertionError: assert '' == 'Hello Mike'
    E         - Hello Mike
    
    <ipython-input-8-bb8ac158b55d>:2: AssertionError
    =========================== short test summary info ============================
    FAILED Testing.py::test_greeter - AssertionError: assert '' == 'Hello Mike'
    1 failed in 0.01s


Починим тест


```python
class Greeter:
    def greet(self, name):
        return "Hello Mike"
```


```python
%%run_pytest[clean] -q

def test_greeter():
    assert Greeter().greet("Mike") == "Hello Mike"
```

    .                                                                        [100%]
    1 passed in 0.00s


## 2. Параметризация

Наша реализация представляет собой немного не то что мы хотели. Наверное стоит добавить больше разных тестов.
Чтобы не копировать один и тот же тест, можно воспользоваться параметризацией:


```python
%%run_pytest[clean] -q
test_cases = [("Mike", "Hello Mike"), ("John", "Hello John"), ("Greg", "Hello Greg")]

@pytest.mark.parametrize("name, greeting", test_cases)
def test_greeter(name, greeting):
    assert Greeter().greet(name) == greeting
```

    .FF                                                                      [100%]
    =================================== FAILURES ===================================
    ________________________ test_greeter[John-Hello John] _________________________
    
    name = 'John', greeting = 'Hello John'
    
        @pytest.mark.parametrize("name, greeting", test_cases)
        def test_greeter(name, greeting):
    >       assert Greeter().greet(name) == greeting
    E       AssertionError: assert 'Hello Mike' == 'Hello John'
    E         - Hello John
    E         + Hello Mike
    
    <ipython-input-11-e1e045608403>:5: AssertionError
    ________________________ test_greeter[Greg-Hello Greg] _________________________
    
    name = 'Greg', greeting = 'Hello Greg'
    
        @pytest.mark.parametrize("name, greeting", test_cases)
        def test_greeter(name, greeting):
    >       assert Greeter().greet(name) == greeting
    E       AssertionError: assert 'Hello Mike' == 'Hello Greg'
    E         - Hello Greg
    E         + Hello Mike
    
    <ipython-input-11-e1e045608403>:5: AssertionError
    =========================== short test summary info ============================
    FAILED Testing.py::test_greeter[John-Hello John] - AssertionError: assert 'He...
    FAILED Testing.py::test_greeter[Greg-Hello Greg] - AssertionError: assert 'He...
    2 failed, 1 passed in 0.01s


Видим отчеты пайтеста во всей красе. Починим тесты:


```python
class Greeter:
    def greet(self, name):
        return "Hello " + name
```


```python
%%run_pytest[clean] -q
test_cases = [("Mike", "Hello Mike"), ("John", "Hello John"), ("Greg", "Hello Greg")]

@pytest.mark.parametrize("name, greeting", test_cases)
def test_greeter(name, greeting):
    assert Greeter().greet(name) == greeting
```

    ...                                                                      [100%]
    3 passed in 0.01s


Перейдем к следующему пункту нашего задания:

- Метод `greet` должен убирать лишние пробелы - в начале и в конце имени

Опять же, напишем тест:


```python
%%run_pytest[clean] -q

def test_spaces():
    greeter = Greeter()
    greeting = greeter.greet(" Mike")
    assert not greeting.startswith(" ")
```

    .                                                                        [100%]
    1 passed in 0.00s


Обратим внимание что тест проходит и возникает соблазн продолжить работу. Однако если посмотреть на тест внимательно - можно увидеть в нем ошибку.


Чтобы не наступать на такие грабли существует правило - только что написанный тест должен падать, при чем именно из-за того поведения, которое этот тест должен было покрыть.


Вы можете писать тесты на уже существующий код - в таком случае они могут не падать т.к. код уже работает как надо. Тогда есть два варианта:
* Сделать в продовом коде баг чтобы тест упал
* Обратить проверяемое условие в тесте

Поправим наш тест:


```python
%%run_pytest[clean] -q

def test_spaces():
    greeter = Greeter()
    greeted_name = greeter.greet(" Mike").split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ")
```

    F                                                                        [100%]
    =================================== FAILURES ===================================
    _________________________________ test_spaces __________________________________
    
        def test_spaces():
            greeter = Greeter()
            greeted_name = greeter.greet(" Mike").split(" ", 1)[1]
        
    >       assert not greeted_name.startswith(" ")
    E       AssertionError: assert not True
    E        +  where True = <built-in method startswith of str object at 0x7f910861a1b0>(' ')
    E        +    where <built-in method startswith of str object at 0x7f910861a1b0> = ' Mike'.startswith
    
    <ipython-input-15-952847da0f49>:5: AssertionError
    =========================== short test summary info ============================
    FAILED Testing.py::test_spaces - AssertionError: assert not True
    1 failed in 0.01s


Починим тест


```python
class Greeter:
    def greet(self, name):
        if name.startswith(" "):
            name = name[1:] 
        return "Hello " + name
```


```python
%%run_pytest[clean] -q

def test_spaces():
    greeter = Greeter()
    greeted_name = greeter.greet(" Mike").split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ")
```

    .                                                                        [100%]
    1 passed in 0.00s


Перечитаем наше задание:
* Метод greet должен убирать лишние пробелы - в начале и **в конце имени**

Видимо нам нужно расширить тест:


```python
%%run_pytest[clean] -q

def test_spaces():
    greeter = Greeter()
    greeted_name = greeter.greet(" Mike ").split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    F                                                                        [100%]
    =================================== FAILURES ===================================
    _________________________________ test_spaces __________________________________
    
        def test_spaces():
            greeter = Greeter()
            greeted_name = greeter.greet(" Mike ").split(" ", 1)[1]
        
    >       assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
    E       AssertionError: assert (not False and not True)
    E        +  where False = <built-in method startswith of str object at 0x7f9108609130>(' ')
    E        +    where <built-in method startswith of str object at 0x7f9108609130> = 'Mike '.startswith
    E        +  and   True = <built-in method endswith of str object at 0x7f9108609130>(' ')
    E        +    where <built-in method endswith of str object at 0x7f9108609130> = 'Mike '.endswith
    
    <ipython-input-18-0b745d107b33>:5: AssertionError
    =========================== short test summary info ============================
    FAILED Testing.py::test_spaces - AssertionError: assert (not False and not True)
    1 failed in 0.01s


Починим тест


```python
class Greeter:
    def greet(self, name):
        if name.startswith(" "):
            name = name[1:]
        if name.endswith(" "):
            name = name[:1]
        return "Hello " + name
```


```python
%%run_pytest[clean] -q

def test_spaces():
    greeter = Greeter()
    greeted_name = greeter.greet(" Mike ").split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    .                                                                        [100%]
    1 passed in 0.00s


Наш тест все еще недостаточно хорош. Хороший набор тестов должен покрывать разные граничные условия и заходить во все ветки исполнения кода. Параметризуем наш тест так чтобы покрывал как можно путей исполнения кода:


```python
%%run_pytest[clean] -q

@pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "])
def test_spaces(name):
    greeter = Greeter()
    greeted_name = greeter.greet(name).split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    ....FF                                                                   [100%]
    =================================== FAILURES ===================================
    _____________________________ test_spaces[  Mike] ______________________________
    
    name = '  Mike'
    
        @pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "])
        def test_spaces(name):
            greeter = Greeter()
            greeted_name = greeter.greet(name).split(" ", 1)[1]
        
    >       assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
    E       AssertionError: assert (not True)
    E        +  where True = <built-in method startswith of str object at 0x7f91084165b0>(' ')
    E        +    where <built-in method startswith of str object at 0x7f91084165b0> = ' Mike'.startswith
    
    <ipython-input-25-06978f9470a6>:6: AssertionError
    ____________________________ test_spaces[  Mike  ] _____________________________
    
    name = '  Mike  '
    
        @pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "])
        def test_spaces(name):
            greeter = Greeter()
            greeted_name = greeter.greet(name).split(" ", 1)[1]
        
    >       assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
    E       AssertionError: assert (not True)
    E        +  where True = <built-in method startswith of str object at 0x7f9110ac71f0>(' ')
    E        +    where <built-in method startswith of str object at 0x7f9110ac71f0> = ' '.startswith
    
    <ipython-input-25-06978f9470a6>:6: AssertionError
    =========================== short test summary info ============================
    FAILED Testing.py::test_spaces[  Mike] - AssertionError: assert (not True)
    FAILED Testing.py::test_spaces[  Mike  ] - AssertionError: assert (not True)
    2 failed, 4 passed in 0.02s


Можно давать имена отдельным наборам параметров - тогда будет удобнее читать выхлоп пайтеста


```python
%%run_pytest[clean] -q

@pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                         ids=["no spaces", "left space", "right space", 
                              "two-side space", "double space", "two-sided double space"])
def test_spaces(name):
    greeter = Greeter()
    greeted_name = greeter.greet(name).split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    ....FF                                                                   [100%]
    =================================== FAILURES ===================================
    __________________________ test_spaces[double space] ___________________________
    
    name = '  Mike'
    
        @pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                                 ids=["no spaces", "left space", "right space",
                                      "two-side space", "double space", "two-sided double space"])
        def test_spaces(name):
            greeter = Greeter()
            greeted_name = greeter.greet(name).split(" ", 1)[1]
        
    >       assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
    E       AssertionError: assert (not True)
    E        +  where True = <built-in method startswith of str object at 0x7f91083302f0>(' ')
    E        +    where <built-in method startswith of str object at 0x7f91083302f0> = ' Mike'.startswith
    
    <ipython-input-28-4545c8eb55a1>:8: AssertionError
    _____________________ test_spaces[two-sided double space] ______________________
    
    name = '  Mike  '
    
        @pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                                 ids=["no spaces", "left space", "right space",
                                      "two-side space", "double space", "two-sided double space"])
        def test_spaces(name):
            greeter = Greeter()
            greeted_name = greeter.greet(name).split(" ", 1)[1]
        
    >       assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
    E       AssertionError: assert (not True)
    E        +  where True = <built-in method startswith of str object at 0x7f9110ac71f0>(' ')
    E        +    where <built-in method startswith of str object at 0x7f9110ac71f0> = ' '.startswith
    
    <ipython-input-28-4545c8eb55a1>:8: AssertionError
    =========================== short test summary info ============================
    FAILED Testing.py::test_spaces[double space] - AssertionError: assert (not True)
    FAILED Testing.py::test_spaces[two-sided double space] - AssertionError: asse...
    2 failed, 4 passed in 0.02s


Починим тест


```python
class Greeter:
    def greet(self, name):
        while name.startswith(" "):
            name = name[1:]
        while name.endswith(" "):
            name = name[:1]
        return "Hello " + name
```


```python
%%run_pytest[clean] -q

@pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                         ids=["no spaces", "left space", "right space", 
                              "two-side space", "double space", "two-sided double space"])
def test_spaces(name):
    greeter = Greeter()
    greeted_name = greeter.greet(name).split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    ......                                                                   [100%]
    6 passed in 0.01s


Код кажется слишком многословным! Но, при наличии тестов можно безбоязненно его порефакторить:


```python
class Greeter:
    def greet(self, name):
        return "Hello " + name.strip()
```


```python
%%run_pytest[clean] -q


@pytest.mark.parametrize("name, greeting", [("Mike", "Hello Mike"), ("John", "Hello John"), ("Greg", "Hello Greg")])
def test_greeter(name, greeting):
    assert Greeter().greet(name) == greeting


@pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                         ids=["no spaces", "left space", "right space", 
                              "two-side space", "double space", "two-sided double space"])
def test_spaces(name):
    greeter = Greeter()
    greeted_name = greeter.greet(name).split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    .........                                                                [100%]
    9 passed in 0.01s


## 3. Рефакторинг тестов и фикстуры

Сами тесты тоже надо рефакторить. У нас есть две проблемы.

Во-первых - имена тестов не очень информативны. Если упадет тест `test_greater` - будет не совсем понятно что именно тестировалось и что надо чинить. В целом имена тестам надо давать как можно более подробные - тесты вызываются автоматически, автоматике длинна имени безразлична, а вот человеку, читающему выхлоп пайтеста, лучше предоставить как можно больше информации.

[Статья на тему](https://enterprisecraftsmanship.com/posts/you-naming-tests-wrong)


Переименуем наши тесты:


```python
%%run_pytest[clean] -q


@pytest.mark.parametrize("name", ["Mike", "John", "Greg"])
def test_greet_returns_name_with_greeting(name):
    assert Greeter().greet(name) == "Hello " + name


@pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                         ids=["no spaces", "left space", "right space", 
                              "two-side space", "double space", "two-sided double space"])
def test_greet_removes_leading_and_trailing_spaces_from_name(name):
    greeter = Greeter()
    greeted_name = greeter.greet(name).split(" ", 1)[1]
    
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    .........                                                                [100%]
    9 passed in 0.02s


Вторая проблема - в обоих тестах мы создаем `greeter`. Это привожит к дублированию кода. Кроме того, на практике вместо `greeter` у нас может быть какой-нибудь тяжелый объект типа базы даных, который надо каждый раз инициализировать и чистить. Решить эти проблемы нам поможет механизм фикстур:


```python
%%run_pytest[clean] -q

@pytest.fixture(scope="module")
def greeter():
    yield Greeter()

@pytest.mark.parametrize("name", ["Mike", "John", "Greg"])
def test_greet_returns_name_with_greeting(greeter, name):
    assert Greeter().greet(name) == "Hello " + name


@pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                         ids=["no spaces", "left space", "right space", 
                              "two-side space", "double space", "two-sided double space"])
def test_greet_removes_leading_and_trailing_spaces_from_name(greeter, name):
    greeted_name = greeter.greet(name).split(" ", 1)[1]
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    .........                                                                [100%]
    9 passed in 0.02s


Фикстуры так же могут прибираться за создаваемым объектом в конце теста и иметь разный скоуп - например создваться на каждый тест, модуль или тред, запускающий тесты. [Подробнее в документации] (https://docs.pytest.org/en/stable/fixture.html)

Для БД фикстура может выглядеть примерно так:


```python
%%run_pytest[clean] -s

class DBConnection:
    pass

class TestDB:
    def init_db(self):
        print("init db")
        
    def get_connection(self):
        return DBConnection()

    def shutdown(self):
        print("close db")

@pytest.fixture(scope="module")
def db_connection():
    db = TestDB()
    db.init_db()
    try:
        yield db.get_connection()
    finally:
        db.shutdown()
    
def test_db_1(db_connection):
    assert db_connection
    
def test_db_2(db_connection):
    assert db_connection
```

    ============================= test session starts ==============================
    platform linux -- Python 3.7.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
    rootdir: /home/npytincev/lectures-2020-spring/07.2.TestingAndLogging
    collected 2 items
    
    Testing.py init db
    ..close db
    
    
    ============================== 2 passed in 0.01s ===============================


Так же в `pytest` есть разные встроенные фикстуры. [Список лежит здесь](https://docs.pytest.org/en/stable/fixture.html). Наиболее интересные:
* monkeypatch - временно можифицирует методы классов, модулей и т.д.
* testdir - создает верменную директорию для каждого теста, которую потом чистит



## 4. Тестирование исключений, сравнение флотов, манкипатчинг

Следующий пункт нашей каты:
- Метод `greet` должен возвращать ошибку если имя - пустая строка (или строка с пробелами)

Для тестирования исключений есть специальная функциональность:


```python
%%run_pytest[clean] -q

@pytest.fixture(scope="module")
def greeter():
    yield Greeter()

def test_greet_raises_value_error_on_empty_string(greeter):
    with pytest.raises(ValueError):
        greeter.greet("")
```

    F                                                                        [100%]
    =================================== FAILURES ===================================
    ________________ test_greet_raises_value_error_on_empty_string _________________
    
    greeter = <__main__.Greeter object at 0x7f910f5b0b50>
    
        def test_greet_raises_value_error_on_empty_string(greeter):
            with pytest.raises(ValueError):
    >           greeter.greet("")
    E           Failed: DID NOT RAISE <class 'ValueError'>
    
    <ipython-input-39-5e9e4ef9f063>:7: Failed
    =========================== short test summary info ============================
    FAILED Testing.py::test_greet_raises_value_error_on_empty_string - Failed: DI...
    1 failed in 0.01s


По тексту отчета видим, что тест ожидал исключения, но его не было. Починим тест:


```python
class Greeter:
    def greet(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Empty name!")
        return "Hello " + name
```


```python
%%run_pytest[clean] -q

@pytest.fixture(scope="module")
def greeter():
    yield Greeter()

def test_greet_raises_value_error_on_empty_string(greeter):
    with pytest.raises(ValueError):
        greeter.greet("")
```

    .                                                                        [100%]
    1 passed in 0.00s


ок, остался последний пункт нашей каты:
 - Метод `greet` возвращает "Good evening <имя>" если текущее время - 18:00-22:00

Реализация такого пункта скорее всего будет вызывать `datetime.now()` где-то внутри. Чтобы обеспечить в тесте нужное нам поведение - используем специяльную фикстуру `monkeypatch`. Подробно про неё можно почитать [тут](https://docs.pytest.org/en/latest/monkeypatch.html).


```python
%%run_pytest[clean] -q

import datetime

@pytest.fixture(scope="module")
def greeter():
    yield Greeter()

def test_greeting_is_good_evening_in_evening(monkeypatch, greeter):
    fake_time =  datetime.datetime(2020, 11, 10, 19)
    class mydatetime:
        @classmethod
        def now(cls):
            return fake_time

    monkeypatch.setattr(datetime, 'datetime', mydatetime)
    assert greeter.greet("Mike").startswith("Good evening")
```

    F                                                                        [100%]
    =================================== FAILURES ===================================
    ___________________ test_greeting_is_good_evening_in_evening ___________________
    
    monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f90f3d4cad0>
    greeter = <__main__.Greeter object at 0x7f90f3d4c990>
    
        def test_greeting_is_good_evening_in_evening(monkeypatch, greeter):
        
            class mydatetime:
                @classmethod
                def now(cls):
                    return datetime(2020, 11, 10, 19)
        
            monkeypatch.setattr(datetime, 'datetime', mydatetime)
        
    >       assert greeter.greet("Mike").startswith("Good evening")
    E       AssertionError: assert False
    E        +  where False = <built-in method startswith of str object at 0x7f90f3d4c5b0>('Good evening')
    E        +    where <built-in method startswith of str object at 0x7f90f3d4c5b0> = 'Hello Mike'.startswith
    E        +      where 'Hello Mike' = <bound method Greeter.greet of <__main__.Greeter object at 0x7f90f3d4c990>>('Mike')
    E        +        where <bound method Greeter.greet of <__main__.Greeter object at 0x7f90f3d4c990>> = <__main__.Greeter object at 0x7f90f3d4c990>.greet
    
    <ipython-input-47-1975bd68bb5b>:16: AssertionError
    =========================== short test summary info ============================
    FAILED Testing.py::test_greeting_is_good_evening_in_evening - AssertionError:...
    1 failed in 0.01s



```python
import datetime

class Greeter:
    def greet(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Empty name!")
        hour = datetime.datetime.now().hour
        if 19 <= hour <= 22:
            return "Good evening " + name
        return "Hello " + name
```


```python
%%run_pytest[clean] -q

import datetime

@pytest.fixture(scope="module")
def greeter():
    yield Greeter()

def test_greeting_is_good_evening_in_evening(monkeypatch, greeter):
    fake_time =  datetime.datetime(2020, 11, 10, 19)
    class mydatetime:
        @classmethod
        def now(cls):
            return fake_time

    monkeypatch.setattr(datetime, 'datetime', mydatetime)
    assert greeter.greet("Mike").startswith("Good evening")
```

    .                                                                        [100%]
    1 passed in 0.00s


Посмотрим, что со старыми тестами


```python
%%run_pytest[clean] -q

@pytest.fixture(scope="module")
def greeter():
    yield Greeter()

@pytest.mark.parametrize("name", ["Mike", "John", "Greg"])
def test_greet_returns_name_with_greeting(greeter, name):
    assert Greeter().greet(name) == "Hello " + name


@pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                         ids=["no spaces", "left space", "right space", 
                              "two-side space", "double space", "two-sided double space"])
def test_greet_removes_leading_and_trailing_spaces_from_name(greeter, name):
    greeted_name = greeter.greet(name).split(" ", 1)[1]
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
```

    FFF......                                                                [100%]
    =================================== FAILURES ===================================
    _________________ test_greet_returns_name_with_greeting[Mike] __________________
    
    greeter = <__main__.Greeter object at 0x7f90f3ac3510>, name = 'Mike'
    
        @pytest.mark.parametrize("name", ["Mike", "John", "Greg"])
        def test_greet_returns_name_with_greeting(greeter, name):
    >       assert Greeter().greet(name) == "Hello " + name
    E       AssertionError: assert 'Good evening Mike' == 'Hello Mike'
    E         - Hello Mike
    E         + Good evening Mike
    
    <ipython-input-57-50b48232e1f0>:7: AssertionError
    _________________ test_greet_returns_name_with_greeting[John] __________________
    
    greeter = <__main__.Greeter object at 0x7f90f3ac3510>, name = 'John'
    
        @pytest.mark.parametrize("name", ["Mike", "John", "Greg"])
        def test_greet_returns_name_with_greeting(greeter, name):
    >       assert Greeter().greet(name) == "Hello " + name
    E       AssertionError: assert 'Good evening John' == 'Hello John'
    E         - Hello John
    E         + Good evening John
    
    <ipython-input-57-50b48232e1f0>:7: AssertionError
    _________________ test_greet_returns_name_with_greeting[Greg] __________________
    
    greeter = <__main__.Greeter object at 0x7f90f3ac3510>, name = 'Greg'
    
        @pytest.mark.parametrize("name", ["Mike", "John", "Greg"])
        def test_greet_returns_name_with_greeting(greeter, name):
    >       assert Greeter().greet(name) == "Hello " + name
    E       AssertionError: assert 'Good evening Greg' == 'Hello Greg'
    E         - Hello Greg
    E         + Good evening Greg
    
    <ipython-input-57-50b48232e1f0>:7: AssertionError
    =========================== short test summary info ============================
    FAILED Testing.py::test_greet_returns_name_with_greeting[Mike] - AssertionErr...
    FAILED Testing.py::test_greet_returns_name_with_greeting[John] - AssertionErr...
    FAILED Testing.py::test_greet_returns_name_with_greeting[Greg] - AssertionErr...
    3 failed, 6 passed in 0.03s


Всё падает, потому что чейчас вечер. Выставим для тестов дефолтное время при помощи фикстур:


```python
%%run_pytest[clean] -q

import datetime


@pytest.fixture(scope="function")
def set_time(monkeypatch):
    def set_time_(time):
        class mydatetime:
            @classmethod
            def now(cls):
                return time

        monkeypatch.setattr(datetime, 'datetime', mydatetime)
    yield set_time_

    
@pytest.fixture(scope="function")
def set_day_time(set_time):
    yield set_time(datetime.datetime(2020, 10, 10, 10))
    

@pytest.mark.parametrize("name", ["Mike", "John", "Greg"])
def test_greet_returns_name_with_greeting(set_day_time, greeter, name):
    assert Greeter().greet(name) == "Hello " + name


@pytest.mark.parametrize("name", ["Mike", " Mike", "Mike ", " Mike ", "  Mike", "  Mike  "],
                         ids=["no spaces", "left space", "right space", 
                              "two-side space", "double space", "two-sided double space"])
def test_greet_removes_leading_and_trailing_spaces_from_name(set_day_time, greeter, name):
    greeted_name = greeter.greet(name).split(" ", 1)[1]
    assert not greeted_name.startswith(" ") and not greeted_name.endswith(" ")
    

def test_greeting_is_good_evening_in_evening(set_time, monkeypatch, greeter):
    set_time(datetime.datetime(2020, 11, 10, 19))
    assert greeter.greet("Mike").startswith("Good evening")
```

    ..........                                                               [100%]
    10 passed in 0.02s


### Сравнение float

 Сравнение `float` сталось за кадром - разберем его отдельно.
 Из-за ошибок округления `float` трудно сравнивать через `==`


```python
%%run_pytest[clean] -q
def test_float():
    assert 0.1 + 0.2 == 0.3
```

    F                                                                                                                                                                                                    [100%]
    ================================================================================================= FAILURES =================================================================================================
    ________________________________________________________________________________________________ test_float ________________________________________________________________________________________________
    
        def test_float():
    >       assert 0.1 + 0.2 == 0.3
    E       assert (0.1 + 0.2) == 0.3
    
    <ipython-input-41-d4fdc5effe72>:2: AssertionError
    1 failed in 0.02s


Исправить ситуацию поможет `pytest.approx`


```python
%%run_pytest[clean] -q
def test_float():
    assert 0.1 + 0.2 == pytest.approx(0.3)
```

    .                                                                                                                                                                                                    [100%]
    1 passed in 0.01s


`pytest.approx` так же работает и с коллекциями:


```python
%%run_pytest[clean] -q
def test_float():
    assert [0.1 + 0.2, 0.5] == pytest.approx([0.3, 0.5])
```

    .                                                                                                                                                                                                    [100%]
    1 passed in 0.01s


## Итого

Мы сделали небольшую кату, познакомились с TDD и основной функциональностью `pytest`:

* Как пайтест находит тесты
* Ассерты `pyteset`
* Параметризация тестов
* Фикстуры 
* Тестирование исключений
* Манкипатчинг

Какие в итоге профиты у тестов:
 - Тесты помогают следить за тем что код соответствует спецификации
 - Тесты позволяют рефакторить код и не бояться при этом посадить баг
 - Тесты документируют код
 
Что осталось за кадром:
 - Виды тестов - юнит, интеграционные и т.д.
 - Настройка тестов в ci/cd
 - Плагины pytest


```python

```
