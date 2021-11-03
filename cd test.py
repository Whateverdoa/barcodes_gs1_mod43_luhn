from checkdigit import luhn
import checkdigit as cd
from baluhn import generate, verify
import biip
from biip.gs1 import GS1Message
from biip.gs1.checksums import numeric_check_digit

from icecream import ic

validate = '123456789012'

ic(cd.luhn.calculate(validate))

sscc_ = '350504067240000013'
# sscc ='0406724000002'

ic(generate(sscc_))
# ic(generate(validate))

result = biip.parse("96385074")
ic(result.gtin)

sscctest = biip.parse(sscc_)
ic(sscctest)

valuesscc ="00350504067240000013"

msg = GS1Message.parse(valuesscc)
ic(msg.as_hri())

ic(numeric_check_digit('871234567890'))
# ean13
ic(numeric_check_digit('2123456'))
#ean 8



