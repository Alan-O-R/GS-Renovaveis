from energia.dados import (dados_financeiros, 
                           GERACAO_FOTOVOLTAICA_MENSAL, 
                           REDUCAO_AQUECIMENTO_SOLAR,
                           TARIFA_KWH,
                           CONSUMO_MINIMO_BIFASICO_KWH )

def comparar_alternativas(diagnostico):
    consumo_total = diagnostico["consumo_total"]
    consumo_chuveiro = next(
        (aparelho["consumo"] for aparelho in diagnostico["maiores_consumidores"]
        if aparelho["nome"] == "Chuveiro"),0
        )
    economia_aquecimento = (consumo_chuveiro * REDUCAO_AQUECIMENTO_SOLAR)
    consumo_com_aquecimento = max(0,consumo_total-economia_aquecimento)
    
    alternativas = [
        {
            "nome":"Convencional",
            "consumo":consumo_total,
            "geracao_solar":0
        },
        {
            "nome":"Solar fotovoltaica",
            "consumo": consumo_total,
            "geracao_solar": GERACAO_FOTOVOLTAICA_MENSAL
        },
        {
            "nome":"Aquecimento solar",
            "consumo":consumo_com_aquecimento,
            "geracao_solar":0
        },
        {
            "nome":"Fotovoltaica + aquecimento solar",
            "consumo":consumo_com_aquecimento,
            "geracao_solar": GERACAO_FOTOVOLTAICA_MENSAL
        }]
    return alternativas


def calcular_conta_estimada(consumo , geracao_solar):
    consumo_liquido = max(0 , consumo - geracao_solar)
    consumo_faturavel = max(consumo_liquido, CONSUMO_MINIMO_BIFASICO_KWH)
    return consumo_faturavel * TARIFA_KWH


def calcular_retorno(investimento , economia_mesal):
    
    if economia_mesal <= 0 or investimento <= 0:
        return None
    
    retorno_meses = investimento / economia_mesal
    
    retorno_anos = retorno_meses / 12
    
    return retorno_anos


def analisar_financeiro(alternativas):
    resultados = []
    
    convencional = next(
        (
            item for item in alternativas if item["nome"] == "Convencional"
        ), None )
    if convencional is None:
        raise ValueError("Alternativa convencional não foi encontrada")
    conta_base = calcular_conta_estimada(convencional["consumo"] , convencional["geracao_solar"])
    
    for alternativa in alternativas:
        financeiro = next(
            (
                item for item in dados_financeiros
                if item["nome"] == alternativa["nome"]
            ), None )
        
        if financeiro is None:
            raise ValueError(f"Dados financeiros não encontrados: {alternativa['nome']}")
        
        conta_estimada = calcular_conta_estimada(alternativa["consumo"] , alternativa["geracao_solar"])
        
        economia_mensal = max(0 , conta_base - conta_estimada)
        
        retorno_min = calcular_retorno(financeiro["investimento_min"], economia_mensal)
        
        retorno_max = calcular_retorno(financeiro["investimento_max"], economia_mensal)
        
        resultados.append({
            **alternativa,
            **financeiro,
            "conta_estimada": conta_estimada,
            "economia_mensal":economia_mensal,
            "retorno_min":retorno_min,
            "retorno_max":retorno_max,
        })
    return resultados


def ordenar_retorno(alternativa):
    retorno = alternativa["retorno_max"]
    return float("inf") if retorno is None else retorno




