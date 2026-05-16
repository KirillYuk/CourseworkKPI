# 📊 Financial Data Monitoring System
## Тема
Розробка бібліотеки для моніторингу криптовалютного ринку засобами Python.


## Можливості
- генерація потоку ринкових даних <sup style="color:gray;">local</sup>
- синхронний та асинхронний моніторинг <sup style="color:gray;">local</sup>
- розрахунок RSI та сигналів BUY / SELL / NEUTRAL <sup style="color:gray;">local</sup>
- керовані alert-и через EventEmitter <sup style="color:gray;">local</sup>
- BiQueue для перегляду alert-ів за пріоритетом і порядком появи <sup style="color:gray;">local</sup>
- CSV history processing без завантаження всього файлу в пам'ять <sup style="color:gray;">local</sup>
- async utilities для обробки списків символів <sup style="color:gray;">local</sup>
- AuthProxy для роботи з реальним API
- memoization cache для локальних даних та API-запитів
- logging decorator для логування API-запитів і помилок

<sup style="color:gray;">local - реалізовано тільки для локальних данних (задля збереження безкоштовного ліміту використання API запитів, бо я бідний студент)</sup>

## Встановлення
```
pip install -e .
```

## Налаштування API
Створити файл `.env` у корені проєкту:

```
API_KEY=your_api_key_here
```

## Запуск
```
python demo/main.py
```

## Команди
- stream
- async_stream
- info
- history
- price
- scan
- exit

## Керування async_stream
- q: зупинити stream
- s: увімкнути/вимкнути price threshold alerts
- a: показати стан alert queue

## Preview

### Async stream
![stream preview](preview/stream.gif)

### API request
![API request preview](preview/apir.gif)
## Технології
- [Python 3.12+](https://www.python.org/)
- [rich](https://github.com/textualize/rich)
- [requests](https://github.com/psf/requests)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [pynput](https://github.com/moses-palmer/pynput)

## Відповідність вимогам
Task 1: price_generator і run з timeout.

Task 2: pyproject, license, структура src/demo.

Task 3: memoize з max_size, LRU/LFU, TTL, custom policy.

Task 4: BiQueue з highest/lowest/oldest/newest.

Task 5: async_filter і callback variant.

Task 6: CSV stream processing.

Task 7: EventEmitter з multiple listeners і unsubscribe.

Task 8: AuthProxy з API Key/JWT/OAuth.

Task 9: logging decorator для sync/async функцій.


## Ліцензія
[MIT](LICENSE)

## Автор
Студент групи ІМ-51 Юхимчук Кирило Сергійович **[Telegram](https://t.me/saaayq)**

ФІОТ НТУУ "КПІ"
