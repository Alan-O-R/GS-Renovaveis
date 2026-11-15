# Citizen Assist AI

Assistente inteligente para análise de consumo residencial e orientação sobre eficiência energética e fontes renováveis.

## Integrantes

- ALAN OTALVARO | RM: 571794
- JOÃO PEDRO RIBEIRO | RM: 570562
- JOÃO PEDRO EVANGELISTA | RM: 573899

## Sobre o projeto

O Citizen Assist AI é um assistente virtual desenvolvido com inteligência artificial generativa para auxiliar moradores a compreender seu consumo de energia elétrica, identificar oportunidades de economia e avaliar alternativas energéticas.

O projeto foi feito para a materia **Soluções em Energias Renováveis e Sustentáveis** e tem como objetivo integrar conceitos de energia, potência, eficiência energética e sustentabilidade a uma solução digital para o público.

O assistente utiliza cálculos realizados em Python e a API do Google Gemini para interpretar os resultados e apresentar orientações em linguagem natural.

As recomendações consideram o consumo residencial, os custos estimados, as condições de instalação e os impactos ambientais das alternativas avaliadas.

## Público-alvo e o problema deles

O público-alvo são moradores de residências que desejam compreender melhor seu consumo de energia elétrica e avaliar possibilidades de redução de gastos e adoção de fontes renováveis.

O problema abordado é a dificuldade de identificar o consumo dos equipamentos, identificar os principais responsáveis pelo gasto energético e comparar alternativas de economia e geração de energia.

O assistente busca facilitar esse processo por meio de diagnósticos, simulações e recomendações fundamentadas em dados e premissas explícitas.

## Funcionalidades

### 1. Diagnóstico de consumo residencial

O sistema analisa o consumo estimado dos equipamentos da residência e apresenta:

- Consumo mensal total em kWh.
- Custo energético estimado.
- Identificação dos equipamentos com maior consumo.
- Participação percentual de cada equipamento no consumo total.
- Oportunidades de economia e recomendações de eficiência energética.

### 2. Comparação de alternativas energéticas

O sistema compara quatro cenários:

- Convencional  - Consumo atendido pela rede elétrica, sem instalação adicional.
- Solar fotovoltaica  - Geração de eletricidade por meio de painéis solares.
- Aquecimento solar  - Utilização da energia solar térmica para aquecimento da água.
- Fotovoltaica + aquecimento solar  - Combinação das duas tecnologias.

A comparação considera investimento estimado, economia potencial, viabilidade de instalação e impactos ambientais.

### 3. Recomendações personalizadas

O assistente considera informações fornecidas pelo usuário:

- Orçamento disponível.
- É possivel fazer a instalação fotovoltaica no telhado
- Tem a infraestrutura para aquecimento solar de água.
- Objetivo principal: menor investimento, menor conta estimada ou maior utilização de fontes renováveis.

A seleção das alternativas viáveis é realizada pela lógica desenvolvida em Python. O Gemini interpreta os resultados e explica a recomendação ao usuário.

### 4. Simulação de redução do tempo de banho

Permite simular a economia de energia e o custo energético estimado ao reduzir o tempo de utilização do chuveiro elétrico.

A simulação considera:

- Tempo atual de banho.
- Novo tempo de banho.
- Quantidade de moradores.
- Potência configurada para o chuveiro.
- Tarifa energética utilizada pelo sistema.

O resultado apresenta a economia mensal estimada em kWh e reais.

### 5. Assistente conversacional com IA

O Google Gemini permite que o usuário interaja por meio de perguntas em linguagem natural.

O assistente pode explicar os resultados, esclarecer dúvidas, apresentar comparações e orientar o usuário sobre eficiência energética e alternativas renováveis.

Os cálculos energéticos e financeiros são realizados pelas funções Python, que servem como fonte principal dos resultados quantitativos.

---

## Cenário residencial utilizado

Para desenvolver e testar as análises, foi definido um cenário residencial hipotético.

- Localização  - São Paulo, SP
- Moradores  - 4 pessoas
- Período de análise  - 30 dias
- Tipo de residência  - Casa
- Fornecimento elétrico  - Rede convencional
- Conexão considerada  - Bifásica
- Geração solar inicial  - Inexistente
- Consumo mensal estimado  - 348,19 kWh

**Importante:** esse cenário representa uma residência simulada. Os valores não correspondem a medições reais de uma unidade consumidora.

## Análise do consumo energético

O consumo dos equipamentos é estimado a partir de sua potência, tempo de utilização e frequência de uso.

A fórmula utilizada para equipamentos de uso diário é:

- E = P * t * d / 1000

- E = energia consumida em kWh.
- P = potência do equipamento em watts.
- t = tempo diário de utilização em horas.
- d = quantidade de dias considerados.

Para equipamentos com consumo por ciclo ou consumo mensal informado, são utilizadas as respectivas informações de consumo e frequência.

### Principais consumidores identificados

| Equipamento | Consumo mensal | Participação |
|---|---:|---:|
| Chuveiro elétrico | 132 kWh | 37,9% |
| Ar-condicionado | 114 kWh | 32,7% |

O chuveiro e o ar-condicionado representam juntos aproximadamente 70,6% do consumo estimado da residência.

Por isso, recebem prioridade nas recomendações de eficiência energética.

**Observação:** os valores de consumo dependem das potências e dos hábitos de utilização considerados no cenário simulado.

## Premissas das alternativas renováveis

### Sistema fotovoltaico

O sistema fotovoltaico foi dimensionado a partir das estimativas de consumo residencial e potencial de geração solar.

Premissas utilizadas:

- Potência de referência do sistema: 3,5 kWp.
- Quantidade de módulos considerada: 7 módulos de 500 W.
- Horas de Sol Pleno (HSP): 4,66 horas por dia.
- Período de análise: 30 dias.
- Performance Ratio (PR): 80%.

A geração mensal de referência é estimada pela relação:

- E = P * HSP * d * PR

Com essas premissas, a geração estimada é de aproximadamente **391,44 kWh por mês**.

Esse valor representa uma estimativa de geração, não uma garantia de desempenho. A produção real depende das condições de instalação, orientação, inclinação, condições climáticas.

### Aquecimento solar de água

A alternativa de aquecimento solar considera um sistema de referência com:

- Reservatório térmico de 200 litros.
- Coletor solar de aproximadamente 3,6 m².
- Capacidade de referência de 24 tubos.
- Consumo de água quente estimado em 45 litros por pessoa ao dia.

Para quatro moradores, considera-se uma demanda de aproximadamente 180 litros de água quente por dia.

O modelo utiliza uma hipótese de redução de 70% do consumo elétrico associado ao chuveiro.

Essa redução é uma premissa de simulação baseada em referência técnica, não um resultado garantido para qualquer residência.

---

## Análise financeira

O sistema compara os investimentos estimados e o potencial de economia de cada alternativa.

### Investimentos de referência

| Alternativa | Investimento estimado |
|---|---:|
| Convencional | R$ 0 |
| Solar fotovoltaica | R$ 13.000 a R$ 17.000 |
| Aquecimento solar | R$ 6.000 a R$ 10.000 |
| Fotovoltaica + aquecimento solar | R$ 19.000 a R$ 27.000 |

Os valores são estimativas utilizadas no modelo e não representam orçamentos comerciais.

### Tarifa energética

O cenário utiliza uma tarifa de referência de:

**R$ 0,78938 por kWh.**

A tarifa foi baseada na tabela de referência da Enel São Paulo consultada para o projeto.

O custo energético estimado é calculado multiplicando o consumo em kWh pela tarifa adotada.

## Impactos ambientais

A comparação considera benefícios e limitações ambientais de cada alternativa.

| Alternativa | Benefícios ambientais | Limitações ambientais |
|---|---|---|
| Convencional | Não exige a instalação de novos equipamentos na residência. | Mantém a dependência da matriz elétrica e seus impactos ambientais. |
| Solar fotovoltaica | Produz eletricidade a partir de uma fonte renovável. | A fabricação, o transporte e o descarte dos módulos possuem impactos ambientais. |
| Aquecimento solar | Aproveita a energia solar térmica e reduz a necessidade de eletricidade para aquecimento da água. | Exige materiais, fabricação, instalação e manutenção dos equipamentos. |
| Fotovoltaica + aquecimento solar | Combina geração elétrica e aproveitamento térmico da energia solar. | Apresenta maior quantidade de equipamentos, materiais e requisitos de instalação. |

A análise ambiental é qualitativa e considera os benefícios e impactos associados às tecnologias.

O projeto não realiza uma avaliação completa do ciclo de vida nem calcula reduções quantitativas de emissões de gases de efeito estufa.

---

## Tecnologias utilizadas

- **Python:** implementação dos cálculos e regras de negócio.
- **Google Gemini API:** interpretação dos resultados e interação conversacional.
- **Google Gen AI SDK:** integração da aplicação com o modelo Gemini.
- **python-dotenv:** carregamento das variáveis de ambiente.

### Responsabilidade dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Inicialização e execução da aplicação. |
| `ai/gemini.py` | Comunicação com a API Gemini e configuração das ferramentas. |
| `data/system_prompt.txt` | Instruções, identidade e regras de comportamento do assistente. |
| `energia/dados.py` | Premissas, dados dos equipamentos, tarifas e investimentos. |
| `energia/consumo.py` | Cálculo e diagnóstico do consumo residencial. |
| `energia/alternativas.py` | Comparação energética e análise financeira das alternativas. |
| `energia/recomendacoes.py` | Seleção de alternativas viáveis e geração de recomendações. |

---

## Como executar o projeto

### 1. Pré-requisitos

- Acesso à internet.
- Chave de API do Google Gemini.

para rodar o projeto, primeiro é necessário clonar o projeto em sua maquina:

```bash
git clone https://github.com/Alan-O-R/GS-Renovaveis.git
```

Entre na pasta:

```bash
cd Citizen-Assist-AI
```

### 2. Criar um ambiente virtual

```bash
python -m venv venv
```

Ativar no Windows:

```bash
venv\Scripts\activate
```

Ativar no linux:

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a chave da API

Crie um arquivo `.env` na raiz do projeto seguindo o .env.exemplo

### 5. Executar o sistema

```bash
python main.py
```

Para encerrar a conversa, digite:

```text
sair
```

---

## Testes e validação

Os testes têm como objetivo verificar o funcionamento das ferramentas Python, a integração com o Gemini e a coerência das recomendações.

Cenários de teste realizados:

- Apresentação e identificação do assistente.
- Simulação de redução do tempo de banho.
- Análise residencial com orçamento limitado.
- Análise residencial com orçamento suficiente para instalação fotovoltaica.
- Verificação das condições de viabilidade das alternativas.
- Verificação da utilização dos resultados calculados pelo Python nas respostas do Gemini.

### Resultados e ajustes

Durante os testes, foram identificados comportamentos que exigiram ajustes:

- Solicitação desnecessária de tarifa ao usuário durante a simulação de banho.
- Respostas com cálculos próprios do Gemini em vez da utilização dos resultados da ferramenta Python.
- Recomendações de alternativas que ultrapassavam o orçamento informado.

Foram realizadas alterações nas instruções do assistente e nas regras de seleção das alternativas para corrigir esses comportamentos.

**Testes com usuários:** com ajuda da minha familia consegui identificar e corrigir esses erros.

- pergunta: Somos 4 pessoas e queremos reduzir o banho de 12 para 8 minutos. Quanto economizaremos por mês?
    resposta resumida: com certeza , me diga qual seria a tarifa de kWh por mês(a tarifa já tinha sido configurada)

- pergunta: mesma pergunta
    resposta resumida: teria uma economia de 40 kWh e economia financeira de R$ 48 (ele inventou a propia resposta , a resposta certa era 44 e R$ 34,73)

- pergunta: com 10 mil , telhado adequado , sem espaço para o aquecedor e procurando a opção mais renovavel
    resposta resumida: sua melhor opção é a instalação do sistema fotovoltaico (sendo que o orçamento era menor que o investimento maximo , para oferecer essa ideia o orçamento tem que ser maior que o investimento maximo por segurança)

esses testes nos permitiram arrumar problemas e confirmar o funcionamento esperado do assistente.

---

## Limitações do projeto

O Citizen Assist AI é uma ferramenta de orientação e simulação.

Principais limitações:

1. O consumo residencial é baseado em dados simulados e premissas de utilização, não em medições reais.
2. A geração fotovoltaica é estimada e pode variar conforme as condições locais.
3. A redução de consumo atribuída ao aquecimento solar é uma hipótese de referência.
4. Os custos de instalação são estimativas e variam conforme equipamentos, fornecedores e condições da residência.
5. O modelo financeiro fotovoltaico é simplificado e não representa integralmente as regras de faturamento e compensação da concessionária.
6. Os impactos ambientais são apresentados qualitativamente, sem análise completa do ciclo de vida ou quantificação de emissões.
7. As recomendações dependem das informações fornecidas pelo usuário e das premissas configuradas no sistema.

---

## Referências

As fontes devem permitir a verificação dos dados, cálculos e premissas utilizados no projeto.

- **Enel São Paulo:** tabela tarifária utilizada como referência para o custo do kWh. [https://www.gov.br/inmetro/pt-br/assuntos/regulamentacao/avaliacao-da-conformidade/programa-brasileiro-de-etiquetagem/tabelas-de-eficiencia-energetica]
- **Cooperluz:** tabela tarifária utilizada como referência para o custo do kWh. [https://www.cooperluz.com.br/tabela-de-consumo/]
- **INMETRO:** Programa Brasileiro de Etiquetagem e informações técnicas de equipamentos de aquecimento solar. [https://www.gov.br/inmetro/pt-br/assuntos/regulamentacao/avaliacao-da-conformidade/programa-brasileiro-de-etiquetagem/tabelas-de-eficiencia-energetica/equipamentos-de-aquecimento-solar-de-agua?]
- **Serasa/blog:** referência utilizada para dicas de redução do consumo elétrico. [https://www.serasa.com.br/blog/como-economizar-energia-eletrica-em-todos-os-comodos-da-casa/]
- **IEA PVPS:** estudos de avaliação do ciclo de vida de sistemas fotovoltaicos. [https://iea-pvps.org/fact-sheets/fact-sheet-environmental-life-cycle-assessment-of-electricity-from-pv-systems/]
- **Ministério de Minas e Energia:** materiais técnicos sobre eficiência energética e tecnologias solares. [https://www.gov.br/mme/pt-br/assuntos/ee/publicacoes-e-estudos/copy6_of_GuiadeEficienciaEnergeticaemEdificiosPblicosRevisao2024.pdf]
