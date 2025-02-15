"""документация+ к каждой функций"""

def add_new_student():
  name=input("name:")
  if name not in school_class:
    school_class[name]=()
    print('Студент успешно создан')
  else:
    print('Уже был создан')

def add_new_grade():
  name=input("name:")
  if name in school_class:
    grade=int(input('grade (1-10):'))
    school_class[name]+=(grade, )
    print('Оценка успешно добавлена')
  else:
    print('студента еще не существует')

def show_student_avg():
  if len(school_class)==0:
    print('Оценок не содержится')
  elif len(school_class)>0:
    for name in school_class.keys():
      grades=school_class[name]
      if len(grades)>0:
        print(name)
        print(school_class[name])
        print('avg:')
        print(sum(grades)/len(grades))
      else:
        print('У', name, 'нет оценок')
    



def main():
  school_class={}

  menu="""
  1 - добавить нового студента
  2 - добавить оценку
  3 - посчитать средний балл
  -1 - выход"""

  oper=int(input(menu))

  while oper!=-1:
      if oper==1:
          add_new_student()
      elif oper==2:
          add_new_grade()
      elif oper==3:
          show_student_avg()
      oper=int(input(menu))


main()
