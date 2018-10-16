# program to check if trainee has achieved his/her weekly target or not
# 12 - October - 2018

class Trainee:
    name = "TrneeOne"
    designation = "Developer"
    tasksMadeThisWeek = 6

    def hasAchievedTarget(self):

        if self.tasksMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")
trainee = Trainee()
trainee.name
print(trainee.name)
trainee.hasAchievedTarget()
