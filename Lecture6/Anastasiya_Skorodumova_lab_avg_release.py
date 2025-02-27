"""документация+ к каждой функций"""
""" Программа студенты с возможностью добавлять/удалять/выводить
список студентовб добавлять оценки и считать средний балл
Автор: Anastasiya
Cуть - словарь значений студент-оценка"""

def add_new_student():
  """Функция добавления студента."""
  name = input("Введите имя студента:")
  if name not in school_class:
    school_class[name] = ()
    print(f'Студент {name} успешно создан')
  else:
    print('Уже был создан')

def add_new_grade():
  """Функция добавления оценок."""
  name = input("Введите имя студента:")
  if name in school_class:
    grade = int(input('Введите оценку (1-10):'))
    school_class[name] += (grade,)
    print('Оценка успешно добавлена')
  else:
    print('Студента еще не существует')

def show_student_avg():
  if len(school_class) == 0:
    print('Оценок не содержится')
  elif len(school_class) > 0:
    for name in school_class.keys():
      grades = school_class[name]
      if len(grades) > 0:
        print(name)
        print(school_class[name])
        print('Средний балл:')
        print(sum(grades) / len(grades))
      else:
        print('У', name, 'нет оценок')
    
def delete_student():
  """Функйия удаления студента."""
  name = input('Введите имя студента:')
  if name in school_class:
    print(school_class.pop(name))
    print(f'Студент {name} удален')
  else:
    print(f'Студента {name} еще не существует')

def student_list():
  """Функция вывода списка студентов"""
  num = 1
  if len(school_class) != 0:
    for name in school_class.keys():
      print(f"№{num} - {name}")
      num += 1
  else:
    print("Список студентов пуст")

        
def main():
  menu = """
  1 - добавить нового студента
  2 - добавить оценку
  3 - посчитать средний балл
  4 - вывести список студентов
  5 - удалить студента
  -1 - выход \n"""

  oper = int(input(menu))

  while oper != -1:
    if oper == 1:
      add_new_student()
    elif oper == 2:
      add_new_grade()
    elif oper == 3:
      show_student_avg()
    elif oper == 4:
      student_list()
    elif oper == 5:
      delete_student()
    oper = int(input(menu))

school_class = {}
main()
