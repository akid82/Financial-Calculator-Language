
periodScalars = {
	"annually": 1,
	"semiannually": 2,
	"quarterly": 4,
	"monthly": 12,
	"weekly": 52,
	"daily": 365
}

def adjustTimeAndYield(yieldTup, timeTup):
	# grabbing numerical values
	bareYield = yieldTup[1]
	bareTime = timeTup[1]

	# adjust whole number yield to decimal rate
	if bareYield >= 0:
		bareYield = bareYield / 100
	else:
		raise ValueError("rates must be positive")
	
	# adjusting yield to periodic rate based on compounding frequency
	compoundingFrequency = yieldTup[2]
	yieldScalar = periodScalars[compoundingFrequency]
	periodicYield = bareYield/yieldScalar

	# reconciling differences between time and yield
	timeMeasure = timeTup[2]
	timeScalar = periodScalars[timeMeasure]
	periodicTime = bareTime * (yieldScalar/timeScalar)

	return (periodicYield, periodicTime)

def adjustYield(yieldTup):
	bareYield = yieldTup[1]
	# adjust whole number yield to decimal rate
	if bareYield >= 0:
		bareYield = bareYield / 100
	else:
		raise ValueError("rates must be positive")
	# adjusting yield to periodic rate based on compounding frequency
	compoundingFrequency = yieldTup[2]
	yieldScalar = periodScalars[compoundingFrequency]
	periodicYield = bareYield/yieldScalar
	return periodicYield

def getYieldScalar(compoundingFrequency):
	yieldScalar = periodScalars[compoundingFrequency]
	return yieldScalar

def orderAttributes(attributesGiven, attributesNeeded, errorMessage):
	
	if len(attributesGiven) != len(attributesNeeded):
		raise Exception(errorMessage)
	else:
		orderedAttributes = [0] * len(attributesNeeded)
		for i in range(len(attributesNeeded)):
			matchFound = False
			for j in range(len(attributesGiven)):
				if attributesGiven[j][0] == attributesNeeded[i] and matchFound == False:  # if function name from parse tree in attributes needed for a particular function, order it in the proper spot
					orderedAttributes[i] = attributesGiven[j]
					matchFound = True
			
			if matchFound == False:
				raise Exception(errorMessage)
			
	return orderedAttributes
	