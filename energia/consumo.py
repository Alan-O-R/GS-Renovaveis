from energia.dados import DIAS_MES , TARIFA_KWH


def calcular_consumo(aparelho):
    tipo = aparelho["tipo"]
    if tipo == "diario":
        consumo = (aparelho["potencia"] * aparelho["horas_dia"] * DIAS_MES ) / 1000
    elif tipo == "mensal":
        consumo = aparelho["consumo"]
    elif tipo == "ciclos":
        consumo = (aparelho["consumo_ciclo"] * aparelho["ciclos_mes"])
    elif tipo == "uso_mensal":
        consumo = (aparelho["potencia"] * aparelho["horas_uso"] * aparelho["usos_mes"]) / 1000
    else:
        raise ValueError(f"Tipo de calculo invalido: {tipo}")
    return consumo


def analisar_aparelhos(lista_aparelhos):
    resultados = []
    
    for aparelho in lista_aparelhos:
        consumo = calcular_consumo(aparelho)
        resultados.append({
                "nome" : aparelho["nome"],
                "consumo" : consumo,
                "confiabilidade" : aparelho["confiabilidade"]
            })
    return resultados


def calcular_participacao(resultados , consumo_total):
    for aparelho in resultados:
        if consumo_total > 0:
            participacao = ( aparelho["consumo"] / consumo_total) * 100
        else:
            participacao = 0
        
        aparelho["participacao"] = participacao
    return resultados


def identificar_oportunidades(resultados):
    oportunidades = []
    
    for aparelho in resultados:
        nome = aparelho["nome"]
        participacao = aparelho["participacao"]
        
        if nome == "Chuveiro" and participacao >=20:
            oportunidades.append({
                "aparelho":nome,
                "prioridade":"Alta",
                "recomendacao":"Avaliar aqueciemnto solar de agua e redução do tempo de banho" } )
        elif nome == "Ar-condicionado" and participacao >=20:
            oportunidades.append({
                "aparelho":nome,
                "prioridade":"Alta",
                "recomendacao":"Avaliar ajustes de temperatura e tempo de utilização e eficiência" } )
        elif nome == "Geladeira" and participacao >=10:
            oportunidades.append({
                "aparelho":nome,
                "prioridade":"Media",
                "recomendação":"Verificar vedação,temperatura e eficiência energetica" } )
        elif participacao>=10:
            oportunidades.append({
                "aparelho":nome,
                "prioridade":"Media",
                "recomendação":"Invertigar habitos de utilização para identificar possiveis economias" } )
    return oportunidades


def gerar_diagnostico(resultados):
    consumo_total = sum(aparelho["consumo"] for aparelho in resultados)
    
    resultados = calcular_participacao(resultados , consumo_total)
    custo_estimado = consumo_total * TARIFA_KWH
    maiores_consumidores = sorted(resultados, key= lambda aparelho:aparelho["consumo"], reverse= True)
    oportunidades = identificar_oportunidades(maiores_consumidores)
    return{
        "consumo_total" : consumo_total,
        "custo_estimado" : custo_estimado,
        "maiores_consumidores" : maiores_consumidores,
        "oportunidades":oportunidades
    }
