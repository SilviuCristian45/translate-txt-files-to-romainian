from googletrans import Translator
import os


def translateFile(fileName) -> str:
    file = open(fileName)
    content = file.read()
    file.close()
    return translator.translate(content, dest='ro')


def writeToFile(filename: str, content: str) -> None:
    outputFile = filename[:filename.find('.txt')] + '-translated.txt'
    file = open(outputFile, 'w')
    file.write(content)
    file.close()


translator = Translator()

path = input("enter path: ")

while not os.path.exists(path):
    path = input("enter path: ")

files = os.listdir(path)

for file in files:
    if file.endswith('.txt') and 'translated' not in file:
        translation = translateFile(file)
        print(translation)
        writeToFile(file, translation.text)
