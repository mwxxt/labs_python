print("\nВас приветствует шар предсказаний!\n")
question = input("Введите Ваш вопрос: ")
import random
print("\nШар предсказаний выдал следующий ответ:\n")
print(question,"-",random.choice(['Безусловно!', 'Лучше этого не делать!', 'Довертесь своей интуиции!', 'Лучше воздержитесь от этого!', 'Это определённо необходимо!', 'Рекомендуется!','Нет!','Да!','Сделайте это!','Не делайте этого!']),"\n")