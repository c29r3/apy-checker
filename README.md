### README.md

---

#### English Version

# APY Monitoring Telegram Bot

This Telegram bot is designed to monitor APY (Annual Percentage Yield) values from two sources: Solend and Kamino. It periodically collects data and sends notifications if the APY values meet certain conditions.

## Features

### Periodic Data Collection
- The bot periodically fetches APY values for USDC and USDT from Solend and Kamino.
- The data is cached for subsequent use and comparison.

### Notifications
- The bot sends notifications on Telegram if the APY values from one of the sources are less than or equal to the specified minimum threshold (`MIN_APY_THRESHOLD`).
- The bot also sends notifications if the APY change (in percentage) between two consecutive measurements exceeds the specified threshold (`PERCENTAGE_CHANGE`).

### Command Handling
- `/start`: Sends a welcome message and provides buttons for interacting with the bot.
- `/apy`: Sends the current cached APY values for Solend and Kamino.
- `/set_threshold`: Allows authorized users to set a new minimum APY threshold.
- `/set_percentage_change`: Allows authorized users to set a new APY percentage change threshold.
- `/show_config`: Displays the current bot configuration (authorized users, thresholds, and check interval).

### Authorization and Request Frequency Control
- The bot supports a list of authorized users who can change settings.
- It controls the frequency of user requests to prevent spam.

## Technical Details

- **Logging**: Logs all important events and errors for easier diagnosis and debugging.
- **Multithreading**: The bot runs in a separate thread, allowing it to process commands and collect data simultaneously.
- **Configuration Parameters**: Loaded from `config.json`, including Telegram token, chat ID, check interval, APY thresholds, and authorized users list.

### Main Dependencies

- `requests`: For making HTTP requests to Solend and Kamino APIs.
- `telebot`: For working with the Telegram Bot API.
- `threading`: For organizing multithreading.
- `logging`: For event and error logging.
- `json`: For working with the configuration file.
- `pytz`: For working with time zones.

This bot is useful for automatic monitoring of financial indicators and receiving notifications about significant APY changes.

---

#### Russian Version

# Телеграм-бот для мониторинга APY

Этот телеграм-бот предназначен для мониторинга значений APY (годовая процентная доходность) из двух источников: Solend и Kamino. Он периодически собирает данные и отправляет уведомления, если значения APY удовлетворяют определённым условиям.

## Функции

### Периодический сбор данных
- Бот периодически запрашивает значения APY для USDC и USDT из Solend и Kamino.
- Данные кэшируются для последующего использования и сравнения.

### Уведомления
- Бот отправляет уведомления в Telegram, если значения APY из одного из источников меньше или равны заданному минимальному порогу (`MIN_APY_THRESHOLD`).
- Бот также отправляет уведомления, если изменение APY (в процентах) между двумя последовательными замерами превышает заданный порог (`PERCENTAGE_CHANGE`).

### Обработка команд
- `/start`: Отправляет приветственное сообщение и предоставляет кнопки для взаимодействия с ботом.
- `/apy`: Отправляет текущие кэшированные значения APY для Solend и Kamino.
- `/set_threshold`: Позволяет авторизованным пользователям установить новый минимальный порог APY.
- `/set_percentage_change`: Позволяет авторизованным пользователям установить новый порог изменения APY в процентах.
- `/show_config`: Показывает текущую конфигурацию бота (авторизованные пользователи, пороги и интервал проверки).

### Авторизация и контроль частоты запросов
- Бот поддерживает список авторизованных пользователей, которые могут изменять настройки.
- Контролирует частоту запросов от пользователей, чтобы предотвратить спам.

## Технические детали

- **Логирование**: Ведется логирование всех важных событий и ошибок, что упрощает диагностику и отладку.
- **Многопоточность**: Бот работает в отдельном потоке, что позволяет ему параллельно обрабатывать команды и собирать данные.
- **Параметры конфигурации**: Загружаются из `config.json` и включают токен Telegram, идентификатор чата, интервал проверки, пороги APY и список авторизованных пользователей.

### Основные зависимости

- `requests`: Для выполнения HTTP-запросов к API Solend и Kamino.
- `telebot`: Для работы с Telegram Bot API.
- `threading`: Для организации многопоточности.
- `logging`: Для логирования событий и ошибок.
- `json`: Для работы с конфигурационным файлом.
- `pytz`: Для работы с временными зонами.

Этот бот может быть полезен для автоматического мониторинга финансовых показателей и получения уведомлений о значимых изменениях APY.
