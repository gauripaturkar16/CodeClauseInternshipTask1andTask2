import time

String="""this is a typing speed calculator and we are using python here.Copying this paragraph in below.Develop a Python program that prompts the user to type a given set of words or sentences.The program should record the time taken to type and calculate the typing speed in WPM. Provide feedback on accuracy and speed. """
wordcount=len(String.split())
print(String)

while True:

    t0=time.time()

    inputtext=str(input(' the Sentence:'))

    t1=time.time()

    accuracy=len(set(inputtext.split())&set(String.split()))

    accuracy=accuracy/wordcount

    timetaken =t1-t0

    wpm=wordcount/timetaken

    print("WPM :",wpm, "\n Accuracy :", accuracy, "\n Timetaken :",timetaken)