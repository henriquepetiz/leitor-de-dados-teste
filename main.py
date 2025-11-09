####leitor de dados pequenos


class LeitorSinalizacao:
    """Classe para ler e analisar dados de sinalização"""
    
    def __init__(self, arquivo):
        """Inicializa o leitor com o nome do arquivo"""
        self.arquivo = arquivo
        self.antiga = ''
        self.ausente = []
        self.interesse = []
    
    def ler_arquivo(self):
        """Lê o arquivo CSV e processa os dados"""
        with open(self.arquivo, 'r') as f:
            primeira = True
            for line in f:
                if primeira:
                    primeira = False
                    continue
                
                self._processar_linha(line)
    
    def _processar_linha(self, line):
        """Processa uma linha do CSV"""
        lista = line.strip().split(';')
        
        if len(lista) < 15:
            return
        
        if self.antiga == '' or self.antiga > lista[4]:
            self.antiga = lista[4]
        
        if lista[13].strip() == '' or lista[14].strip() == '':
            self.ausente.append(lista)
        else:
            self.interesse.append(lista)
    
    def obter_data_antiga(self):
        """Retorna a data mais antiga encontrada"""
        return self.antiga
    
    def obter_dados_sem_coordenadas(self):
        """Retorna lista de dados sem latitude ou longitude"""
        return self.ausente
    
    def obter_dados_com_coordenadas(self):
        """Retorna lista de dados com latitude e longitude"""
        return self.interesse
    
    def exibir_relatorio(self):
        """Exibe um relatório completo dos dados"""
        print(f"Data da primeira implementacao: {self.antiga}")
        print()
        print(f"Dados sem latitude ou longitude: {len(self.ausente)} registros")
        print()
        print(f"Dados com latitude ou longitude: {len(self.interesse)} registros")


if __name__ == "__main__":
    leitor = LeitorSinalizacao("sinalizacao.csv")
    leitor.ler_arquivo()
    leitor.exibir_relatorio()
