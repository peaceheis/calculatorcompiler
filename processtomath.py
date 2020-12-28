import math
_WRITTEN_NUMBERS = ("zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten","eleven", "twelve", "thirteen", "forteen", "fifteen", "sixteen", 
                    "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand", "million", "billion", "trillion")
_ABLE_TO_BE_MULTIPLIED = ("hundred", "thousand", "million", "billion", "trillion")
_ABLE_TO_BE_MULTIPLIERS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
                           "eleven", "twelve", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", 
                           "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" "hundred"
                           "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", 
                           "20", "30", "40", "50", "60", "70", "80", "90", "100")
_NUMBERS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "30", "40", "50", "60", "70", "80", "90", "100", "1000", "1000000", "1000000000", "1000000000000")
_WRITTEN_OPERATORS = ("plus", "minus", "times", "divided by", "sqrt(", "squared", "cubed", "to the power of", "*", "+", "-","/", "(", ")", "^")
_OPERATORS = ("+", "-", "*", "/", "math.sqrt(", "**2", "**3", "**", "*", "+", "-", "/", "(", ")", "**")

#this class is largely an assistance to Parser, which contains each individual word,
#and a type, either being a number, a multiplier, or an operator.
#numbers and multipliers are both "numbers", per se, but in a phrase
#one hundred thousand, there has to be a way to tell what's being said,
#and in reality, 'one' and 'hundred' are being multiplied to 'thousand'.
#'thousand' is the "number", and one and hundred are the multipliers.
class Symbol() : 
    def __init__(self, value, type_of_symbol) : 
        self.value = value
        self.type_of_symbol = type_of_symbol
    
    def __str__(self) : 
        return "value: " + str(self.value) + " type: " + self.type_of_symbol
    
    def __repr__(self) : 
        return str(self)

    def set_type(self, type_of_symbol) :
        self.type = type_of_symbol
        return self

#this is the class that takes human input, and translates it to python-readable code.
class Parser() : 
    def __init__(self, raw_input) : 
        unparsed_input = raw_input.replace(" ", "#")
        self.symbols = []
        current_value = ""
        #if there is a #, which is used to replace a space, 
        #that means a new "symbol" should be made and added to symbols.
        for char in unparsed_input : 
            if char == "#" : 
                type_of_symbol = self.determine_type(current_value)
                s = Symbol(current_value, type_of_symbol)
                self.symbols.append(s)
                current_value = ""
            else : 
                current_value += char
        type_of_symbol = self.determine_type(current_value)
        self.symbols.append(Symbol(current_value, type_of_symbol))

    def __str__(self) : 
        return str(self.symbols)
    
    def __repr__(self) : 
        return str(self)

    #these two are pretty self-explanatory, just look if the symbol is in the list of
    #numbers and operators.
    @staticmethod
    def decide_if_number(word) : 
        if word in _NUMBERS : 
            return 1
        if word in _WRITTEN_NUMBERS : 
            return 1
        else : 
            return 0
    @staticmethod
    def decide_if_operator(word) : 
        if word in _WRITTEN_OPERATORS : 
            return 1
        else : 
            return 0

    #after first assignment, "numbers" that serve as "multipliers", such as the hundred in 
    #hundred thousand, will be turned to "multipliers". 
    #after this, the list symbols should be ready for translation
    def assign_multipliers(self) : 
        for i in range(len(self.symbols)) : 
            current_symbol = self.symbols[i]
            if current_symbol.type_of_symbol == "number" and not i == len(self.symbols) - 1:
                if self.symbols[i + 1].type_of_symbol == "number" and self.symbols[i + 1].value in _ABLE_TO_BE_MULTIPLIED : 
                    if self.symbols[i].value in _ABLE_TO_BE_MULTIPLIERS : 
                        self.symbols[i] = Symbol(self.symbols[i].value, "multiplier")
        return self

    def determine_type(self, word) : 
        if self.decide_if_number(word) : 
            return "number" 
        elif self.decide_if_operator(word) :
            return "operator"
        else :
            return ""
    
    #this is where the good stuff happens! after multipliers have been assigned,
    #the symbols list will be turned into a string evaluatable by python, essentially
    #being compiled (hence the name calculatorcomplier)
    def translate(self) :
        python_evaluatable = "import math; "
        for symbol in self.symbols : 
            if symbol.type_of_symbol == "number" :              
                if symbol.value in _WRITTEN_NUMBERS :
                    x = _WRITTEN_NUMBERS.index(symbol.value)                    
                    python_evaluatable += str(_NUMBERS[x])
                else : 
                    python_evaluatable += str(x)
            
            if symbol.type_of_symbol == "multiplier" : 
                if symbol.value in _WRITTEN_NUMBERS :  
                    x = _WRITTEN_NUMBERS.index(symbol.value)
                    python_evaluatable += str(_NUMBERS[x]) + "*"
                else : 
                    python_evaluatable += str(symbol) + "*"

            if symbol.type_of_symbol == "operator" : 
                x = _WRITTEN_OPERATORS.index(symbol.value)
                python_evaluatable += _OPERATORS[x]                    
        return python_evaluatable
                 
                

