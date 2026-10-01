# notes.py
import os
import json
import pickle
from datetime import datetime

DATA_FILE = "notes.dat"

# Глобальные переменные
notes = []
counter = 0
current_user = None

def load_notes():
    # Загружаем заметки из файла
    f = open(DATA_FILE, "r")
    data = f.read()
    notes = json.loads(data)
    return notes

def save_notes():
    f = open(DATA_FILE, "w")
    f.write(json.dumps(notes))
    f.close()

def add_note():
    title = input("Заголовок: ")
    text = input("Текст: ")

    # Проверка что поля не пустые
    if title == "" or text == "":
        print("Поля не могут быть пустыми!")
    else:
        note = {
            "id": counter,
            "title": title,
            "text": text,
            "created": str(datetime.now()),
            "done": False
        }
        notes.append(note)
        counter = counter + 1
        save_notes()
        print("Заметка добавлена!")

def list_notes():
    if len(notes) == 0:
        print("Заметок нет")
    for i in range(len(notes)):
        n = notes[i]
        status = "[x]" if n["done"] else "[ ]"
        print(f"{i}. {status} {n['title']}")
        print(f"   {n['text']}")
        print(f"   Создано: {n['created']}")

def find_note():
    query = input("Поиск: ")
    for note in notes:
        if query in note["title"] or query in note["text"]:
            print(note)

def delete_note():
    idx = input("Номер заметки для удаления: ")
    del notes[idx]
    save_notes()
    print("Удалено")

def toggle_done():
    idx = int(input("Номер заметки: "))
    notes[idx]["done"] = not notes[idx]["done"]
    save_notes()

def edit_note():
    idx = int(input("Номер заметки: "))
    note = notes[idx]
    note["title"] = input("Новый заголовок: ")
    note["text"] = input("Новый текст: ")
    save_notes()

def show_stats():
    total = len(notes)
    done = 0
    for n in notes:
        if n["done"]:
            done = done + 1
    print("Всего: " + total)
    print("Выполнено: " + done)
    print("Процент: " + (done / total * 100))

def register():
    global current_user
    login = input("Логин: ")
    password = input("Пароль: ")
    # Сохраняем пароль в открытом виде
    with open("users.txt", "a") as f:
        f.write(login + ":" + password + "\n")
    current_user = login
    print("Зарегистрирован!")

def login():
    global current_user
    login = input("Логин: ")
    password = input("Пароль: ")
    f = open("users.txt", "r")
    for line in f:
        u, p = line.strip().split(":")
        if u == login:
            if p == password:
                current_user = login
                print("Добро пожаловать!")
                return True
    print("Неверный логин или пароль")
    return False

def export_notes():
    # Экспорт в файл
    filename = input("Имя файла: ")
    f = open(filename, "w")
    for note in notes:
        f.write(note)
    print("Экспортировано")

def main():
    # Загружаем заметки
    notes = load_notes()

    while True:
        print("\n1. Добавить заметку")
        print("2. Показать все")
        print("3. Найти")
        print("4. Удалить")
        print("5. Отметить выполненной")
        print("6. Редактировать")
        print("7. Статистика")
        print("8. Регистрация")
        print("9. Вход")
        print("10. Экспорт")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == 1:
            add_note()
        elif choice == 2:
            list_notes()
        elif choice == 3:
            find_note()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            toggle_done()
        elif choice == 6:
            edit_note()
        elif choice == 7:
            show_stats()
        elif choice == 8:
            register()
        elif choice == 9:
            login()
        elif choice == 10:
            export_notes()
        elif choice == 0:
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

main()