# %%
from library import LexicalAnalyzer, Parser, FiniteAutomata

stri = input()
spl = stri.split()
lexi = LexicalAnalyzer()
token = [lexi.analysis(string) for string in spl]
parser = Parser()
if parser.output(token):
    print("Sring "+stri, " Valid")
else:
    print("String " + stri + " Tidak Valid")

# %%
fin = FiniteAutomata("=")
# %%
