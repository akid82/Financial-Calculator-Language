# Financial-Calculator-Language

## Description:
The language defined by my Lark grammar is for a financial calculation programming language I defined myself.
This language was inspired by the way TVM calculations are inputted on the BA2 Plus Professional Financial Calculator.
The language has function names for time value of money calculations, present and future values of annuities, and bond pricing.
This langauge also has support for basic arithmetic between scalars and functions, multiple functions, and scalars within attributes.
Each function has a given number of attributes enclosed in "()".
Each attribute has a variable name, such as present value or coupon rate, tied to a numerical value and enclosed by "<>".
When the program is started, ">>>" are printed and the user is prompted to enter an expression of functions and arithmetic operations on a single line.
When a user presses 'Enter', the calculation described by their input is printed to the terminal and the user in prompted to enter another line.
Users can continue to perform calculations and can quit the program by typing "quit".

## Important Notes:
- My grammar supports ordering the attributes of a function in any order
- All rates (coupon and yield) are stated in whole number annual terms in accordance with how many financial markets quote interest rates

## To run the program: 
1. Navigate to the directory that stores all the program files
2. Enter the command: python3 Driver.py
3. Key in a line of expressions and type 'Enter'
4. Type "quit" to exit the program

# Sample Programs for Each Supported Calculation:
## Arithmetic
  \>>> 5+4\*12
  
  program result: 53.0
  
  \>>> (5 + 4)\*12
	
  program result: 108.0
  
  \>>> (1-2)/4\*12
	
  program result: 3.0
  
  \>>> 1-2/4\*12
	
  program result: -5.0

## Basic TVM
- Future Value of a Lump Sum:

	\>>> lump_sum_FV(<35000 PV> <4% compounds annually> <52\*40 weeks>) 
    
   BA2 Plus Pro: 168,035.722
    
   program result: 168035.721977783
    
- Present Value of a Lump Sum:
	\>>> lump_sum_PV(<1 year> <7% compounds annually> <10000 FV>)
    
   BA2 Plus Pro: 9,345.794393
    
   program result: 9345.794392523363
    
- Time:

  \>>> lump_sum_time(<10% compounds annually> <7000 + 4000\*2 PV> <20000 FV>)
	
  BA2 Plus Pro: 3.018377
	
  program result: 3.0183771874358225
  
- Discount Rate:
	
  \>>> lump_sum_rate(<1200 FV> <1000 PV> <5 years>)
	
  BA2 Plus Pro: 3.713729
	
  program result: 3.713728933664817%

## Annuities
- Ordinary Annuity

	\>>> ordinary_annuity_PV(<1000 payment> <4 years> <4% compounds annually>)
  
	BA2 Plus Pro: 3,629.895224
    
	program result: 3629.895224256857
	
  \>>> ordinary_annuity_FV(<10000 payment> <3 years > <8% compounds annually>)
  
	BA2 Plus Pro: 32464.00
    
	program result: 32464.000000000022
  
- Annuity Due

	\>>> annuity_due_PV(<10 years> <1000 payment> <3% compounds annually>)
  
	BA2 Plus Pro: 8,786.108922
    
	program result: 8786.10892187911
  
	\>>> annuity_due_FV(<10000 payment> <3 years > <8% compounds annually>)
  
	BA2 Plus Pro: 35,061.12
    
	program result: 35061.120000000024

## Bonds Pricing

  \>>> price_bond(<1000 par> <6% coupon> <3% compounds semiannually> <5 years>)
	
  BA2 Plus Pro: 1,138.3327
  
  program result: 1138.3327682778158

## Additional Problems
\>>> lump_sum_PV(<20 years> <15000 FV> <7% compounds annually>) + 3 * lump_sum_FV(<10\*1000 PV> <18\*12 months> <6% compounds annually>)

program result: 89506.4596295927

\>>> price_bond(<1000 par> <9% compounds semiannually> <6% coupon> <5\*52 weeks>)

program result: 881.3092273433476

\>>> 2 + ordinary_annuity_FV(<0.75\*12% compounds monthly> <100 payment> <15\*365 days>) / price_bond(<7% coupon><7% compounds semiannually><1000 par><12\*4 quarters>)

program result: 39.84057689971924

\>>> ( 2 + ordinary_annuity_FV(<0.75\*12% compounds monthly> <100 payment> <15\*365 days>) ) / price_bond(<7% coupon><7% compounds semiannually><1000 par><12\*4 quarters>)

program result: 37.84257689971923

## Future Extensions
1. The current functionality of this program rests on the assumption that all rates inputted by the user are in annual terms. Stating all interest rates in annual terms is a precedence set by most financial markets. However, users may not always have their rates in annual terms so one future extensions of this project could be to separate the yield attribute into two different attributes.
	 - One attribute would be a yield attribute containing the rate with the correct time measure (annual, semiannual, etc.).
	 - The second attribute would be a compounding attributes that states the compounding frequency.
	    - This addition would require compounding to be added to each of the appropriate neededAttributes.
	    - This addition would also require a separate function to reconcile differences between the yield's time measure and compounding frequency.
2. Currently the program only supports a select number of calculations. Additions such as deferred annuities, bond duration, and conversions between EAR and APY are all possible additions in the future.
