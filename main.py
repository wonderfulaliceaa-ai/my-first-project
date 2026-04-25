import os

if os.path.exists('main.py'):
    print('існує')
else:
    print("не існує")

#os.mkdir('file.txt ')
os.makedirs("папка a/папка b/папка c", exist_ok=True)

with open('lesson.txt', 'w', encoding="UTF-8") as file: # w - перезаписує файлик
    file.write("урок про файлики")

with open('lesson.txt', 'a', encoding="UTF-8") as file: # a - дописує до файлика
    file.write("\n деякий тект")

with open('lesson.txt', 'r', encoding="UTF-8") as file: # r - читає файлик
    print(file.readline())
    print(file.readline())

if os.path.exists('file.txt'):
    os.remove('file.txt')

#os.rmdir('папка')
#os.removedirs("папка a/папка b/папка c")
print("НАША ПАПКА")
for i, dirs, files in os.walk("."):
    for dir in dirs:
        print(dir)
    for file in files:
        print("🐾", file)


from tkinter.filedialog import askopenfilename
file = askopenfilename()
print(file)
