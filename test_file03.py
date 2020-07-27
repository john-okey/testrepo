import sys

print{" "}

for i in range(1,int((sys.argv[1]))):
    if i == 1:
        print("Deze nummer is de {}st keer ik 'jij ben geweldig' moet schrijven".format(i))
    elif i == 2:
        print("Deze nummer is de {}nd keer ik 'jij ben geweldig' moet schrijven".format(i))
    elif i == 3:
        print("Deze nummer is de {}rd keer ik 'jij ben geweldig' moet schrijven".format(i))
    else:
        print("Deze nummer is de {}th keer ik 'jij ben geweldig' moet schrijven".format(i))
