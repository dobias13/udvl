#David Dobias
class Formula:
    def __init__(self,subformulas):
        self.subforms=subformulas

    def toString(self):
        pass

    def eval(self,i):
        pass

    def subf(self):
        return self.subforms


class Variable(Formula):
    def __init__(self,name):
        Formula.__init__(self,[])
        self.m_name=name

    def toString(self):
        return self.name()

    def eval(self,i):
        return i[self.name()]

    def name(self):
        return self.m_name


class Negation(Formula):
    def __init__(self,orig):
        Formula.__init__(self,[orig])

    def originalFormula(self):
        return self.subf()[0]

    def toString(self):
        return '-'+ self.originalFormula().toString()

    def eval(self,i):
        return not self.originalFormula().eval(i)

#'spojka'.join(['1','2','3','4'])
    #1spojka2spojka
    #[[[avb]],[cvd]]
    #arraz
class Implication(Formula):
    def __init__(self,left, right):
        Formula.__init__(self, [left, right])

    #budem potrebovat laveho a praveho potomka

    def left(self):
        return self.subf()[0]

    def right(self):
        return self.subf()[1]

    def toString(self):#a=> b
        return "(" + self.left().toString() + "=>" + self.right().toString() + ")"

    def eval(self,i):
        return (not self.left().eval(i)) or (self.right().eval(i))

class Disjunction(Formula):
    def __init__(self,orig):
        Formula.__init__(self,orig)
        
    def toString(self):
        pomocnePole=""
        for j in  self.subf():
            pomocnePole+=j.toString()
            pomocnePole += "|"
        # funguje iba pri jednoduchejsich vzrazoch
        #print('('+'&'.join(  self.subf().toString() )+')')
        return '('+pomocnePole[0:-1] + ')'

    def eval(self,i):
        for j in self.subf():
            if (j.eval(i)):
                return True
        return False

class Conjunction(Formula):
    def __init__(self,orig):
        Formula.__init__(self,orig)

    def toString(self):
        pomocnePole=""
        for j in  self.subf():
            pomocnePole+=j.toString()
            pomocnePole += "&"
        #print('('+'&'.join(  self.subf().toString() )+')')
        #return '('+'&'.join( pomocnePole )+')'
        return '('+pomocnePole[0:-1] + ')'

    def eval(self,i):
        for j in self.subf():
            if not(j.eval(i)):
                return False
        return True


class Equivalence(Formula):
    #podobne ako pri implikacii
    # teda .. ked sa na to pozeram tak skoro rovnako okrem eval
    def __init__(self, left, right):
        Formula.__init__(self, [left, right])

    def left(self):
        return self.subf()[0]

    def right(self):
        return self.subf()[1]
    
    def toString(self):
        return "(" + self.left().toString() + "<=>" + self.right().toString() + ")"
    
    def eval(self, i):
        return (self.left().eval(i) == self.right().eval(i))

