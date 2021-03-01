# You choose one animal from the list. The program will ask the questions about it,
# you can answer only "Yes" or "No". The program should guess and win.

animals = ['Cow', 'Mouse', 'Camel', 'Hawk', 'Cat', 'Dog', 'Piranha', 'Shark', 'Butterfly',
           'Bee', 'Mosquito', 'Fly', 'Snow Leopard', 'Chicken', 'Duck']

q = [
    'Is your animal longer than a Macbook Air? Pls google, if in doubt.\n(a) Yes\n(b) No\n\n',
    'Can your animal be domestic? Do people keep it on a farm/ in their homes?\n(a) Yes\n(b) No\n\n',
    'Do people keep it for its meat, milk or eggs?\n(a) Yes\n(b) No\n\n',
    'Do people keep it for its skin?\n(a) Yes\n(b) No\n\n',
    'Can it fly? Even a little?\n(a) Yes\n(b) No\n\n',
    'Does it like Pedigree or Chappi more than Whiskas and Kitekat?\n(a) Yes\n(b) No\n\n',
    'Does it swim in the water?\n(a) Yes\n(b) No\n\n',
    'Does it hunt alone?\n(a) Yes\n(b) No\n\n',
    'Can it fly like a king of the sky?\n(a) Yes\n(b) No\n\n',
    'Can it survive the ardent heat?\n(a) Yes\n(b) No\n\n',
    'Can it sting a person, even if it does it seldom?\n(a) Yes\n(b) No\n\n',
    'Does it collect honey?\n(a) Yes\n(b) No\n\n',
    'Do you want to kill it during the sleepless night?\n(a) Yes\n(b) No\n\n',
    'Can it fly above the lake?\n(a) Yes\n(b) No\n\n',
]

answers = {
    q[0]: {"Yes": q[1], "No": q[4]},
    q[1]: {"Yes": q[2], "No": q[6]},
    q[2]: {"Yes": q[3], "No": q[5]},
    q[3]: {"Yes": "Your animal is a cow", "No": q[13]},
    q[4]: {"Yes": q[10], "No": "Your animal is a mouse"},
    q[5]: {"Yes": "Your animal is a dog", "No": "Your animal is a cat"},
    q[6]: {"Yes": q[7], "No": q[8]},
    q[7]: {"Yes": "Your animal is a shark", "No": "Your animal is a piranha"},
    q[8]: {"Yes": "Your animal is a hawk", "No": q[9]},
    q[9]: {"Yes": "Your animal is a camel", "No": "Your animal is a snow leopard"},
    q[10]: {"Yes": q[11], "No": "Your animal is a butterfly"},
    q[11]: {"Yes": "Your animal is a bee", "No": q[12]},
    q[12]: {"Yes": "Your animal is a mosquito", "No": "Your animal is a fly"},
    q[13]: {"Yes": "Your animal is a duck", "No": "Your animal is a chicken"},
}

def run_test():
    item = q[0]
    print(item)
    answer = input("Enter Yes or No: ")
    seconddict = answers[item]
    if answer in seconddict.keys():
        item = seconddict[answer]
        print(item)
        answer = input("Enter Yes or No: ")
        seconddict = answers[item]
        if answer in seconddict.keys():
            item = seconddict[answer]
            if "animal" in item:
                return item
            else:
                print(item)
                answer = input("Enter Yes or No: ")
                seconddict = answers[item]

