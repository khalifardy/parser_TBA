class FiniteAutomata:
    def __init__(self,string):
        self.string = string
        self.char = list(self.string)
    
    def fa_if(self):
        q2 = True
        q3 = False
        q1 = {
            'f':q2
        }
        q0 = {
            'i':q1
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
            '=':q4,
            'posisi':'q2'
        }
        q3 = {
            '=':q4,
            'posisi':'q3'
        }
        q1 = {
            '=':q4,
            'posisi':'q1'
        }
        q0 = {
            '=':q1,
            '>':q2,
            '<':q3,
            'posisi':'q0'
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
        q2= {
            'd':q3,
        }
        q1 = {
            'n':q2
        }
        q0 = {
            'a':q1,
            '&':q3
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
            'r':q2
        }
        q0 = {
            'o':q1,
            '|':q2
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
            ':':q1,
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
        q1 = True
        q2 = False

        q0 = {
            '+':q1,
            '-':q1,
            '*':q1,
            '/':q1,
            '**':q1,
            '//':q1,
            "%":q1
        }

        

        q_current = q0

        for i in self.char:
            try:
                q_current = q_current[i]
            except Exception as _:
                q_current = q2
                break
        
        return q_current
    
    

