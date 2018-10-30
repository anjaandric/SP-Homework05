""""
Write a Python program that inputs a document and then outputs a bar- chart plot
 of the frequencies of each alphabet character that appears in that document.
"""

import matplotlib.pyplot as plt


x = input("Your document: ")


d = {}
length = len(x)


for i in range(length):

    if x[i] not in d and x[i].isalpha():

        y = 0

        for j in range(i, length):

            if x[i] == x[j]:
                y += 1

        d[x[i]] = y


plt.bar(range(len(d)), list(d.values()), align='center')
plt.xticks(range(len(d)), list(d.keys()))

plt.show()