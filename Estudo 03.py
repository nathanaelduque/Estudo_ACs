import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import math 
from autolabel import rotulo

                    
class data():
        
    def get_data(self,dados):
        
        aparelho=0
        for ind in dados.index:
            for btu in self.BTU:
                if dados["BTU's"][ind]==btu and len(dados["Trifasico"][ind])==self.fases:
                    aparelho+=1
                    self.BTU[btu].update({"Aparelho %s" % (aparelho):{"setor":dados["SETOR"][ind]}})
                    self.BTU[btu]["Aparelho %s" % (aparelho)]["marca"]=dados["EQUIPAMENTO"][ind]
                    self.BTU[btu]["Aparelho %s" % (aparelho)]["corrente"]=dados["Corrente Total[A]"][ind]
                    self.BTU[btu]["Aparelho %s" % (aparelho)]["tensão"]=dados["Tensão  Alimentador [V]"][ind]
                    self.BTU[btu]["Aparelho %s" % (aparelho)]["trif"]=dados["Trifasico"][ind]
                    self.BTU[btu]["Aparelho %s" % (aparelho)]["fc"]=dados["Fases"][ind]
                    
class plottar():
    #Vai ter que herdar btu 
    def plottar_mono(self,btu):
    
        if self.plote_corrente !=list() :
            fig, ax = plt.subplots()
            grafico=ax.bar(self.plote_setor,self.plote_corrente)
            plt.xticks(rotation=90)
            ax.set_title("Corrente AC's {} BTU's".format(btu))
            ax.set_ylabel("Corrente [A]")
            ax.set_ylim([0,max(self.plote_corrente)+5])
            rotulo.dados(grafico,ax)
            plt.show()
                            
            if (len(self.plote_tensao_maxima)==1):
    
                self.plote_tensao_maxima.append(1.05*220)
                self.plote_tensao_minima.append(0.95*220) 
                                    
                            
            fig, ax = plt.subplots()
            grafico=ax.scatter(self.plote_setor,self.plote_tensao)
            plt.xticks(rotation=90)
            ax.set_title("Tensão AC's {} BTU's".format(btu))
            ax.set_ylabel("Tensão [A]")
            ax.set_ylim([0,max(self.plote_tensao)+50])
            for i in range(0,len(self.plote_tensao)):
                plt.text(x=self.plote_setor[i],y=self.plote_tensao[i],s=self.plote_tensao[i])
            plt.plot(self.plote_tensao_maxima,color="red")
            plt.plot(self.plote_tensao_minima,color="green")
            plt.show()
            
    def plottar_tri(self,btu,setor):
    
        if self.plote_corrente !=list() :
            fig, ax = plt.subplots()
            self.maximo=max(self.plote_corrente)
            self.minimo=min(self.plote_corrente)
            if (self.minimo/self.maximo)<0.91:   
                grafico=ax.bar(self.plote_fasec,self.plote_corrente,color='red')
            else:
                grafico=ax.bar(self.plote_fasec,self.plote_corrente,color='blue')
            plt.xticks(rotation=90)
            ax.set_title("Corrente AC's {} BTU's/ {}".format(btu,setor))
            ax.set_ylabel("Corrente [A]")
            ax.set_ylim([0,max(self.plote_corrente)+5])
            rotulo.dados(grafico,ax)
            plt.show()
                            
            if (len(self.plote_tensao_maxima)==1):
    
                self.plote_tensao_maxima.append(1.05*380)
                self.plote_tensao_minima.append(0.95*380) 
                                    
                            
            fig, ax = plt.subplots()
            grafico=ax.scatter(self.plote_faset,self.plote_tensao)
            plt.xticks(rotation=90)
            ax.set_title("Tensão AC's {} BTU's / {}".format(btu,setor))
            ax.set_ylabel("Tensão [A]")
            ax.set_ylim([0,max(self.plote_tensao)+50])
            for i in range(0,len(self.plote_tensao)):
                plt.text(x=self.plote_faset[i],y=self.plote_tensao[i],s=self.plote_tensao[i])
            plt.plot(self.plote_tensao_maxima,color="red")
            plt.plot(self.plote_tensao_minima,color="green")
            plt.show()       



            

# Parte do código referente a plotagem das correntes por setor             
class comparativos(plottar):
    
    def comparativo_mono(self,btu):            
        
        #for btu in self.BTU.keys():   
            
            a=0 # Variável auxiliar utilizada para plotar de 5 em 5,as corrente x setor 
            # Se for maior do que 6, divide de 5 em 5 
            if (len(self.BTU[btu])>6):
                for AC in self.BTU[btu].keys(): 
                    self.plote_corrente=list()
                    self.plote_setor=list()
                    self.plote_tensao=list()
                    self.plote_tensao_maxima=list()
                    self.plote_tensao_minima=list()
                    i=0 # Variável auxiliar utilizada para plotar de 5 em 5,as corrente x setor 
                    while(len(self.plote_corrente)<5 and a+i<=len(self.BTU[btu])-1): 
                        
                        self.plote_corrente.append(round(self.corrente[i+a],5))
                        self.plote_setor.append(self.setor[i+a])
                        self.plote_tensao.append(self.tensao[i+a])
  
                        #Limites de tensão dos AC's monofásicos                 
                        self.plote_tensao_maxima.append(1.05*220)
                        self.plote_tensao_minima.append(0.95*220)
                        i+=1
                    a+=5
                    self.plottar_mono(btu)
                        
                        
            else:
                self.plote_tensao_maxima=list()
                self.plote_tensao_minima=list()
                for AC in self.BTU[btu].keys():
                    self.plote_corrente=self.corrente
                    self.plote_setor=self.setor
                    self.plote_tensao=self.tensao
                    self.plote_tensao_maxima.append(1.05*220)
                    self.plote_tensao_minima.append(0.95*220)
                    
                self.plottar_mono(btu)
                
                
                
    def comparativo_tri(self,btu):            
        

            
            a=0 # Variável auxiliar utilizada para plotar de 5 em 5,as corrente x fase
            # Se for maior do que 6, divide de 5 em 5 
            for AC in self.BTU[btu].keys(): 
                    self.plote_corrente=list()
                    self.plote_fasec=list()
                    self.plote_faset=list()
                    self.plote_tensao=list()
                    self.plote_tensao_maxima=list()
                    self.plote_tensao_minima=list()
                    self.plote_setor=list()
                    i=0 # Variável auxiliar utilizada para plotar de 5 em 5,as corrente x setor 
                    while(len(self.plote_corrente)<3 and a+i<=len(self.BTU[btu])-1): 
                        
                        self.plote_corrente.append(round(self.corrente[i+a],2))
                        self.plote_fasec.append(self.fasec[i+a])
                        self.plote_faset.append(self.faset[i+a])
                        self.plote_tensao.append(self.tensao[i+a])
                        self.plote_setor.append(self.setor[i+a])
                        
  
                        #Limites de tensão dos AC's trifásicos                 
                        
                        i+=1
                        if i==1 and self.plote_setor != []:
                            self.salve_setor=self.plote_setor[0]
                    a+=3
                    for i in range(0,3):
                        if self.plote_tensao != list():
                            if min(self.plote_tensao)>300:
                                self.plote_tensao_maxima.append(1.05*380)
                                self.plote_tensao_minima.append(0.95*380)  
                            else:
                                self.plote_tensao_maxima.append(1.05*220)
                                self.plote_tensao_minima.append(0.95*220) 
                    self.plottar_tri(btu,self.salve_setor)

#Parte do código referente a plotagem dos histogramas de AC's monofásicos
class histogramas(comparativos):
    
    def histogramas_mono(self):
        # for estrutura in estruturado.keys()
        for btu in self.BTU.keys():
            self.corrente=list()
            self.setor=list()
            self.tensao=list()
            self.plote_setor=list()
            for AC in self.BTU[btu].keys():
               self.corrente.append(self.BTU[btu][AC]['corrente'])
               self.setor.append(self.BTU[btu][AC]['setor'])
               self.tensao.append(self.BTU[btu][AC]['tensão'])
            tamanho=len(self.corrente)         #Número de dados para cada tipo de AC (N° de BTU's)
            N_barras=int(math.sqrt(tamanho))+1 #N° de barras = Raiz do número de dados, aproximada 
                                               #para o maior inteiro mais próximo
            '''                                   
            fig, ax = plt.subplots()
            grafico=ax.hist(self.corrente,N_barras,rwidth=0.5)
            print(ax.hist.values())
            ax.set_title("Histograma Corrente AC's {} BTU's".format(btu))
            ax.set_xlabel("Corrente [A]")
            ax.set_ylabel("Frequência")
            plt.show()
            self.comparativo_mono(btu)
            '''
            (n, bins, patches) = plt.hist(self.corrente,N_barras,rwidth=0.5)
            plt.title("Histograma Corrente AC's {} BTU's".format(btu))
            plt.xlabel("Corrente [A]")
            plt.ylabel("Frequência")
            plt.show()
            self.comparativo_mono(btu)            
            
            
            
class tratamento(comparativos):
    
    def tratamento_tri(self):
        self.n_acs=self.n_acs/3
        self.carga_termica=self.carga_termica/3
        for btu in self.BTU.keys():
            self.setor=list()
            self.faset=list()
            self.fasec=list()
            self.corrente=list()
            self.tensao=list()
            for AC in self.BTU[btu].keys():
               self.faset.append(self.BTU[btu][AC]['trif'])
               self.fasec.append(self.BTU[btu][AC]['fc'])
               self.corrente.append(self.BTU[btu][AC]['corrente'])
               self.tensao.append(self.BTU[btu][AC]['tensão'])
               self.setor.append(self.BTU[btu][AC]['setor'])
            self.comparativo_tri(btu)
            
        '''
        for btu in self.BTU.keys():
            b=0 # Variável auxiliar utilizada para calcular a corrente média de cada AC trifásico
            for AC in self.BTU[btu].keys(): 
                self.corrente_media=0
                self.agrupar_corrente=list()
                j=0
                while(len(self.agrupar_corrente)<3 and b+j<len(self.BTU[btu])-1): 
                    self.agrupar_corrente.append(self.BTU[btu][AC]['corrente'])
                    j+=1
                self.corrente_media=sum(self.agrupar_corrente)/3
                b+=3
        self.histogramas_tri()
        '''    
        
class estudos(histogramas,tratamento):
    
    def estudo_mono(self):
        self.histogramas_mono()
        
    def estudo_tri(self):
        self.tratamento_tri()
    

class separe_monofasicos(data,estudos):
    
    def __init__(self,dados):
           
        self.fases=1
        # Criando as chaves vazias de cada para cada valor em BTU dos dados
        self.BTU=dict()
        
        #Usados em comparativo mono
        self.plote_corrente=list()
        self.plote_setor=list()
        self.plote_tensao=list()
        self.plote_tensao_maxima=list()
        self.plote_tensao_minima=list()     
                
        #Usados em histograma mono
        self.corrente=list()
        self.setor=list()
        self.tensao=list()
        
        #Número de AC's:
        self.n_acs=0
        #Carga Térmica Total:
        self.carga_termica=0
        
        #Separa em BTU's
        for ind in dados.index:  
            if(len(dados["Trifasico"][ind])==1):
                self.n_acs+=1
                self.carga_termica+=dados["BTU's"][ind]
                i=dados["BTU's"][ind]
                if i in self.BTU:
                    pass
                else:
                    self.BTU[i]=dict()
        self.get_data(dados)
        
class separe_trifasicos(data,estudos):
    
    def __init__(self,dados):
           
        self.fases=3
        # Criando as chaves vazias de cada para cada valor em BTU dos dados
        self.BTU=dict()
        
        #Usados em comparativo tri
        self.plote_corrente=list()
        self.plote_tensao=list()
        self.plote_tensao_maxima=list()
        self.plote_tensao_minima=list()     
                
        #Usados em histograma tri
        self.corrente=list()
        self.fase_corrente=list()
        self.fase_tensao=list()
        self.tensao=list()
        self.setor=list()
        self.corrente_media=list()
        
        #Número de AC's trifásicos
        self.n_acs=0
        #Carga Térmica Total:
        self.carga_termica=0
        #Separa em BTU's
        for ind in dados.index:  
            if(len(dados["Trifasico"][ind])>1):
                self.n_acs+=1
                self.carga_termica+=dados["BTU's"][ind]
                i=dados["BTU's"][ind]
                if i in self.BTU:
                    pass
                else:
                    self.BTU[i]=dict()
        self.get_data(dados)


# Aqui vai ficar o main do código
dados=pd.read_excel("Copia.xlsx")
mono=separe_monofasicos(dados)
mono.estudo_mono()
tri=separe_trifasicos(dados)
tri.estudo_tri()
carga_termica_tot=mono.carga_termica + tri.carga_termica



#Gerando gráficos que vão no inicio da apresentação
graficos_acs=list()
btus=list()
salve=list()
termica_individual=list()

#primeiramente os monofásicos
for btu in mono.BTU.keys():
    graficos_acs.append(len(mono.BTU[btu]))
    termica_individual.append(btu*len(mono.BTU[btu]))
    btus.append(str(btu))
    salve.append(str(btu))

#Depois os trifasicos
for btu in tri.BTU.keys():
    graficos_acs.append(len(tri.BTU[btu])/3)
    termica_individual.append(btu*len(tri.BTU[btu])/3)
    btus.append(str(btu))
    salve.append(str(btu))
    
#Tá organizando, mas tem como fazer isso de maneira melhor, fiz correndo 
i=0
lista_organizada_btus = list()
lista_organizada_graficos_acs=list()
tamanho=len(btus)



while (i!=tamanho):
    arg=np.argmax(graficos_acs)
    lista_organizada_graficos_acs.append(int(graficos_acs[arg]))
    lista_organizada_btus.append(btus[arg])
    graficos_acs.remove(graficos_acs[arg])
    btus.remove(btus[arg])
    i+=1



fig, ax = plt.subplots()

plt.xticks(rotation=90)
#Plotando Gráfico do Número de AC's:
grafico=ax.bar(lista_organizada_btus,lista_organizada_graficos_acs,width=0.5)
rotulo.dados(grafico,ax)

ax.set_title("Número de AC's por BTU's")
ax.set_ylabel("Número")
ax.set_xlabel("BTU's")
ax.set_ylim([0,max(lista_organizada_graficos_acs)*1.1])
plt.show()




#Plotando Gráfico da Carga Térmica

#Tá organizando, mas tem como fazer isso de maneira melhor, fiz correndo 
i=0
lo_btus = list()
lo_cargatermica=list()
tamanho=len(salve)

while (i!=tamanho):
    arg=np.argmax(termica_individual)
    lo_cargatermica.append(int(termica_individual[arg]/1000))
    lo_btus.append(salve[arg])
    termica_individual.remove(termica_individual[arg])
    salve.remove(salve[arg])
    i+=1



fig, ax = plt.subplots()

plt.xticks(rotation=90)

grafico=ax.bar(lo_btus,lo_cargatermica,width=0.5)
rotulo.dados(grafico,ax)

ax.set_title("Carga Térmica por kBTU's")

ax.set_ylabel("Carga Térmica")
ax.set_xlabel("BTU's")
ax.set_ylim([0,max(lo_cargatermica)*1.1])
plt.show()
