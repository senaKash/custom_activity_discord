# custom_activity_discord
# Кастомная\красивая активность в дискорде

Итак, все довольно просто. 
 - установим библиотеку pypresence
  ```python
    pip install pypresence
   ```
 - заходим в корневую папку с Python (`USER` замените на ваше имя пользовотеля) c:\users\\`USER`\appdata\local\programs\python\python39\
 
   далее lib -> site-packages -> pypresence
  
    мой путь: c:\users\\`USER`\appdata\local\programs\python\python39\lib\site-packages\pypresence
  
  - скачиваем последнюю актуальную версию библиотеки с [GitHub](https://github.com/qwertyquerty/pypresence)
  - распаковываем содержимое архива в pypresence с заменой
  - удаляем папку `__pycache__` из pypresence
  
  всё это нужно было сделать для того, чтобы не _словить ошибок от библиотеки_
  
  - скачиваем код из репозитория
  
## Настройка discord_activity.py

- заходим на портал разработчиков _https://discord.com/developers/applications_
- нажимаем на кнопку `New Application` в правом верхнем углу и создаем приложение
- на появившейся странице копируем `APPLICATION ID` и вставляем в 7 строку _discord_activity.py_
- переходим в `Rich Presence` через кнопку в левом меню
- добавляем картинки через `Add images`. Теперь в полях **large_image** и **small_image** можно указать названия загруженных картинок
  
 
 
 Если вы хотите более детально разобраться с `Discord RPC`, читайте -> [pypresence](https://qwertyquerty.github.io/pypresence/html/doc/client.html)
