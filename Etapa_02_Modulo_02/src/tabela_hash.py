import re

class TabelaHash:
    
    def __init__(self, tamanho=97, funcao_hash='enlacamento'):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(self.tamanho)]
        self.funcao_hash_escolhida = funcao_hash

    def _hash_por_extracao(self, chave):
        numeros = re.findall(r'\d', str(chave))
        if not numeros: return 0
        valor_extraido = int("".join(numeros))
        return valor_extraido

    def _hash_por_enlacamento_deslocado(self, chave, tamanho_pedaco=2):
        chave_str = str(chave)
        hash_valor = 0
        for i in range(0, len(chave_str), tamanho_pedaco):
            pedaco = chave_str[i:i+tamanho_pedaco]
            soma_pedaco = 0
            for char in pedaco:
                soma_pedaco += ord(char)
            hash_valor += soma_pedaco
        return hash_valor
    
    def _funcao_hash(self, chave):
        if self.funcao_hash_escolhida == 'extracao':
            valor_bruto = self._hash_por_extracao(chave)
        else:
            valor_bruto = self._hash_por_enlacamento_deslocado(chave)
        
        return valor_bruto % self.tamanho

    def inserir(self, chave, valor):
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        for i, par in enumerate(bucket):
            if par[0] == chave:
                bucket[i] = (chave, valor)
                return
        bucket.append((chave, valor))

    def buscar(self, chave):
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        for par_chave, par_valor in bucket:
            if par_chave == chave:
                return par_valor
        return None
    
    def todas_as_chaves(self):
        chaves = []
        for bucket in self.tabela:
            for chave, _ in bucket:
                chaves.append(chave)
        return chaves
    
    def todos_os_valores(self):
        for bucket in self.tabela:
            for _, valor in bucket:
                yield valor
        
    def __str__(self):
        repr_str = ""
        for i, bucket in enumerate(self.tabela):
            if bucket:
                chaves_no_bucket = [par[0] for par in bucket]
                repr_str += f"Bucket {i}: {chaves_no_bucket}\n"
        return repr_str if repr_str else "Tabela Hash está vazia."