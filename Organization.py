from Adjustments import *
from Calculations import *
from math import log

def lump_sum_FV(attributes): 			# takes in attributes from parse tree
	neededAttributes = ['present_value', 'yield', 'time']
	errorMessage = "Calculating the future value of a lump sum requires three arguments: present value, interest rate, and time to maturity"
	# send unorderedAttributes to ordering function
	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)
	
	adjustedTimeAndYield = adjustTimeAndYield(orderedAttributes[1], orderedAttributes[2])

	# extract calculation values from attributes
	presentValue = orderedAttributes[0][1]
	periodicRate = adjustedTimeAndYield[0]
	numPeriods = adjustedTimeAndYield[1]
	
	# perform calculation
	futureValue = calc_lump_sum_FV(presentValue, periodicRate, numPeriods)
	return futureValue


def lump_sum_PV(attributes):
	neededAttributes = ['future_value', 'yield', 'time']
	errorMessage = "Calculating the present value of a lump sum requires three arguments: future value, interest rate, and time to maturity"

	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)
	
	adjustedTimeAndYield = adjustTimeAndYield(orderedAttributes[1], orderedAttributes[2])

	# extract calculation values from attributes
	futureValue = orderedAttributes[0][1]
	periodicRate = adjustedTimeAndYield[0]
	numPeriods = adjustedTimeAndYield[1]

	presentValue = calc_lump_sum_PV(futureValue, periodicRate, numPeriods)

	return presentValue


def lump_sum_time(attributes):
	neededAttributes = ['present_value', 'future_value','yield']
	errorMessage = "Calculating the time of a lump sum requires three arguments: future value, present value, and interest rate"
	
	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)

	# extract calculation values from attributes
	presentValue = orderedAttributes[0][1]
	futureValue = orderedAttributes[1][1]
	periodicRate = adjustYield(orderedAttributes[2])

	periodicTime = calc_lump_sum_time(presentValue, futureValue, periodicRate)

	return periodicTime

def lump_sum_rate(attributes):
	neededAttributes = ['present_value', 'future_value','time']
	errorMessage = "Calculating the required rate for a lump sum requires three arguments: future value, present value, and time to maturity"
	
	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)

	presentValue = orderedAttributes[0][1]
	futureValue = orderedAttributes[1][1]
	numPeriods = orderedAttributes[2][1]

	periodicRate = calc_lump_sum_rate(presentValue, futureValue, numPeriods)
	stringResult = str(periodicRate) + '%'
	return stringResult

def ordinary_annuity_PV(attributes):
	neededAttributes = ['time', 'periodic_payment', 'yield']
	errorMessage = "Calculating the present value of an ordinary annuity requires three arguments: time, periodic payment, and yield"

	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)

	adjustedTimeAndYield = adjustTimeAndYield(orderedAttributes[2], orderedAttributes[0])

	numPeriods = adjustedTimeAndYield[1]
	payment = orderedAttributes[1][1]
	periodicRate = adjustedTimeAndYield[0]

	presentValue = calc_ordinary_annuity_PV(numPeriods, payment, periodicRate)
	return presentValue

def ordinary_annuity_FV(attributes):
	neededAttributes = ['time', 'periodic_payment', 'yield']
	errorMessage = "Calculating the future value of an ordinary annuity requires three arguments: time, periodic payment, and yield"
	
	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)

	adjustedTimeAndYield = adjustTimeAndYield(orderedAttributes[2], orderedAttributes[0])

	numPeriods = adjustedTimeAndYield[1]
	payment = orderedAttributes[1][1]
	periodicRate = adjustedTimeAndYield[0]

	futureValue = calc_ordinary_annuity_FV(numPeriods, payment, periodicRate)
	return futureValue

def annuity_due_PV(attributes):
	neededAttributes = ['time', 'periodic_payment', 'yield']
	errorMessage = "Calculating the present value of an annuity due requires three arguments: time, periodic payment, and yield"

	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)

	adjustedTimeAndYield = adjustTimeAndYield(orderedAttributes[2], orderedAttributes[0])

	numPeriods = adjustedTimeAndYield[1]
	payment = orderedAttributes[1][1]
	periodicRate = adjustedTimeAndYield[0]

	presentValue = calc_annuity_due_PV(numPeriods, payment, periodicRate)
	return presentValue

def annuity_due_FV(attributes):
	neededAttributes = ['time', 'periodic_payment', 'yield']
	errorMessage = "Calculating the future value of an annuity due requires three arguments: time, periodic payment, and yield"

	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)

	adjustedTimeAndYield = adjustTimeAndYield(orderedAttributes[2], orderedAttributes[0])

	numPeriods = adjustedTimeAndYield[1]
	payment = orderedAttributes[1][1]
	periodicRate = adjustedTimeAndYield[0]

	futureValue = calc_annuity_due_FV(numPeriods, payment, periodicRate)
	return futureValue

def price_bond(attributes):
	neededAttributes = ['par_value', 'time', 'coupon_rate', 'yield']
	errorMessage = "Calculating the price of a bond requires 4 arguments: par value, coupon rate, time to maturity, and yield to maturity"

	orderedAttributes = orderAttributes(attributes, neededAttributes, errorMessage)

	bareCouponRate = orderedAttributes[2][1]
	periodicCouponRate = bareCouponRate / getYieldScalar(orderedAttributes[3][2]) / 100

	adjustedTimeAndYield = adjustTimeAndYield(orderedAttributes[3], orderedAttributes[1])

	numPeriods = adjustedTimeAndYield[1]
	parValue = orderedAttributes[0][1]
	periodicRate = adjustedTimeAndYield[0]
	coupon = parValue*periodicCouponRate

	presentValueCoupons = calc_ordinary_annuity_PV(numPeriods, coupon, periodicRate)
	presentValuePar = calc_lump_sum_PV(parValue, periodicRate, numPeriods)

	bondPrice = presentValueCoupons + presentValuePar
	return bondPrice