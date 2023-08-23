import matplotlib.pyplot as plt
import numpy as np
import copy
import os
import time

try:
    path = os.path.dirname(__file__)

    filePath = path+r"\data\emailAndBacklog.txt"

    file = open(filePath, "r")

    userData = file.readline().split()
    userData.pop(0)
    userData1 = copy.deepcopy(userData)
    userData1.pop(0)

    for x in range(len(userData)):
        userData[x] = int((userData[x]))

    if int(max(userData)) < 60:
        factor = 1
        title = "Seconds"
    elif int(max(userData)) < 3600:
        factor = 60
        title = ("Minutes")
    else:
        factor = 3600
        title = "Hours"
    for x in range(len(userData)):
        userData[x] = int((userData[x])/factor)

    company=['All Time','Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    xpos = np.arange(len(company))

    plt.bar(xpos, userData, label=title)

    plt.xticks(xpos,company)
    plt.ylabel(title+" Spent Programming")
    plt.xlabel("Days Of The Week")
    plt.title('Hours Spent Programming')
    plt.legend()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.show()
except:
    print("User hasn't been created yet!")
