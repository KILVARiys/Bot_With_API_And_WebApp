# Telegram Bot with Weather WebApp

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Aiogram](https://img.shields.io/badge/Aiogram-3.x-00BFFF?style=for-the-badge&logo=telegram&logoColor=white)
  ![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-FF6F00?style=for-the-badge&logo=openweathermap&logoColor=white)
  ![HTML5](https://img.shields.io/badge/HTML5-WebApp-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  ![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Hosting-222222?style=for-the-badge&logo=githubpages&logoColor=white)
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
  [![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/your_bot_username)
  
  <h3>Асинхронный Telegram бот для просмотра погоды с интерактивным WebApp интерфейсом</h3>
  
  <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/screenshots/demo.gif" alt="Демонстрация работы" width="600">
  
</div>

---

## О проекте

Проект представляет собой Telegram бота, который получает актуальную информацию о погоде через OpenWeatherMap API и отображает её двумя способами:
- **Текстовое сообщение** с красивым форматированием и эмодзи
- **Интерактивный WebApp** с динамическим дизайном, адаптирующимся под тип погоды и тему Telegram

---

## Возможности
<div align="center">
<table>
  <tr>
    <td align="center"></td>
    <td><b>Поиск по городу</b> - любой город мира</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td><b>Температура</b> - текущая и ощущается как</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td><b>Скорость ветра</b> - точные данные</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td><b>Описание погоды</b> - ясно, облачно, дождь и т.д.</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td><b>Динамический WebApp</b> - меняет цвет и фон под погоду</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td><b>Адаптация под тему</b> - светлая/темная тема Telegram</td>
  </tr>
</table>


## Технологический стек

<div align="center">
  
  | Технология | Назначение |
  |------------|------------|
  | **Python 3.13+** | Основной язык программирования |
  | **Aiogram 3.x** | Фреймворк для Telegram ботов |
  | **Aiohttp** | Асинхронные HTTP запросы |
  | **OpenWeatherMap API** | Источник данных о погоде |
  | **HTML5/CSS3** | Верстка WebApp интерфейса |
  | **JavaScript (ES6)** | Логика WebApp, работа с Telegram API |
  | **GitHub Pages** | Хостинг WebApp |
  
</div>

---

## Настройка конфигурации

Откройте файл main.py и замените токены:

  TOKEN = 'ваш_токен_бота'        # от @BotFather  
  API_TOKEN = 'ваш_api_ключ'      # от OpenWeatherMap  

## Использование

1️. Отправьте команду /start  
2️.  Используйте /weather для поиска погоды  
3. Введите название города (например, "Москва")  
4. Получите информацию о погоде  
5. Нажмите кнопку для открытия WebApp  

## Быстрый старт

### Предварительные требования

- Python 3.13 или выше
- Токен Telegram бота (получить у [@BotFather](https://t.me/BotFather))
- API ключ [OpenWeatherMap](https://openweathermap.org/api) (бесплатный)

### Пошаговая установка

#### 1. Клонирование репозитория

```bash
git clone https://github.com/KILVARiys/Bot_With_API_And_WebApp.git
cd Bot_With_API_And_WebApp
