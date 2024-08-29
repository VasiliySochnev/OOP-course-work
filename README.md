# **Курсовая работа. Раздел 4 ООП.** 
_Этот проект предназначен для получения и обработки вакансий, опубликованных на сайте hh.ru._

___
### **Установка:**
Для установки проекта OOP course work, следуйте инструкциям:

1. Склонируйте репозиторий на своем компьютере:

`git clone https://github.com/MichaelGorbunov/CW_4_OOP.git`

2. Перейдите в папку с проектом:

`OOP course work`

3. Создайте и активируйте виртуальное окружение:

`poetry init`

`poetry shell`

4. Установите зависимости проекта:

`poetry install`

___
### **Описание работы**
1. Выберите источник списка вакансий: hh.ru или локальный файл в директории DATA.
2. При выборе в качестве источника локального файла отобразится список файлов в директории. Если файлов нет, то программа завершит работу. Если файлы имеются, то при вводе индекса файла его можно загрузить для дальнейшей обработки.
3. При выборе в качестве источника hh.ru следует ввести наименование вакансии, например "python разработчик" или "программист".
4. Далее вакансии будут отсортированы по значению заработной платы и будет предложено вывести их топ. В дальнейшей обработке будут участвовать только эти вакансии.
5. Вакансии можно отфильтровать по покрытию зарплатной вилки, от минимально - необходимого до желаемого уровня. Если в качестве аргумента ввести "0", то будут учитыватся вакансии где критерий зарплаты не указан.
6. Следующим шагом будет предложено осуществить фильтрацию по ключевым словам. Поиск происходит по принципу "ИЛИ", то есть будут отобраны вакансии где найдено хотя-бы одно ключевое слово.
7. Программа выводит список вакансий, сохраняет его и завершает работу.
___
### **Ограничения:**
1. Проект разрабатывался как учебный, поэтому с сайта загружается первые 100 вакансий.
2. При сохранении имя файла формируется автоматически и состоит из названия указанной в поиске вакансии, даты в формате YYYY_MM_DD-hh_mm, и расширения ".vac". Файл повторяет структуру файлов формата JSON.
___
## **Лицензия**

Этот проект можно использовать безвозмездно для любых, 
не противоречащих законодательству целей.