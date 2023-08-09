class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    # def __init__(self, someone, question):
    #     self.someone = someone
    #     self.question = question

    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        print(f'{someone.name}, {question}')
        # запросите ответ на вопрос у someone
        print(f'{someone.name}, {question}')

        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
        if question == 'мне грустненько, что делать?':
            print('Держись, все получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)


student1 = Student('Тимофей')
curator = Curator('Марина')

student1.ask_question(curator, 'мне грустненько, что делать?')

