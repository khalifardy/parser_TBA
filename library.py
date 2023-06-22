class FiniteAutomata:
    def __init__(self, string):
        self.string = string
        self.char = list(self.string)

    def fa_if(self):
        q2 = True
        q3 = False
        q1 = {
            'f': q2
        }
        q0 = {
            'i': q1
        }

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q3
                break

        if q_current != q2 and q_current != q3:
            q_current = False

        return q_current

    def fa_perbandingan(self):
        q4 = True
        q5 = False
        q2 = {
            '=': q4,
            'posisi': 'q2'
        }
        q3 = {
            '=': q4,
            'posisi': 'q3'
        }
        q1 = {
            '=': q4,
            'posisi': 'q1'
        }
        q0 = {
            '=': q1,
            '>': q2,
            '<': q3,
            'posisi': 'q0'
        }

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q5
                break

        if q_current != q4 and q_current != q5:
            if (q_current == q2 or q_current == q3) and len(self.char) == 1 and q_current != q1:

                q_current = True
            else:
                q_current = False

        return q_current

    def fa_dan(self):

        q3 = True
        q4 = False
        q2 = {
            'd': q3,
        }
        q1 = {
            'n': q2
        }
        q0 = {
            'a': q1,
            '&': q3
        }

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q4
                break

        if q_current != q3 and q_current != q4:
            q_current = False

        return q_current

    def fa_atau(self):

        q2 = True
        q3 = False

        q1 = {
            'r': q2
        }
        q0 = {
            'o': q1,
            '|': q2
        }

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q3
                break

        if q_current != q2 and q_current != q3:
            q_current = False

        return q_current

    def fa_titikdua(self):
        q2 = False
        q1 = True
        q0 = {
            ':': q1,
        }

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q2
                break

        return q_current

    def fa_operator(self):
        q3 = True
        q1 = {
            '/': q3,
            '*': q3
        }
        q2 = False

        q0 = {
            '+': q3,
            '-': q3,
            '*': q1,
            '/': q1,
            "%": q3
        }

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q2
                break

        return q_current

    def fa_not(self):
        q3 = True
        q4 = False

        q2 = {
            't': q3,
        }

        q1 = {
            'o': q2
        }

        q0 = {
            'n': q1
        }

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q4

        return q_current

    def fa_variabel(self):

        q3 = True
        q2 = False
        q1 = {
            "=": q2,
        }
        q0 = {
            "1": q1,
            "2": q2
        }

        for i in range(len(self.char)):
            if i == 0 and self.char[i]:
                try:
                    float(self.char[i])
                    q_current = q0["2"]
                    break
                except Exception as _:
                    q_current = q0["1"]
                    try:
                        q_current = q_current[self.char[i]]
                    except Exception as _:
                        q_current = q3
            else:
                q_current = q0["1"]
                try:
                    q_current = q_current[self.char[i]]
                except Exception as _:
                    q_current = q3

        return q_current

    def fa_boolean(self):
        q9 = False
        q5 = True
        q4 = {
            'e': q5
        }
        q3 = {
            "u": q4
        }
        q1 = {
            "r": q3
        }

        q8 = {
            'e': q5
        }
        q7 = {
            's': q8
        }
        q6 = {
            'l': q7
        }
        q2 = {
            'a': q6
        }
        q0 = {
            "T": q1,
            "F": q2
        }

        q_current = q0
        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q9

        return q_current

    def fa_sama_dengan(self):
        q2 = False
        q1 = True
        q0 = {
            "=": q1
        }

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except:
                q_current = q2

        return q_current


class LexicalAnalyzer:

    def analysis(self, symbol):
        dfa = FiniteAutomata(symbol)

        if dfa.fa_if():
            return 1
        elif dfa.fa_dan():
            return 2
        elif dfa.fa_atau():
            return 3
        elif dfa.fa_perbandingan():
            return 4
        elif dfa.fa_titikdua():
            return 5
        elif dfa.fa_operator():
            return 7
        elif dfa.fa_not():
            return 8
        elif dfa.fa_boolean():
            return 9
        elif dfa.fa_sama_dengan():
            return 10
        elif dfa.fa_variabel():
            return 6


class Parser:
    def __init__(self):
        self.list_simbol = {
            1: "a",
            2: "b",
            3: "j",
            4: "c",
            5: "d",
            6: "e",
            7: "f",
            8: "g",
            9: "h",
            10: "i"
        }

    def __getitem__(self, key):
        return self.list_simbol[key]

    def output(self, list_analysis):
        lst = [self.__getitem__(i) for i in list_analysis]
        stack = []
        stack.append("#")
        stack.append("S")
        while stack[-1] != "#":

            if stack[-1] == "S":
                stack.pop()
                stack.append("D")
                stack.append("d")
                stack.append("A")
                stack.append("a")
                if stack[-1] != lst[0]:
                    return False
            elif stack[-1] == "A":
                stack.pop()
                if lst[0] == "e" and lst[1] == "c":
                    stack.append("e")
                    stack.append("c")
                    stack.append("e")
                elif lst[0] == "h":
                    stack.append("h")
                elif lst[0] == "g" and lst[1] == "h":
                    stack.append("h")
                    stack.append("g")
                elif lst[0] == "g" and lst[1] == "e" and lst[2] == "c":
                    stack.append("e")
                    stack.append("c")
                    stack.append("e")
                    stack.append("g")
                elif lst[0] == "e" and lst[1] == "j":
                    stack.append("e")
                    stack.append("j")
                    stack.append("e")
                elif lst[0] == "e" and lst[1] == "b":
                    stack.append("e")
                    stack.append("b")
                    stack.append("e")
                elif lst[0] == "g" and lst[1] == "e" and lst[2] == "b":
                    stack.append("e")
                    stack.append("b")
                    stack.append("e")
                    stack.append("g")
                elif lst[0] == "g" and lst[1] == "e" and lst[2] == "j":
                    stack.append("e")
                    stack.append("j")
                    stack.append("e")
                    stack.append("g")

                else:
                    return False

            elif stack[-1] == "D":
                stack.pop()
                stack.append("e")
                stack.append("f")
                stack.append("e")
                stack.append("i")
                stack.append("e")

            elif stack[-1] == "a":
                if lst[0] == "a":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False

            elif stack[-1] == "c":
                if lst[0] == "c":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False

            elif stack[-1] == "e":
                if lst[0] == "e":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False

            elif stack[-1] == "f":
                if lst[0] == "f":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False

            elif stack[-1] == "h":
                if lst[0] == "h":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False

            elif stack[-1] == "d":
                if lst[0] == "d":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False

            elif stack[-1] == "i":
                if lst[0] == "i":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False
            elif stack[-1] == "j":
                if lst[0] == "j":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False
            elif stack[-1] == "g":
                if lst[0] == "g":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False
            elif stack[-1] == "b":
                if lst[0] == "b":
                    stack.pop()
                    lst.pop(0)
                else:
                    return False

        return True
