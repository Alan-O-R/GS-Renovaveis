DIAS_MES = 30
TARIFA_KWH = 0.78938
GERACAO_FOTOVOLTAICA_MENSAL = 391.44
REDUCAO_AQUECIMENTO_SOLAR = 0.70
CONSUMO_MINIMO_BIFASICO_KWH = 50

perfil_residencial = {
    "orcamento":27000,
    "telhado_adequado":True,
    # "telhado_adequado":False,
    "infraestrutura_agua_quente":True,
    # "infraestrutura_agua_quente":False,
    "objetivo":"menor_investimento"
    # "objetivo":"menor_conta",
    # "objetivo":"mais_renovavel"
}

#dados simulados
aparelhos = [
    {
        "nome": "Chuveiro",
        "tipo": "diario",
        "potencia": 5500,
        "horas_dia": 0.8,
        "confiabilidade": "estimativa"
    },{
        "nome": "Geladeira",
        "tipo": "mensal",
        "consumo": 23,
        "confiabilidade": "fabricante"
    },{
        "nome": "Televisão",
        "tipo": "diario",
        "potencia": 205,
        "horas_dia": 3,
        "confiabilidade": "estimativa"
    },{
        "nome": "Maquina de lavar",
        "tipo": "ciclos",
        "consumo_ciclo": 0.40,
        "ciclos_mes": 12,
        "confiabilidade": "inmetro"
    },{
        "nome": "Lampadas LED",
        "tipo": "diario",
        "potencia": 76,
        "horas_dia": 5,
        "confiabilidade": "modelo candidato"
    },{
        "nome": "Computador + monitor",
        "tipo": "diario",
        "potencia": 87,
        "horas_dia": 4,
        "confiabilidade": "estimativa"
    },{
        "nome": "Ar-condicionado",
        "tipo": "diario",
        "potencia": 950,
        "horas_dia": 4,
        "confiabilidade": "estimativa"
    },{
        "nome": "Micro-ondas",
        "tipo": "diario",
        "potencia": 1250,
        "horas_dia": 20/60,
        "confiabilidade": "estimativa"
    },{
        "nome": "Ventilador",
        "tipo": "diario",
        "potencia": 140,
        "horas_dia": 3,
        "confiabilidade": "estimativa"
    },{
        "nome": "Air fryer",
        "tipo": "uso_mensal",
        "potencia": 1350,
        "horas_uso": 20/60,
        "usos_mes": 20,
        "confiabilidade": "estimativa"
    }
]

dados_financeiros = [
    {
        "nome":"Convencional",
        "investimento_min":0,
        "investimento_max":0,
        "nivel_renovavel":0,
        "beneficio_ambiental":(
            "Não exige novos equipamentos e "
            "evita o uso adicional de materia" ),
        "impacto_ambiental":(
            "Mantem o consumo dependente de "
            "eletricidade fornecida pela rede" ),
        "limitacao_ambiental":(
            "Não utiliza geração renovavel propia e "
            "não reduz diretamente o consumo da residência" )
    },{
        "nome":"Solar fotovoltaica",
        "investimento_min":13000, 
        "investimento_max":17000, 
        "nivel_renovavel":1,
        "beneficio_ambiental": (
            "Gera eletricidade a partir da energia solar "
            "e pode reduzir a necessidade de eletricidade da rede." ),
        "impacto_ambiental": (
            "A fabricação dos módulos e componentes utiliza "
            "materiais e energia e gera impactos ambientais." ),
        "limitacao_ambiental": (
            "Exige destinação adequada dos equipamentos "
            "ao final da vida útil e gerenciamento dos resíduos." )
    },{
        "nome":"Aquecimento solar",
        "investimento_min":6000, 
        "investimento_max":10000, 
        "nivel_renovavel":1,
        "beneficio_ambiental": (
            "Utiliza energia solar térmica para aquecer a água "
            "e pode reduzir o consumo elétrico do chuveiro." ),
        "impacto_ambiental": (
            "A fabricação dos coletores, reservatório e tubulações "
            "demanda materiais e energia." ),
        "limitacao_ambiental": (
            "Pode precisar de aquecimento auxiliar em períodos "
            "de menor disponibilidade de radiação solar." )
    },{
        "nome":"Fotovoltaica + aquecimento solar",
        "investimento_min":19000, 
        "investimento_max":27000, 
        "nivel_renovavel":2,
        "beneficio_ambiental": (
            "Combina geração de eletricidade fotovoltaica "
            "com aquecimento solar de água, reduzindo "
            "a dependência de energia da rede." ),
        "impacto_ambiental": (
            "A instalação utiliza materiais e componentes "
            "dos dois sistemas, aumentando os recursos "
            "necessários para sua fabricação." ),
        "limitacao_ambiental": (
            "Exige espaço, infraestrutura adequada "
            "e destinação correta dos componentes ao final "
            "da vida útil." )
    }
]