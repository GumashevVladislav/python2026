Время затраченное на выполнение: 0:22

result: 0/100

1) **Сильные стороны**
- Студент начал работу над заданием, попытался использовать абстрактный класс и импортировать необходимые модули.

2) **Ошибки и недочёты**

**Блокирующие (ломает выполнение требований задания)**
- Файл не является рабочим Python-кодом. Предоставлен только фрагмент с синтаксическими ошибками, отсутствует основная часть реализации.
- Импорт некорректен: `from abc import ABS` (должно быть `ABC`), `from typing import list` (регистр не имеет значения, но обычно импортируют `List` для аннотаций, хотя в данном задании типизация не требовалась).
- Строка `sender_name("MyService")` находится вне класса и не является валидным Python-кодом.
- Определение класса `NotificationChannel(ABS)` не имеет двоеточия в конце и тело класса не оформлено корректно.
- Метод `__init__` написан как `_init_` (неверное количество подчёркиваний) и не имеет корректного синтаксиса.
- Отсутствуют все требуемые классы (`EmailChannel`, `SMSChannel`, `NotificationService`) и демонстрация работы.
- Код не запустится из-за синтаксических ошибок.

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- Не реализованы абстрактный метод `send`, обычный метод `format_message`, классы-наследники и сервис. Задание не выполнено по существу.

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- Имя файла не соответствует требуемому (`notifications.py`), но это не является критичным, если код рабочий. Однако код нерабочий.

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 0/50 (отсутствует рабочая реализация всех требуемых компонентов)
- Качество кода: 0/30 (код содержит синтаксические ошибки, не структурирован)
- Стиль и тесты: 0/20 (стиль не оценивается из-за отсутствия рабочего кода, тесты не требовались и не предоставлены)

Итог: 0 баллов, так как решение не соответствует условию и не является выполняемым кодом.

4) **Если задание выполнено не полностью**
- Отсутствует полностью: абстрактный класс `NotificationChannel` с методами `send` (абстрактный) и `format_message` (обычный), классы-наследники `EmailChannel` и `SMSChannel` с переопределением `send` и использованием `super()`, класс `NotificationService` с методом `notify_all`, демонстрация работы.
- Сделано частично: предпринята попытка начать абстрактный класс, но с ошибками.

**Вариант полного решения (код):**

```python
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def __init__(self, sender_name: str):
        self.sender_name = sender_name

    def format_message(self, message: str) -> str:
        return f"[{self.sender_name}] {message}"

    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass

class EmailChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_email: str):
        super().__init__(sender_name)
        self.sender_email = sender_email

    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"EMAIL to {recipient}: {formatted_message} (from {self.sender_email})")

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_phone: str):
        super().__init__(sender_name)
        self.sender_phone = sender_phone

    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"SMS to {recipient}: {formatted_message} (from {self.sender_phone})")

class NotificationService:
    def __init__(self, channels: list[NotificationChannel]):
        self.channels = channels

    def notify_all(self, recipient: str, message: str) -> None:
        for channel in self.channels:
            channel.send(recipient, message)

# Демонстрация работы
if __name__ == "__main__":
    email_channel = EmailChannel("MyService", "noreply@myservice.com")
    sms_channel = SMSChannel("MyService", "+1234567890")
    service = NotificationService([email_channel, sms_channel])
    service.notify_all("user@example.com", "Hello! Your order is ready.")
    service.notify_all("+0987654321", "Reminder: meeting at 3 PM.")
```
