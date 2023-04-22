# Write your code here :-)
import pyinputplus as pyin
import random, time

#keep track of questions and answers

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        #right answers are handled by allowRegexes
        #wrong answers are handled by blockRegexes, with a custom message
        pyin.inputStr(prompt, allowRegexes = ['^%s$' % (num1 * num2)], blockRegexes = [('.*', "Incorrect")], timeout = 8, limit = 3)
    except pyin.TimeoutException:
        print('Out of time')
    except pyin.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    # pause to let user see result.
    time.sleep(1)
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

