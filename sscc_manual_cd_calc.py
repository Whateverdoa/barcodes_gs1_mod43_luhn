import pandas as pd
from checkdigit._data import cleanse, convert
from icecream import ic



def calc_sscc(string='12345678901234567'):
    pass
        # for num in string:
        #     int(num[0])*3 + int(num[1]) +
        #
def calculate(data: str) -> str:
    """Calculates the luhn check digit.

    Args:
        data: A block of data without the check digit

    Returns:
        str: A string representing the missing check digit

    """
    data = cleanse(data)
    position_counter = 1  # 1-based indexing
    total_sum = 0
    for item in data[::-1]:  # Reverses String
        digit = int(item)
        if position_counter % 2:  # If position number is odd with reversed string
            add_value = digit * 3
            total_sum += add_value
        else:

            total_sum += digit

        # ic(total_sum)
        position_counter += 1
    return convert(10 - (total_sum % 10), "luhn")


sscc = 35050406724000001
# ic(calculate(sscc))




def maak_simpele_lijst(begin_nummer,totaal, pdf='leeg.pdf'):
    '''list comp voor maken nummer lijst, 3 kolommen
    kijk voor benamingen in project lijst bewerken'''
    eind = begin_nummer + totaal
    nummers = [[f'{x:>{0}{17}}{calculate(str(x))}',f'{pdf}'," "] for x in range(begin_nummer,eind)]


    return nummers

print(maak_simpele_lijst(sscc,10))

df = pd.DataFrame(maak_simpele_lijst(sscc,300000), columns=["kolom1", "pdf", "omschrijving"], dtype="str")
ic(df.head(10))
df.to_csv('sscc_300_000.csv',sep=";", encoding="utf-8",index=0)