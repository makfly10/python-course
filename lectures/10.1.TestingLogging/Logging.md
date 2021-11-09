## Логгирование


```python
import sys
import logging

logger = logging.getLogger('my_logger')

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setLevel(logging.INFO)
logger.addHandler(stdout_handler)

logger.warning('Watch out!')
```

    Watch out!


### Логгирование и его уровни

Логгировать можно при помощи следующих методов:
1. `logger.debug()`
2. `logger.info()`
3. `logger.warning()`
4. `logger.error()`
5. `logger.critical()`
6. `logger.exception()`


С самого маленького до самого большого

|Уровень | Когда используется|
|:------ |:------------------|
|`DEBUG`|Для диагностической информации|
|`INFO`|Для подтверждения того, что всё работает как запланировано|
|`WARNING`|Когда нужно предупредить что вскоре возможна поломка или программа используется не совсем так как нужно|
|`ERROR`|Для логгирования сепъезных ошибок, из-за которых программа теряет часть функциональности|
|`CRITICAL`|Для логгирования ошибок, после которых программа не может продолжать работу|

Стандартный уровень логгирования - `WARNING`


```python
logger.info('Will not be printed')
logger.warning('Will be printed')
```

    Will be printed


Поменяем уровень логгирования:


```python
logger.setLevel(logging.INFO)
logger.info('Will not be printed')
logger.warning('Will be printed')
logger.setLevel(logging.WARNING)
```

    Will not be printed
    Will be printed



```python
logger.log(logging.WARNING, 'Will be printed')
```

    Will be printed


logging.exception немножко особенный - он добавляет информацию о последнем исключении и traceback


```python
try:
    1 / 0
except:
    logger.exception("Cought error:")
```

    Cought error:
    Traceback (most recent call last):
      File "<ipython-input-5-7090cd0566ef>", line 2, in <module>
        1 / 0
    ZeroDivisionError: division by zero


### Логгирование в файл и хэндлеры

Научимся логгировать в файл


```python
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)  # Выставляем уровень сообщений, которые будут логгироваться в файл.
logger.addHandler(fh)
```


```python
logger.setLevel(logging.DEBUG)
logger.debug("Debug message")  # Не попадет в stdout, зато попадет в файл
print ("debug.log contents:")

with open("debug.log") as f:
    for l in f.readlines():
        print(l)
```

    debug.log contents:
    Debug message
    


Другие полезные хендлеры из библиотеки `logging`:

* `StreamHandler` - используется для логгирования в `stderr` и `stdout`
* `RotatingFileHandler` - Работает вкак файл хендлер, но при этом если файл, в который пишет логгер, достигнет определенного размера, начнет писать в новый файл. Старый файл либо удалит, либо оставит как бекап. Число бэкапов настраивается. 
* `TimedRotatingFileHandler` - Работает как логгер выше, но файлы делятся не по размеру, а по времени записей
* `NullHandler` - Используется чтобы заглушить какой-нибудь логгер

### Фильтрация

На логгеры и хендлеры можно вешать дополнительные фильтры


```python
logger.warning("Not important warning")

class OnlyImportantFilter(logging.Filter):
    def filter(self, record):
        return not record.getMessage().startswith('Not important')

logger.addFilter(OnlyImportantFilter())
logger.warning("Not important warning")
```

    Not important warning


### Форматирование

Для хендлера можно выставить формат при помощи метода `setFormatter`


```python
format_example_logger = logging.getLogger('format_example')
format_example_logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
format_example_logger.addHandler(ch)

format_example_logger.debug('debug message')
format_example_logger.info('info message')
format_example_logger.warning('warn message')
format_example_logger.error('error message')
format_example_logger.critical('critical message')
```

    2019-10-29 15:15:34,721 - format_example - DEBUG - debug message
    2019-10-29 15:15:34,723 - format_example - INFO - info message
    2019-10-29 15:15:34,723 - format_example - WARNING - warn message
    2019-10-29 15:15:34,725 - format_example - ERROR - error message
    2019-10-29 15:15:34,725 - format_example - CRITICAL - critical message


`Formatter` принимает три аргумента: `fmt`, `datefmt`, `style`.

`fmt` - это шаблон записи. Если в `style` стоит %, форматирование произойдет при помощи %. Если `style` равен {, форматирование будет произведено через `.format()`. В `fmt` можно добавить любые атрибуты класса [`LogRecord`](https://docs.python.org/3/library/logging.html#logrecord-attributes)

`datefmt` - шаблон для форматирования дат, по дефолту `%Y-%m-%d %H:%M:%S`

### Дерево логгеров

Когда вы создаете логгер, он добавляется в дерево логгеров. Путь логгера в дереве определяется по его имени. Если логгер назван `a.b.c`, то он станет дочерним логгером логгера `b`, который в свою очередь является дочерним логгером логгера `a`. `a` будет дочерним логгером корневого логгера, который всегда есть по умолчанию

Если вы создаете логгер и никак его не настраиваете - он будет наследовать настройки родителя. 

Если вы создаете логгер для какого-то модуля, то удобно будет назвать его по имени этого модуля:
```Python
logger = logging.getLogger(__name__)
```
В этом случае иерархия модулей будет совпадать с иерархией логгеров и будет интуитивно понятно откуда пришло то или иноее сообщение. Так же можно будет легко сконфигурировать логгирование в __init__ файле.

### Всё вместе

<img src="logging_flow.png">

### Оптимизация логгирования

Если в сообщение при логгировании нужно добавить результаты каких-то тяжелых функций, лучше делать это так:


```python
def expensive_func1():
    pass

if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Message with %s', expensive_func1())
```

Во-первых, мы защищаемся от вычисления функции в том случае, если логгирование отключено. Во-вторых, мы не форматируем строку при каждом вызове логгера - он отформатирует её сам в том случае, если она не будет отфильтрована.
