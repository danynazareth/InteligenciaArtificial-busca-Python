class Pilha:
    def __init__(self,tamanho):
        self.cidades = []
        self.tamanho = 0
        
    def getPilha(self):
        return self.cidades
    
    def pilhaVazia(self):
        if(len(self.cidades)== 0):
            return True
        return False
        
    def desempilhar(self):
        if(self.pilhaVazia() == False):
            return self.cidades.pop()
        return None
    def pilhaCheia(self):
        if(len(self.cidades) < self.tamanho):
            return True
        return False
    
    def empilhar(self,cidade):
        if(self.pilhaCheia() == False):
            self.cidades.append(cidade)
    
    def getTopo(self):
        if(len(self.cidades)!=0):
            return self.cidades[len(self.cidades)-1]
        return None
    
    def myPilha(self):
        return self.cidades


class Fila:
    def __init__(self, tamanhoMax=0):
        self.cidades=[]
        self.tamanhoMaximo = tamanhoMax
    
    def getFila(self):
        return self.cidades
    
    def filaCheia(self):
        if(len(self.cidades)<= self.tamanhoMaximo):
            return False
        return True
    
    def filaVazia(self):
        if(len(self.cidades) == 0):
            return True
        return False
        
    def enfileirar(self,cidade):
        if(self.filaCheia() == False):
            self.cidades.append(cidade)
        
    def desenfileirar(self):
        if(self.filaVazia() == False):
            return self.cidades.pop(0)
        return None
    
    def retornaPrimeiro(self):
        if(self.filaVazia() == False):
            return self.cidades[0]
        return None
    
    def tamanhoFila(self):
        return len(self.cidades)
    

class Adjascente:
    
    def __init__(self, cidade, distancia = 0):
        self.cidade = cidade
        self.distancia = distancia       
        self.heuristica = self.cidade.getDistancia()+distancia
        
    def  setCidade(self,cidade):
        self.cidade = cidade
        
    def  getCidade(self):
        return self.cidade
    
    def  setDistancia(self,distancia):
        self.distancia = distancia
        
    def  getDistancia(self):
        return self.distancia

    def funcaoHeuristica(self):
        return self.heuristica
    
    def showDados():
        print(f'Cidade: {self.cidade.getNome()}    -    Distancia: {self.cidade.getDistancia()}')
        


class Cidade:
        
    def __init__(self, nome, distancia=0):
        self.nome = nome
        self.visitado = False
        self.distancia = distancia
        self.adjascente = []
    
    def getDistancia(self):
        return self.distancia
    
    def setDistancia(self,distancia):
        self.distancia = distancia
            
    def addCidadeAdjascente(self, cidade):
        self.adjascente.append(cidade)
        
    def  setNome(self,nome):
        self.nome = nome
        
    def  getNome(self):
        return self.nome
        
    def  setVisitado(self,visitado):
        self.visitado = visitado
        
    def  getVisitado(self):
        return self.visitado
    
    def getAdjascentes(self):
        return self.adjascente

    def showDados(self):
        print(f'Cidade: {self.getNome()}    -    Distancia: {self.getDistancia()}')
        
class BuscaProfundidade:
    def __init__(self,cidadeInicial,cidadeFinal):
        self.fronteira = Pilha(20)
        
        self.inicio = cidadeInicial       
        self.inicio.setVisitado(True)
        
        self.objetivo = cidadeFinal
        
        self.fronteira.empilhar(self.inicio)
        
        self.chegouObjetivo = False

    
    def buscar(self):
        self.topo = self.fronteira.getTopo()
        
        print(f'Topo: {self.topo.getNome()}')

        if(self.topo == self.objetivo):
            self.chegouObjetivo = True
        else:
            for adj in self.topo.getAdjascentes():
                if(self.chegouObjetivo == False):
                    
                    print(f'Visitado: {adj.getCidade().getNome()}')
                    if(adj.getCidade().getVisitado()==False):
                        adj.getCidade().setVisitado(True)
                        self.fronteira.empilhar(adj.getCidade())
                        self.buscar()
                
        print(f'Desempilhou: {self.fronteira.desempilhar().getNome()}')

class Buscalargura:
    def __init__(self,cidadeInicial,cidadeFinal):
        self.fronteira = Fila(20)
        
        self.inicio = cidadeInicial       
        self.inicio.setVisitado(True)
        
        self.objetivo = cidadeFinal
        
        self.fronteira.enfileirar(self.inicio)
        
        self.chegouObjetivo = False

    
    def buscar(self):
        self.primeiro = self.fronteira.retornaPrimeiro()
        print(f'Primeiro: {self.primeiro.getNome()}')
        
        print(f'Desenfileirar {self.fronteira.desenfileirar().getNome()}')
        
        if(self.primeiro == self.objetivo):
            self.chegouObjetivo = True
        else:
            for adj in self.primeiro.getAdjascentes():
                if(adj.getCidade().getVisitado() == False):
                    adj.getCidade().setVisitado(True)
                    self.fronteira.enfileirar(adj.getCidade())
        
            if(self.fronteira.tamanhoFila()>0):
                self.buscar()

class Mapa:
    def __init__(self, peso=False):
        if(peso ==False):
            self.grafoSemPesos()
        else:
            self.grafoComPesos()
    
        self.defineMapa()
        
    def grafoComPesos(self):
        self.mapa = {'portoUniao': Cidade('Porto União',203),'pauloFrontin':Cidade('Paulo Frontin',172),'canoinhas':Cidade('Canoinhas',141),            'irati':Cidade('Irati',139),            'palmeira':Cidade('Palmeira',59),            'campoLargo':Cidade('Campo Largo',27),            'curitiba':Cidade('Curitiba',0),            'balsaNova':Cidade('Balsa Nova',41),            'araucaria':Cidade('Araucaria',23),            'saoJose':Cidade('São José',13),            'contenda':Cidade('Contenda',39),            'mafra':Cidade('Mafra',94),            'tijucaS':Cidade('Tijucas',56),            'lapa':Cidade('Lapa',74),            'saoMateus':Cidade('Sao Mateus',123),            'tresBarras':Cidade('Tres Barras',131) }

    def grafoSemPesos(self):
        self.mapa = {'portoUniao': Cidade('Porto União'),'pauloFrontin':Cidade('Paulo Frontin'),'canoinhas':Cidade('Canoinhas'),            'irati':Cidade('Irati'),            'palmeira':Cidade('Palmeira'),            'campoLargo':Cidade('Campo Largo'),            'curitiba':Cidade('Curitiba'),            'balsaNova':Cidade('Balsa Nova'),            'araucaria':Cidade('Araucaria'),            'saoJose':Cidade('São José'),            'contenda':Cidade('Contenda'),            'mafra':Cidade('Mafra'),            'tijucaS':Cidade('Tijucas'),            'lapa':Cidade('Lapa'),            'saoMateus':Cidade('Sao Mateus'),            'tresBarras':Cidade('Tres Barras') }
        
    def defineMapa(self):
        self.mapa['portoUniao'].addCidadeAdjascente(Adjascente(self.mapa['pauloFrontin'],46))
        self.mapa['portoUniao'].addCidadeAdjascente(Adjascente(self.mapa['canoinhas'],78))
        self.mapa['portoUniao'].addCidadeAdjascente(Adjascente(self.mapa['saoMateus'],87))

        self.mapa['saoMateus'].addCidadeAdjascente(Adjascente(self.mapa['palmeira'],77))
        self.mapa['saoMateus'].addCidadeAdjascente(Adjascente(self.mapa['irati'],57))
        self.mapa['saoMateus'].addCidadeAdjascente(Adjascente(self.mapa['lapa'],60))
        self.mapa['saoMateus'].addCidadeAdjascente(Adjascente(self.mapa['tresBarras'],43))
        self.mapa['saoMateus'].addCidadeAdjascente(Adjascente(self.mapa['portoUniao'],87))
        
        self.mapa['tresBarras'].addCidadeAdjascente(Adjascente(self.mapa['canoinhas'],12))
        self.mapa['tresBarras'].addCidadeAdjascente(Adjascente(self.mapa['saoMateus'],43))

        self.mapa['lapa'].addCidadeAdjascente(Adjascente(self.mapa['contenda'],26))
        self.mapa['lapa'].addCidadeAdjascente(Adjascente(self.mapa['saoMateus'],60))
        self.mapa['lapa'].addCidadeAdjascente(Adjascente(self.mapa['mafra'],57))

        self.mapa['palmeira'].addCidadeAdjascente(Adjascente(self.mapa['irati'],75))
        self.mapa['palmeira'].addCidadeAdjascente(Adjascente(self.mapa['saoMateus'],77))
        self.mapa['palmeira'].addCidadeAdjascente(Adjascente(self.mapa['campoLargo'],55))
        
        self.mapa['campoLargo'].addCidadeAdjascente(Adjascente(self.mapa['palmeira'],55))
        self.mapa['campoLargo'].addCidadeAdjascente(Adjascente(self.mapa['balsaNova'],22))
        self.mapa['campoLargo'].addCidadeAdjascente(Adjascente(self.mapa['curitiba'],29))
        
        self.mapa['balsaNova'].addCidadeAdjascente(Adjascente(self.mapa['curitiba'],51))
        self.mapa['balsaNova'].addCidadeAdjascente(Adjascente(self.mapa['campoLargo'],22))
        self.mapa['balsaNova'].addCidadeAdjascente(Adjascente(self.mapa['contenda'],19))
        
        self.mapa['curitiba'].addCidadeAdjascente(Adjascente(self.mapa['campoLargo'],29))
        self.mapa['curitiba'].addCidadeAdjascente(Adjascente(self.mapa['balsaNova'],51))
        self.mapa['curitiba'].addCidadeAdjascente(Adjascente(self.mapa['araucaria'],37))
        self.mapa['curitiba'].addCidadeAdjascente(Adjascente(self.mapa['saoJose'],15))
        
        self.mapa['araucaria'].addCidadeAdjascente(Adjascente(self.mapa['curitiba'],37))
        self.mapa['araucaria'].addCidadeAdjascente(Adjascente(self.mapa['contenda'],18))
        
        self.mapa['contenda'].addCidadeAdjascente(Adjascente(self.mapa['balsaNova'],19))
        self.mapa['contenda'].addCidadeAdjascente(Adjascente(self.mapa['araucaria'],18))
        self.mapa['contenda'].addCidadeAdjascente(Adjascente(self.mapa['lapa'],26))
        
        self.mapa['saoJose'].addCidadeAdjascente(Adjascente(self.mapa['curitiba'],15))
        self.mapa['saoJose'].addCidadeAdjascente(Adjascente(self.mapa['tijucaS'],49))
        
        self.mapa['tijucaS'].addCidadeAdjascente(Adjascente(self.mapa['mafra'],99))
        self.mapa['tijucaS'].addCidadeAdjascente(Adjascente(self.mapa['saoJose'],49))
        
        self.mapa['mafra'].addCidadeAdjascente(Adjascente(self.mapa['canoinhas'],66))
        self.mapa['mafra'].addCidadeAdjascente(Adjascente(self.mapa['lapa'],57))
        self.mapa['mafra'].addCidadeAdjascente(Adjascente(self.mapa['tijucaS'],99))
        
        self.mapa['canoinhas'].addCidadeAdjascente(Adjascente(self.mapa['portoUniao'],78))
        self.mapa['canoinhas'].addCidadeAdjascente(Adjascente(self.mapa['tresBarras'],12))
        self.mapa['canoinhas'].addCidadeAdjascente(Adjascente(self.mapa['mafra'],66))
        
        self.mapa['pauloFrontin'].addCidadeAdjascente(Adjascente(self.mapa['portoUniao'],46))
        self.mapa['pauloFrontin'].addCidadeAdjascente(Adjascente(self.mapa['irati'],75))

        self.mapa['irati'].addCidadeAdjascente(Adjascente(self.mapa['pauloFrontin'],75))
        self.mapa['irati'].addCidadeAdjascente(Adjascente(self.mapa['palmeira'],75))
        self.mapa['irati'].addCidadeAdjascente(Adjascente(self.mapa['saoMateus'],57))

    def getMapa(self):
        return self.mapa
    
    def toString(self):
        print('Porto Uniao')
        print([i.getCidade().getNome() for i in self.mapa['portoUniao'].getAdjascentes()])
        
        print('canoinhas')
        print([i.getCidade().getNome() for i in self.mapa['canoinhas'].getAdjascentes()])
        
        print('irati')
        print([i.getCidade().getNome() for i in self.mapa['irati'].getAdjascentes()])
       
        print('campo largo')
        print([i.getCidade().getNome() for i in self.mapa['campoLargo'].getAdjascentes()])
       
        print('Curitiba')        
        print([i.getCidade().getNome() for i in self.mapa['curitiba'].getAdjascentes()])
       
        print('Balsa Nova')        
        print([i.getCidade().getNome() for i in self.mapa['balsaNova'].getAdjascentes()])
       
        print('Araucaria')        
        print([i.getCidade().getNome() for i in self.mapa['araucaria'].getAdjascentes()])
       
        print('Sao Jose')        
        print([i.getCidade().getNome() for i in self.mapa['saoJose'].getAdjascentes()])
        
        print('contenda')        
        print([i.getCidade().getNome() for i in self.mapa['contenda'].getAdjascentes()])
        
        print('mafra')        
        print([i.getCidade().getNome() for i in self.mapa['mafra'].getAdjascentes()])
       
        print('tijuca do Sul')
        print([i.getCidade().getNome() for i in self.mapa['tijucaS'].getAdjascentes()])
       
        print('lapa')        
        print([i.getCidade().getNome() for i in self.mapa['lapa'].getAdjascentes()])
       
        print('Sao Mateus')        
        print([i.getCidade().getNome() for i in self.mapa['saoMateus'].getAdjascentes()])
       
        print('tres Barras')
        print([i.getCidade().getNome() for i in self.mapa['tresBarras'].getAdjascentes()])

    '''
        
        'portoUniao': Cidade('Porto União'),
        'pauloFrontin':Cidade('Paulo Frontin'),
        'canoinhas':Cidade('Canoinhas'),            
        'irati':Cidade('Irati'), 
        
        'palmeira':Cidade('Palmeira'),            
        'campoLargo':Cidade('Campo Largo'),            
        'Curitiba':Cidade('Curitiba'),            
        'balsaNova':Cidade('Balsa Nova'),  
                  
        'araucaria':Cidade('Araucaria'),            
        'saoJose':Cidade('São José'),            
        'contenda':Cidade('Contenda'),            
        'mafra':Cidade('Mafra'),  
                 
        'tijucaS':Cidade('TijucaS'),            
        'lapa':Cidade('Lapa'),            
        'saoMateus':Cidade('Sao Mateus'),           
        'tresBarras':Cidade('Tres Barras') 
    '''

class ConjuntoCidades:
    def __init__(self,cidades =[]):
        self.cidades = cidades
    
    def inserirCidade(self,myCidade):
        pos = 0
        while(pos<len(self.cidades)):
            if(self.cidades[pos].getDistancia() > myCidade.getDistancia()):
                break
            pos +=1
        self.cidades.insert(pos, myCidade)
    
    def inserirAdjascenteAStar(self,myAdjascentes):
        pos = 0
        while(pos<len(self.cidades)):
            if(self.cidades[pos].funcaoHeuristica() > myAdjascentes.funcaoHeuristica()):
                break
            pos +=1
        self.cidades.insert(pos, myAdjascentes)
    
    def getFirst(self):
        return self.cidades[0]
    
    def showCidades(self):
        for local in self.cidades:
            local.showDados()         


class BuscaGulosa:
    def __init__(self,objetivo):
        self.objetivo = objetivo
        self.chegou = False
    
    def buscar(self,cidadeAtual):
        cidadeAtual.setVisitado(True)
        print(cidadeAtual.showDados())
        if(cidadeAtual == self.objetivo):
            self.chegou = True
        else:
            self.fronteiras = ConjuntoCidades()
            for adj in cidadeAtual.getAdjascentes():
                if(adj.getCidade().getVisitado() == False):
                    adj.getCidade().setVisitado(True)
                    self.fronteiras.inserirCidade(adj.getCidade())
            self.fronteiras.showCidades()
            if(self.fronteiras.getFirst()): 
                self.buscar(self.fronteiras.getFirst()) 


class AStar:
    def __init__(self,objetivo):
        self.objetivo = objetivo
        self.chegou = False
    
    def buscar(self,cidadeAtual):
        cidadeAtual.setVisitado(True)
        print(cidadeAtual.showDados())
        
        if(cidadeAtual == self.objetivo):
            self.chegou = True
        else:
            self.fronteiras = ConjuntoCidades()
            for adj in cidadeAtual.getAdjascentes():
                if(adj.getCidade().getVisitado() == False):
                     adj.getCidade().setVisitado(True)
                     self.fronteiras.inserirAdjascenteAStar(adj)
            self.buscar(self.fronteiras.getFirst().getCidade()) 

        
        
m = Mapa(True).getMapa()

sets = ConjuntoCidades()


search = AStar(m['curitiba'])

search.buscar(m['portoUniao'])

'''
for city in m:
    sets.inserirCidade(m[city])
    

sets.showCidades()
'''