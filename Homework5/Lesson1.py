#1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

data = "Время сквозь пальцы песком утекает,\
        Буднями мчатся недели, года!\
        Привычный уклад зимний праздник меняет,\
        Когда вокруг ёлки, огни, суета!\
        Так пусть в эти дни волшебство приключится,\
        Магия праздничных, радостных дней!\
        И сказка к вам в дверь в тот же миг постучится,\
        Желания ваши исполнив скорей!"

list_data = filter(lambda x: x.find('а') == -1 and x.find('б') == -1 and x.find('в') == -1, data.split())
output = " ".join(list_data)

print(output)