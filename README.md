# Estudo Dirigido de Processamento Digital de Sinais — Parte 2

**Instituto Federal da Paraíba (IFPB) — Campus Campina Grande**  
**Disciplina:** Processamento Digital de Sinais  
**Professor:** Moacy Pereira da Silva  
**Período:** 2026.2

## Descrição

Este repositório reúne os materiais desenvolvidos para a segunda parte do Estudo Dirigido de Processamento Digital de Sinais, cujo tema é **Fourier, Laplace, Transformada-Z e Análise de Sistemas**.

O trabalho tem como objetivo compreender e aplicar diferentes representações matemáticas de sinais e sistemas, relacionando os domínios do tempo, da frequência, o plano-s e o plano-z.

As atividades incluem fundamentação teórica, formulações matemáticas, implementações computacionais, simulações, análise de resultados e o desenvolvimento de um mini-projeto integrador.

## Conteúdo do trabalho

O estudo contempla 18 tópicos, abrangendo:

- Frequência e exponenciais complexas;
- Transformada de Fourier em Tempo Discreto (DTFT);
- Transformada Discreta de Fourier (DFT) e FFT;
- Resolução espectral e frequência normalizada;
- Teorema da Amostragem de Nyquist e aliasing;
- Vazamento espectral e funções janela;
- Transformada de Laplace e função de transferência;
- Polos, zeros e estabilidade no plano-s;
- Transformada-Z e análise de sistemas discretos;
- Relação entre os planos-s e z.

Além da parte teórica, o trabalho apresenta simulações para investigar e interpretar os conceitos estudados.

## Organização do repositório

A estrutura abaixo segue a organização sugerida pelo professor:

```text
PDS-Parte-2/
│
├── relatorio/
│
├── simulacoes/
│   ├── fourier/
│   ├── dft-fft/
│   ├── nyquist-aliasing/
│   ├── janelamento/
│   ├── laplace/
│   └── transformada-z/
│
├── mini-projeto/
│   ├── codigo/
│
│
└── README.md
```

### Descrição das pastas

| Diretório | Conteúdo |
|---|---|
| `relatorio/` | Relatório técnico com fundamentação, formulações, análises e conclusões. |
| `simulacoes/` | Códigos e experimentos organizados por assunto. |
| `mini-projeto/` | Implementação e materiais do projeto integrador. |
| `resultados/` | Resultados e arquivos complementares das análises. |

## Mini-projeto integrador

**Tema: Monitoramento de Vibrações de uma Máquina**

Como aplicação dos conceitos estudados, foi desenvolvido um mini-projeto de análise multidomínio de um sinal de vibração mecânica.

O projeto utiliza sinais simulados para investigar suas características temporais e espectrais, além de analisar o comportamento dinâmico de um sistema mecânico nos domínios contínuo e discreto.

Entre as atividades desenvolvidas estão a geração e amostragem de sinais, análise por FFT, investigação de aliasing e janelamento, modelagem de um sistema de segunda ordem, discretização por ZOH e análise de polos e estabilidade.

## Ferramentas computacionais

As simulações foram desenvolvidas em Python, utilizando bibliotecas para cálculos numéricos, processamento de sinais, análise de sistemas e visualização gráfica.

Principais bibliotecas:

- NumPy
- SciPy
- Matplotlib

## Execução das simulações

Para preparar o ambiente Python, instale as dependências:

```bash
python -m pip install numpy scipy matplotlib
```

Os códigos estão organizados nas pastas de `simulacoes/` e `mini-projeto/codigo/`. A execução deve ser realizada conforme o arquivo Python correspondente à análise desejada.

## Resultados e documentação

O relatório técnico reúne a fundamentação dos conceitos, as equações utilizadas, os procedimentos computacionais e a interpretação dos resultados obtidos.

Os gráficos permitem observar características dos sinais e sistemas, incluindo espectros de magnitude e fase, efeitos da amostragem, vazamento espectral, respostas temporais e diagramas de polos e zeros.

## Considerações finais

O estudo dirigido busca integrar teoria e prática, demonstrando como Fourier, Laplace e Transformada-Z oferecem diferentes perspectivas para a análise de sinais e sistemas.

A aplicação desses conhecimentos ao mini-projeto de vibrações permite relacionar os fundamentos do Processamento Digital de Sinais com problemas de engenharia, especialmente no contexto de análise de sistemas e monitoramento de equipamentos.

---

**IFPB — Campus Campina Grande | 2026**
