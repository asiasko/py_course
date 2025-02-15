Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
school_class={}
name=input('name:')
name:vasia pupkin
name
'vasia pupkin'
#(name:grades, name:grades)
grade=int(input('grade:'))
grade:7
school_class[name]=(grade,)
grade=int(input('grade:'))
grade:5
school_class[name]+=(grade,)
school_class
{'vasia pupkin': (7, 5)}
school_class[name]
(7, 5)
sum(school_class[name])/len(school_class[name])
6.0
menu="""
1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход"""
oper=int(input(menu))

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выходwhile oper
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    oper=int(input(menu))
ValueError: invalid literal for int() with base 10: 'while oper'
oper=int(input(menu))

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    oper=int(input(menu))
ValueError: invalid literal for int() with base 10: ''
oper=int(input(menu))

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход1
while oper!=-1:
    if oper==1:
        name=input("name:")
        if name not in school_class:
            school_class[name]=()
            print('Студент успешно создан')
        else:
            print('Уже был создан')
    elif==2:
        
SyntaxError: invalid syntax
while oper!=-1:
    if oper==1:
        name=input("name:")
        if name not in school_class:
            school_class[name]=()
            print('Студент успешно создан')
        else:
            print('Уже был создан')
    elif oper==2:
        name=input("name:")
        if name not in school_class:
            grade=int(input('grade (1-10):'))
            school_class[name]+=(grade, )
            print('Оценка успешно добавлена')
        else:
            print('студента еще не существует')
    elif oper==3
    
SyntaxError: expected ':'
while oper!=-1:
    if oper==1:
        name=input("name:")
        if name not in school_class:
            school_class[name]=()
            print('Студент успешно создан')
        else:
            print('Уже был создан')
    elif oper==2:
        name=input("name:")
        if name not in school_class:
            grade=int(input('grade (1-10):'))
            school_class[name]+=(grade, )
            print('Оценка успешно добавлена')
        else:
            print('студента еще не существует')
    elif oper==3:
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
    oper=int(input(menu))

    
name:dima
Студент успешно создан

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход3
vasia pupkin
(7, 5)
avg:
6.0
У dima нет оценок

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход2
name:dima
студента еще не существует

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход
Traceback (most recent call last):
  File "<pyshell#43>", line 30, in <module>
    oper=int(input(menu))
ValueError: invalid literal for int() with base 10: ''
while oper!=-1:
    if oper==1:
        name=input("name:")
        if name not in school_class:
            school_class[name]=()
            print('Студент успешно создан')
        else:
            print('Уже был создан')
    elif oper==2:
        name=input("name:")
        if name in school_class:
            grade=int(input('grade (1-10):'))
            school_class[name]+=(grade, )
            print('Оценка успешно добавлена')
        else:
            print('студента еще не существует')
    elif oper==3:
        if len(school_class)<1:
            print('Оценок не содержится')
        elif len(school_class)>=1:
            for name in school_class.keys():
                grades=school_class[name]
                if len(grades)>=1:
                    print(name)
                    print(school_class[name])
                    print('avg:')
                    print(sum(grades)/len(grades))
                else:
                    print('У', name, 'нет оценок')
    oper=int(input(menu))

    
name:oleg
студента еще не существует

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход2
name:oleg
студента еще не существует

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход-1
school_class
{'vasia pupkin': (7, 5), 'dima': ()}
while oper!=-1:
    if oper==1:
        name=input("name:")
        if name not in school_class:
            school_class[name]=()
            print('Студент успешно создан')
        else:
            print('Уже был создан')
    elif oper==2:
        name=input("name:")
        if name in school_class:
            grade=int(input('grade (1-10):'))
            school_class[name]+=(grade, )
            print('Оценка успешно добавлена')
        else:
            print('студента еще не существует')
    elif oper==3:
        if len(school_class)<1:
            print('Оценок не содержится')
        elif len(school_class)>=1:
            for name in school_class.keys():
                grades=school_class[name]
                if len(grades)>=1:
                    print(name)
                    print(school_class[name])
                    print('avg:')
                    print(sum(grades)/len(grades))
                else:
                    print('У', name, 'нет оценок')
    oper=int(input(menu))

    

oper=int(input(menu))

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход3
while oper!=-1:
    if oper==1:
        name=input("name:")
        if name not in school_class:
            school_class[name]=()
            print('Студент успешно создан')
        else:
            print('Уже был создан')
    elif oper==2:
        name=input("name:")
        if name in school_class:
            grade=int(input('grade (1-10):'))
            school_class[name]+=(grade, )
            print('Оценка успешно добавлена')
        else:
            print('студента еще не существует')
    elif oper==3:
        if len(school_class)<1:
            print('Оценок не содержится')
        elif len(school_class)>=1:
            for name in school_class.keys():
                grades=school_class[name]
                if len(grades)>=1:
                    print(name)
                    print(school_class[name])
                    print('avg:')
                    print(sum(grades)/len(grades))
                else:
                    print('У', name, 'нет оценок')
    oper=int(input(menu))

    
vasia pupkin
(7, 5)
avg:
6.0
У dima нет оценок

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход3
vasia pupkin
(7, 5)
avg:
6.0
У dima нет оценок

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход2
name:dima
grade (1-10):10
Оценка успешно добавлена

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход2
name:dima
grade (1-10):10
Оценка успешно добавлена

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход3
vasia pupkin
(7, 5)
avg:
6.0
dima
(10, 10)
avg:
10.0

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход1
name:oleg
Студент успешно создан

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход2
name:oleg
grade (1-10):6
Оценка успешно добавлена

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход3
vasia pupkin
(7, 5)
avg:
6.0
dima
(10, 10)
avg:
10.0
oleg
(6,)
avg:
6.0

1 - добавить нового студента
2 - добавить оценку
3 - посчитать средний балл
-1 - выход-1
