def confidence_interval(correction, auth, neg, cac):
    nega = float(neg)
    correc = float(correction)


    if auth:
        score_a = 10
    else:
        score_a = 0

    print(nega)
    if nega < 15:
        score_n = 15
    elif nega >=15 and nega < 30:
        score_n = 7.5
    elif nega >= 30:
        score_n = 0
        
    if correc == 0:
        score_c = 25
    elif correc == 1:
        score_c = 22
    elif correc == 2:
        score_c = 20
    elif correc == 3:
        score_c = 17
    elif correc == 4:
        score_c = 15
    elif correc == 5:
        score_c = 12
    elif correc == 6:
        score_c = 10
    elif correc == 7:
        score_c = 8
    elif correc == 8:
        score_c = 6
    elif correc == 9:
        score_c = 4
    else:
        score_c = 2

    if cac == True:
        score_cac = 0
    else:
        score_cac = 50
        
    confidence = round(score_a + score_n + score_c + score_cac)

    return confidence    
