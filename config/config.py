import os

###################################### CAMINHOS ##############################################

# Pastas Gerais

PASTA_PROJETO = os.path.join(os.getcwd(), '..')
PASTA_DADOS   = os.path.join(PASTA_PROJETO, 'dados')


# Dados de Entrada

PASTA_DADOS_ENTRADA = os.path.join(PASTA_DADOS, 'entrada')

PASTA_DADOS_MORTALIDADE = os.path.join(PASTA_DADOS_ENTRADA, 'mortalidade')
PASTA_DADOS_QUALIDADE_AR = os.path.join(PASTA_DADOS_ENTRADA, 'qualidade_do_ar')

PASTA_DADOS_QUALIDADE_AR_DF = os.path.join(PASTA_DADOS_QUALIDADE_AR, 'DF_2015_2022')
PASTA_DADOS_QUALIDADE_AR_PE = os.path.join(PASTA_DADOS_QUALIDADE_AR, 'PE_2017_2022')
PASTA_DADOS_QUALIDADE_AR_SP = os.path.join(PASTA_DADOS_QUALIDADE_AR, 'SP_2015_2022')

# Dados Intermediários

PASTA_DADOS_INTERMED = os.path.join(PASTA_DADOS, 'intermediarios')

# Dados de saída

PASTA_DADOS_SAIDA = os.path.join(PASTA_DADOS, 'saida')