from math import log

def calc_lump_sum_FV(presentValue, periodicRate, numPeriods):
	futureValue = presentValue * ((1+periodicRate)**numPeriods)
	return futureValue

def calc_lump_sum_PV(futureValue, periodicRate, numPeriods):
	presentValue = futureValue / ((1+periodicRate)**numPeriods)
	return presentValue

def calc_lump_sum_time(presentValue, futureValue, periodicRate):
	periodicTime = log(futureValue/presentValue) / log(1+periodicRate) 
	return periodicTime

def calc_lump_sum_rate(presentValue, futureValue, numPeriods):
	periodicRate = ((futureValue/presentValue)**(1/numPeriods) - 1) * 100
	return periodicRate

def calc_ordinary_annuity_PV(numPeriods, payment, periodicRate):
	presentValue = payment * ( (1 - (1/((1+periodicRate)**numPeriods))) / periodicRate)
	return presentValue

def calc_ordinary_annuity_FV(numPeriods, payment, periodicRate):
	futureValue = payment * ( ( ( (1 + periodicRate)**numPeriods) - 1) / periodicRate)
	return futureValue

def calc_annuity_due_PV(numPeriods, payment, periodicRate):
	presentValue = calc_ordinary_annuity_PV(numPeriods-1, payment, periodicRate) + payment
	return presentValue

def calc_annuity_due_FV(numPeriods, payment, periodicRate):
	futureValue = calc_ordinary_annuity_FV(numPeriods, payment, periodicRate) * (1 + periodicRate)
	return futureValue