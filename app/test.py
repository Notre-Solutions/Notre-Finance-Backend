config={
	"housePrice": 100000,
	"deposit": 0,
	"mortgageIntRate": 0.06,
	"loanTerms": 10
}

housePrice = float(config['housePrice'])
deposit = float(config['deposit'])
mortgageIntRate = float(config['mortgageIntRate'])
loanTerms = float(config['loanTerms'])

monthlyMortgageIntRate = (mortgageIntRate/12)
z = (1 + monthlyMortgageIntRate)**(loanTerms*12)-1

monthlyPayment = z
# (housePrice * monthlyMortgageIntRate * z)/z
# (housePrice * monthlyMortgageIntRate * (1 + monthlyMortgageIntRate**12*(loanTerms)))/

print(monthlyPayment)