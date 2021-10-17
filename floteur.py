

def computegrade(score):
    #
    score =  float(score)

    x = 'Error'
    if score <0 or score>1:
        x="error"

    elif score >= 0.9:
        x = 'A'
    elif score >=0.8:
        x='B'
    elif score >=0.7:
        x='C'
    elif score >= 0.6:
        x='D'
    
    elif score < .6:
        x ='F'
    
    else:
        x ="Hors de portée"
    return x


ret=computegrade(0)
print(ret)



