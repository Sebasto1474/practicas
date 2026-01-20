card_numeration = "45525842124"
def verify_card_number(card_number):
    clean_number = card_number.replace("-","")
    clean_number = clean_number.replace(" ","")
    total = 0
    pos = 0
    for  i in clean_number[::-1]:
        if pos %2 == 1:
            double_number = int(i) * 2
            if double_number > 9:
                double_number -= 9
            total += double_number
        else:
            total += int(i)
        pos += 1
    if total %10 == 0:
        return "VALID!"
    else:
        return "INVALID!"