#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,  QPushButton, QLabel
from random import shuffle
from random import randint, shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list= []
question_list.append(Question('Как называется столица Франции?', 'Париж', 'Москва', 'Йошкар-Ола', 'Сеул'))
question_list.append(Question('Что нельзя поместить в огромную сковородку?', 'Крышка от сковородки', 'Тарелку', 'Стакан', 'Нож'))
question_list.append(Question('В чем измеряется сила тока?', 'Ампер', 'Вольт', 'Джоуль', 'Ньютон'))
question_list.append(Question('Где находится самая маленькая кость в теле человека?', 'Ухо', 'Нос', 'Палец мизинца', 'Плечо'))
question_list.append(Question('Какая валюта Дании?', 'Крона', 'Рубли', 'Тенге', 'Доллар'))
question_list.append(Question('Зачем язык во рту?', 'За зубами', 'Чтобы есть', 'Чтобы чувствовать', 'Просто чтобы был'))
question_list.append(Question('Какое колесо автомобиля не вращается во время движения? ', 'Запасное', 'Передние', 'Задние', 'Машинное'))
question_list.append(Question('Сын моего отца, а мне не брат. Кто это?', 'Я', 'Брат', 'Дядя', 'Крёстный'))
question_list.append(Question('Какая река самая страшная?', 'Тигр', 'Амазонка', 'Волга', 'Кали'))
question_list.append(Question('Почему собака бегает?', 'По земле', 'Потому что хочет', 'Потому что так устроено', 'Благодаря ногам'))
question_list.append(Question('У кого есть шапка без головы и нога без сапога?', 'У гриба', 'У кота в сапогах', 'У тебя', 'У улитки'))
question_list.append(Question('Каких камней в море не встретишь?', 'Сухих', 'Мягких', 'Жемчужных', 'Окрашенных'))
question_list.append(Question('Из какой посуды нельзя ничего поесть?', 'Из пустой', 'Из посуды соседа', 'Из посуды Бездомного', 'Из посуды собаки'))



app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
okk = QPushButton('Ответить')
question = QLabel('Какой национальности не существует?')
Radioknop = QGroupBox('Варианты ответов')
knop_1 = QRadioButton('Энцы')
knop_2 = QRadioButton('Смурфы')
knop_3 = QRadioButton('Чульмцы')
knop_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(knop_1)
layout_ans3.addWidget(knop_2)
layout_ans3.addWidget(knop_3)
layout_ans3.addWidget(knop_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
Radioknop.setLayout(layout_ans1)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(question)
layout_line2.addWidget(Radioknop)
layout_line3.addWidget(okk)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)

AnsGROUPbOX = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(correct)
AnsGROUPbOX.setLayout(layout_res)
layout_line1.addWidget(question)
layout_line2.addWidget(Radioknop)
layout_line2.addWidget(AnsGROUPbOX)
layout_line3.addWidget(okk, stretch=2)

def show_result():
    ''' показать панель ответов'''
    Radioknop.hide()
    AnsGROUPbOX.show()
    okk.setText('Следующий вопрос')
def show_question():
    '''показать панель вопросов'''
    Radioknop.show()
    AnsGROUPbOX.hide()
    okk.setText('Ответить')
    Radioknop2.setExclusive(False)
    knop_1.setChecked(False)
    knop_2.setChecked(False)
    knop_3.setChecked(False)
    knop_4.setChecked(False)
    Radioknop2.setExclusive(True)
    
'''def test():
    if 'Ответить' == okk.text():
        show_result()
    else:
        show_question()'''
answers = [knop_1, knop_2, knop_3, knop_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    correct.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильних ответов:',window.score)
        print('Рейьтнг:', (window.score/window.total, '\n-Правильных ответов:', window.score))

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked:
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')
def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
def click_OK():
    if okk.text() == 'Ответить':
        check_answer()
    else:
        next_question()  

window = QWidget()  
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')        
Radioknop2 = QButtonGroup()
Radioknop2.addButton(knop_1)
Radioknop2.addButton(knop_2)
Radioknop2.addButton(knop_3)
Radioknop2.addButton(knop_4)
window.cur_question= -1
okk.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec()