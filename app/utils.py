from math import ceil

def calcMortgageMonthlyPayments(housePrice, deposit, mortgageIntRate, loanTerms, type):
  loanAmount = housePrice - deposit
  monthlyMortgageIntRate = (mortgageIntRate/12)
  noOfPayments = loanTerms * 12
  monthlyPayment = False
  if type == 'io':
    monthlyMortgageIntRate = (mortgageIntRate/12)
    monthlyPayment = loanAmount * (monthlyMortgageIntRate)
  elif type == 'fi':
    z = (1+monthlyMortgageIntRate)**(noOfPayments)
    monthlyPayment = loanAmount*(monthlyMortgageIntRate*z)/(z - 1)
  
  monthlyPayment = ceil(monthlyPayment*100)/100
  totalPayable = ceil((monthlyPayment*(noOfPayments))*100)/100
  
  return {"monthlyMortgagePayment": monthlyPayment, "totalPayable": totalPayable}