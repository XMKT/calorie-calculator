class Trans:

    def UserInput(words):
        # example: 100 ккал на 50 г в 1000 г
        text = words.split(' ')
        return text

    def Trans(number, unit):

        TransList = {
            'мг': 0.001,
            'г': 1,
            'кг': 1000,
            'кал': 0.001,
            'ккал': 1, }

        trans = TransList.get(unit)
        NewNumber = number * trans
        return NewNumber

def main(word):

    text = Trans.UserInput(word)
    # calories
    Cal = float(text[0])
    CalUnit = text[1]
    # weight
    Weight = float(text[3])
    WeightUnit = text[4]
    # transfer in weight
    TfWeight = float(text[6])
    TfWeightUnit = text[7]

    cal = Trans.Trans(Cal, CalUnit)
    weight = Trans.Trans(Weight, WeightUnit)
    tfweight = Trans.Trans(TfWeight, TfWeightUnit)
    result = cal * float(tfweight / weight)
    print(result)

if __name__=='__main__':
	print('эта программа предназначена для подсчёта калорий в продукте')
	Quest = str(input('ввод: '))
	if Quest == 'help':
		print('example: 100 ккал на 50 г в 1000 г')
	else:
		main(Quest)