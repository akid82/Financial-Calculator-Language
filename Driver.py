from lark import Lark, Token
from Organization import *

myGrammar = """
start: expression+

?expression: mathematical_expression
        | function 

function: function_title "(" attribute+ ")"

function_title: "lump_sum_FV" -> lump_sum_fv
            | "lump_sum_PV" -> lump_sum_pv
            | "lump_sum_time" -> lump_sum_time
            | "lump_sum_rate" -> lump_sum_rate
            | "ordinary_annuity_PV" -> ordinary_annuity_pv
            | "ordinary_annuity_FV" -> ordinary_annuity_fv
            | "annuity_due_PV" -> annuity_due_pv
            | "annuity_due_FV" -> annuity_due_fv
	    	| "price_bond" -> price_bond
            
?attribute: "<" variable ">"

?variable: present_value
        | future_value
        | time
        | yield
        | periodic_payment
        | par_value 
        | coupon_rate

present_value: mathematical_expression "PV"

future_value: mathematical_expression "FV"

time: mathematical_expression time_measure

time_measure: "years" -> annually
            | "year" -> annually
            | "semiannual periods" -> semiannually
            | "quarters" -> quarterly
            | "months" -> monthly
            | "weeks" -> weekly
            | "days" -> daily

yield: mathematical_expression "% compounds" compounding_frequency

compounding_frequency: "annually" -> annually 
                    | "semiannually" -> semiannually
                    | "quarterly" -> quarterly
                    | "monthly" -> monthly
                    | "weekly" -> weekly
                    | "daily" -> daily

periodic_payment: mathematical_expression "payment"

par_value: mathematical_expression "par"

coupon_rate: mathematical_expression "% coupon" 

?mathematical_expression: high_precedence_term
    | mathematical_expression "+" high_precedence_term -> add
    | mathematical_expression "-" high_precedence_term -> sub

?high_precedence_term: base_exp
                    | high_precedence_term "*" base_exp -> mul
                    | high_precedence_term "/" base_exp -> div

?base_exp: NUMBER -> num
        | function
        | "(" mathematical_expression ")"

%import common.NUMBER
%import common.WS_INLINE
%ignore WS_INLINE

"""

def runTree(t):
	if isinstance(t, Token):
		return t.value
	elif t.data == 'start':
		for child in t.children:
			return runTree(child)
	elif t.data == 'function':
		# for each function we encounter, we need to extract all of the attributes tied to it
		attributes = [] 
		functionName = t.children[0].data
		for child in t.children[1:]: # first child will be the function name guarenteed
			attribute = runTree(child)
			attributes.append(attribute)
		if functionName == 'lump_sum_fv':
			value = lump_sum_FV(attributes)
		elif functionName == 'lump_sum_pv':
			value = lump_sum_PV(attributes)
		elif functionName == 'lump_sum_time':
			value = lump_sum_time(attributes)
		elif functionName == 'lump_sum_rate':
			value = lump_sum_rate(attributes)
		elif functionName == 'ordinary_annuity_pv':
			value = ordinary_annuity_PV(attributes)
		elif functionName == 'ordinary_annuity_fv':
			value = ordinary_annuity_FV(attributes)
		elif functionName == 'annuity_due_pv':
			value = annuity_due_PV(attributes)
		elif functionName == 'annuity_due_fv':
			value = annuity_due_FV(attributes)
		elif functionName == 'price_bond':
			value = price_bond(attributes)
		return value
	elif t.data == 'present_value' or t.data == 'future_value' or t.data == 'periodic_payment' or t.data == 'par_value' or t.data == 'coupon_rate':
		for child in t.children:
			return (runTree(t.data), runTree(child))
	elif t.data == 'time' or t.data == 'yield': # for both time and yield, there are additional non-terminals that need to be extracted
		numericalValue = float(runTree(t.children[0])) 	# first child = token of number
		timeMeasure = runTree(t.children[1]) 			# second child = t.data of the child
		return (runTree(t.data), numericalValue, timeMeasure)
	elif t.data == 'annually' or t.data == 'semiannually' or t.data == 'quarterly' or t.data == 'monthly' or t.data == 'weekly' or t.data == 'daily':
		return t.data
	elif t.data == 'add':
		return runTree(t.children[0]) + runTree(t.children[1])
	elif t.data == 'sub':
		return runTree(t.children[0]) - runTree(t.children[1])
	elif t.data == 'mul':
		return runTree(t.children[0]) * runTree(t.children[1])
	elif t.data == 'div':
		return runTree(t.children[0]) / runTree(t.children[1])
	elif t.data == 'num':
		return float(t.children[0])
	else:
		raise SyntaxError("unknown tree")
	
parser = Lark(myGrammar)

greeting = """
	Welcome! Please enter any combination of arithmetic operations or function calls that you would like to be computed
	Press enter after each line to perform the calculations entered on that line
	Type "quit" when ready to exit the program
"""
print(greeting)
programRunning = True
while programRunning:
	userInput = input(">>> ")
	if userInput == "quit":
		programRunning = False
	else:
		program = userInput
		parseTree = parser.parse(program)
		print(runTree(parseTree))

print("Exited successfully")