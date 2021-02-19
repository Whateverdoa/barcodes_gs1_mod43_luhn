from checkdigit import luhn
import checkdigit as cd
from baluhn import generate, verify

from icecream import ic

validate = '123456789012'

ic(cd.luhn.calculate(validate))

sscc = '35050406724000001'
# sscc ='0406724000002'

ic(generate(sscc))
# ic(generate(validate))

