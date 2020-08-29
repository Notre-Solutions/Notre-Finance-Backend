from math import ceil

def calcMortgageMonthlyPayments(housePrice, deposit, mortgageIntRate, loanTerms, type):
  loanAmount = housePrice - deposit
  monthlyMortgageIntRate = (mortgageIntRate/12)
  noOfPayments = loanTerms * 12

  if type == 'io':
    monthlyMortgageIntRate = (mortgageIntRate/12)
    monthlyPayment = loanAmount * (monthlyMortgageIntRate)
    monthlyPayment = ceil(monthlyPayment*100)/100
    return {"monthlyMortgagePayment": monthlyPayment, "totalPayable": monthlyPayment*(noOfPayments)}
  elif type == 'fi':
    z = (1+monthlyMortgageIntRate)**(noOfPayments)
    monthlyPayment = loanAmount*(monthlyMortgageIntRate*z)/(z - 1)
    monthlyPayment = ceil(monthlyPayment*100)/100
    return {"monthlyMortgagePayment": monthlyPayment, "totalPayable": monthlyPayment*(noOfPayments)}