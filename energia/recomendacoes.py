from energia.dados import (DIAS_MES , TARIFA_KWH , aparelhos , GERACAO_FOTOVOLTAICA_MENSAL , REDUCAO_AQUECIMENTO_SOLAR , CONSUMO_MINIMO_BIFASICO_KWH)
from energia.consumo import (gerar_diagnostico , analisar_aparelhos)
from energia.alternativas import (comparar_alternativas , analisar_financeiro , ordenar_retorno)


def selecionar_recomendacao(resultados_financeiros , perfil):
    objetivo = perfil["objetivo"]
    alternativas_viaveis = []
    alternativas_descartadas = []
    
    for alternativa in resultados_financeiros:
        nome = alternativa["nome"]
        motivos =[]
        
        if nome == "Convencional":
            continue
        
        if perfil["orcamento"] < alternativa["investimento_max"]:
            motivos.append("Investimento maximo acima do orçamento")
        
        if nome in ["Solar fotovoltaica","Fotovoltaica + aquecimento solar"] and not perfil["telhado_adequado"]:
            motivos.append("Telhado inadequado")
        
        if nome in ["Aquecimento solar" , "Fotovoltaica + aquecimento solar"] and not perfil["infraestrutura_agua_quente"]:
            motivos.append("Não tem infraestrutura para aquecimento solar")

        if motivos: 
            alternativas_descartadas.append({
                "nome":nome,
                "motivos": motivos
            })
        else:
            alternativas_viaveis.append(alternativa)
            
    if not alternativas_viaveis:
        return {
            "objetivo": objetivo,
            "recomendacao_principal": "Eficiência energética",
            "alternativas_complementares": [],
            "alternativas_descartadas": alternativas_descartadas,
            "motivo": (
                "Nenhuma alternativa de investimento "
                "atende às condições informadas" )
        }
        
    if objetivo == "menor_investimento":
        alternativas_viaveis.sort(
            key=lambda item: (
                item["investimento_max"], 
                item["investimento_min"] )
        )
    elif objetivo == "menor_conta":
        alternativas_viaveis.sort(
            key=lambda item:(
                item["conta_estimada"], 
                item["investimento_min"]
            )
        )
    elif objetivo == "mais_renovavel":
        alternativas_viaveis.sort(
            key=lambda item:(
                -item["nivel_renovavel"],
                ordenar_retorno(item)
            )
        )
    else:
        raise ValueError("Objetivo de decisão invalido")
    
    principal = alternativas_viaveis[0]
    return {
        "objetivo":objetivo,
        "recomendacao_principal": principal["nome"],
        "investimento_min": principal["investimento_min"],
        "investimento_max":principal["investimento_max"],
        "conta_estimada": principal["conta_estimada"],
        "economia_mensal": principal["economia_mensal"],
        "retorno_min": principal["retorno_min"],
        "retorno_max": principal["retorno_max"],
        "beneficio_ambiental": principal["beneficio_ambiental"],
        "impacto_ambiental": principal["impacto_ambiental"],
        "limitacao_ambiental": principal["limitacao_ambiental"],
        "alternativas_complementares": alternativas_viaveis[1:],
        "alternativas_descartadas":alternativas_descartadas,
        "motivo": (
            f"Alternativa selecionada considerando o objetivo: {objetivo}. "
            "A escolha também respeita as condições de orçamento "
            "e infraestrutura informadas."
        )
    }


def simular_reducao_banho(minutos_atuais:int , minutos_novos:int , moradores:int)-> dict:
    """
    Calcula a economia mensal de energia e dinheiro
    ao reduzir o tempo de banho.

    Esta ferramenta deve ser utilizada sempre que o usuário
    solicitar uma simulação de redução do tempo de banho.

    Parâmetros:
        minutos_atuais: Duração atual do banho.
        minutos_novos: Nova duração desejada.
        moradores: Quantidade de moradores.

    A tarifa e a potência do chuveiro são obtidas
    automaticamente dos dados do sistema.
    """
    
    if minutos_atuais <= 0 or minutos_novos<=0:
        return{"Erro": "os tempos devem ser maiores que zero"}
    if minutos_novos>=minutos_atuais:
        return {"Erro": "o novo tempo deve ser menor que o atual"}
    if moradores<=0 or moradores>15:
        return {"Erro": "quantidade de moradores invalida"}
    
    chuveiro = next(
        (aparelho for aparelho in aparelhos
        if aparelho["nome"] == "Chuveiro"), None)
    if chuveiro is None:
        return{"ERRO": "Dados do chuveiro não foram encontrados"}
    
    potencia_chuveiro = chuveiro["potencia"]
    diferenca_minutos = minutos_atuais - minutos_novos
    horas_economizadas = (diferenca_minutos*moradores*DIAS_MES)/60
    consumo_economizado = (potencia_chuveiro*horas_economizadas)/1000
    economia_reais = consumo_economizado*TARIFA_KWH
    
    return{
        "economia_mensal_kwh": round(consumo_economizado, 2),
        "economia_mensal_reais": round(economia_reais, 2),
        "novo_tempo_banho": minutos_novos,
        "tempo_reduzido": diferenca_minutos,
        "moradores": moradores,
        "observacao": (
        "Estimativa considerando potência máxima do chuveiro "
        "durante todo o banho." )
    }



def analisar_residencia(orcamento: float , telhado_adequado: bool , infraestrutura_agua_quente: bool , objetivo: str):
    """
    Analisa o consumo energético da residência,
    compara alternativas e seleciona recomendações conforme
    as caracteristicas informadas pelo morador.

    Args:
        orcamento: Investimento máximo disponível em reais.
        telhado_adequado: Indica se o telhado é adequado para instalação fotovoltaica.
        infraestrutura_agua_quente: Indica se a residência possui infraestrutura para aquecimento solar.
        objetivo: menor_investimento, menor_conta ou mais_renovavel.

    Retorna:
        dict: Diagnóstico, alternativas, resultados financeiros ,
        recomendações , perfil e premissas da simulação
    """
    objetivos_validos = [
        "menor_investimento",
        "menor_conta",
        "mais_renovavel"
    ]
    if isinstance(orcamento, bool) or not isinstance(orcamento, (int, float)) or orcamento < 0:
        raise ValueError("O orçamento não pode ser negativo.")
    
    if not isinstance(telhado_adequado, bool):
        raise ValueError("A adequação do telhado deve ser True ou False.")

    if not isinstance(infraestrutura_agua_quente, bool):
        raise ValueError("A infraestrutura de água quente deve ser True ou False.")

    if objetivo not in objetivos_validos:
        raise ValueError("Objetivo de decisão inválido.")
    
    perfil = {
        "orcamento": orcamento,
        "telhado_adequado": telhado_adequado,
        "infraestrutura_agua_quente": infraestrutura_agua_quente,
        "objetivo": objetivo
    }
    diagnostico = gerar_diagnostico(analisar_aparelhos(aparelhos))
    
    alternativas = comparar_alternativas(diagnostico)
    
    resultados_financeiros = analisar_financeiro(alternativas)
    
    recomendacoes = selecionar_recomendacao(resultados_financeiros,perfil)

    premissas = {
        "periodo_dias": DIAS_MES,
        "tarifa_kwh": TARIFA_KWH,
        "geracao_fotovoltaica_mensal": GERACAO_FOTOVOLTAICA_MENSAL,
        "reducao_aquecimento_solar": REDUCAO_AQUECIMENTO_SOLAR,
        "consumo_minimo_bifasico_kwh": CONSUMO_MINIMO_BIFASICO_KWH,
        "origem_dados": "Residencia hipotetica com dados simulados"
    }
    
    limitacoes = [
        "O consumo dos aparelhos é baseado em estimativas e dados de referência.",
        "A geração fotovoltaica é uma estimativa mensal, não uma garantia.",
        "A redução do consumo do chuveiro com aquecimento solar é uma hipótese de simulação.",
        "Os custos de instalação são estimativas, não orçamentos comerciais.",
        "A conta de energia utiliza um modelo simplificado de compensação solar.",
        "Os impactos ambientais são descrições qualitativas, não uma análise completa do ciclo de vida."
    ]
    
    return{
        "perfil_residencial": perfil,
        "premissas": premissas,
        "diagnostico": diagnostico,
        "alternativas": alternativas,
        "financeiro": resultados_financeiros,
        "recomendacoes": recomendacoes,
        "limitacoes": limitacoes
    }