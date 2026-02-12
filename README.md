# Инструкция: как воспользоваться шаблонным репозиторием Django

## 1. Склонировать шаблон
```bash
git clone https://github.com/M1ks1i/template_d_j_a_n_g_o_project.git myproject
cd myproject
```

## 2. Создать виртуальное окружение
```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\Activate.ps1
```

## 3. Установить зависимости
```bash
pip install -r requirements.txt
```

## 4. Миграции и суперпользователь
```bash
python manage.py migrate
python manage.py createsuperuser
```

## 5. Запуск
```bash
python manage.py runserver
```
