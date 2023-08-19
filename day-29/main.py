import math

def middle_figure(a, b):
    string = ''.join(a + b).replace(" ", "")        # Remove all spaces
    midpoint = math.floor(len(string) / 2)
    string = string.replace(string[0:midpoint], "").replace(string[-midpoint:], "")
    if string:
        return string
    else:
        return "No middle figure"

print("middle_figure function:", middle_figure("make love", "not wars"))
# print("middle_figure function:", middle_figure("brit", "tney"))
