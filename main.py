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
    
    def exibir_dados_sem_coordenadas(self, limite=None):
        """Exibe os dados sem coordenadas"""
        print("=" * 80)
        print("DADOS SEM LATITUDE OU LONGITUDE")
        print("=" * 80)
        
        dados = self.ausente[:limite] if limite else self.ausente
        
        for i, registro in enumerate(dados, 1):
            print(f"\nRegistro {i}:")
            print(f"  Descrição: {registro[1]}")
            print(f"  Estado: {registro[2]}")
            print(f"  Estado: {registro[3]}")
            print(f"  Data Implantação: {registro[4]}")
            print(f"  Logradouro: {registro[5]}")
            print(f"  Numero Inicial: {registro[6]}")
            print(f"  Numero Final: {registro[7]}")
            print(f"  De Fronte: {registro[8]}")
            print(f"  Cruzamento: {registro[9]}")
            print(f"  Lado: {registro[10]}")
            print(f"  Fluxo: {registro[11]}")
            print(f"  Local de instalação: {registro[12]}")
            print(f"  Latitude: {registro[13]}")
            print(f"  Longitude: {registro[14]}")
        
        if limite and len(self.ausente) < limite:
            print(f"\n... e mais {len(self.ausente) - limite} registros")
        
        print("\n" + "=" * 80)
    
    def exibir_dados_com_coordenadas(self, limite=None):
        """Exibe os dados com coordenadas"""
        print("=" * 80)
        print("DADOS COM LATITUDE E LONGITUDE")
        print("=" * 80)
        
        dados = self.interesse[:limite] if limite else self.interesse
        
        for i, registro in enumerate(dados, 1):
            print(f"\nRegistro {i}:")
            print(f"  Descrição: {registro[1]}")
            print(f"  Estado: {registro[2]}")
            print(f"  Data Implantação: {registro[4]}")
            print(f"  Logradouro: {registro[5]}")
            print(f"  Latitude: {registro[13]}")
            print(f"  Longitude: {registro[14]}")
        
        if limite and len(self.interesse) > limite:
            print(f"\n... e mais {len(self.interesse) - limite} registros")
        
        print("\n" + "=" * 80)
    
    def exibir_todas_listas(self, limite=5):
        """Exibe ambas as listas com um limite de registros"""
        print("\n")
        self.exibir_dados_sem_coordenadas(limite)
        print("\n")
        self.exibir_dados_com_coordenadas(limite)


if __name__ == "__main__":
    leitor = LeitorSinalizacao("sinalizacao.csv")
    leitor.ler_arquivo()
    leitor.exibir_relatorio()
    
    print("\n" + "=" * 80)
    print("VISUALIZANDO OS DADOS DAS LISTAS")
    print("=" * 80)
    
    # Exibe os primeiros 3 registros de cada lista
    leitor.exibir_todas_listas(limite=3)
    
    # Para ver TODOS os dados sem limite, descomente as linhas abaixo:
    # leitor.exibir_dados_sem_coordenadas()
    # leitor.exibir_dados_com_coordenadas()