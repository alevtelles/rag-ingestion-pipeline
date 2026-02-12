# RAG Data Ingestion Pipeline

---
Implementação técnica de um **pipeline de ingestão de dados para arquitetura RAG (Retrieval-Augmented Generation)** utilizando Python, LangChain e ChromaDB como mecanismo de indexação vetorial.

Este repositório tem foco em **compreensão arquitetural e experimentação controlada**, não sendo um projeto orientado a produção.

---

# 1. Contexto Arquitetural

RAG combina dois componentes principais:

1. **Retriever** → Recupera contexto relevante via busca vetorial
2. **Generator (LLM)** → Gera resposta condicionada ao contexto recuperado

Este repositório cobre a primeira etapa crítica do sistema:

> **Pipeline de ingestão e indexação vetorial**

Fluxo implementado:

```
Raw Documents (.txt)
        ↓
Text Loading
        ↓
Chunking Strategy
        ↓
Embedding Generation
        ↓
Vector Index (ChromaDB)
        ↓
Persistent Storage
```

---

# 2. Estrutura do Repositório

```
.
├── docs/
│   ├── google.txt
│   ├── microsoft.txt
│   ├── nvidia.txt
│   ├── spacex.txt
│   └── tesla.txt
│
├── db/
│   └── chroma_db/
│       ├── chroma.sqlite3
│       └── (arquivos internos do índice vetorial)
│
├── ingestion_pipeline.py
├── pyproject.toml
├── poetry.lock
├── .env
└── .gitignore
```

### `docs/`

Fonte de dados bruta utilizada para testes de ingestão e avaliação de recuperação semântica.

### `db/chroma_db/`

Persistência local do índice vetorial gerado pelo ChromaDB.

### `ingestion_pipeline.py`

Script responsável por:

* Carregamento de documentos
* Aplicação de estratégia de divisão de texto
* Geração de embeddings
* Criação e persistência do índice vetorial

---

# 3. Stack Técnica

* **Python 3.10+**
* **LangChain**
* **ChromaDB (Persistent Vector Store)**
* **Modelo de Embeddings (OpenAI ou compatível)**
* **Poetry para gerenciamento de dependências**

---

# 4. Detalhamento do Pipeline

## 4.1 Document Loading

* Leitura de arquivos `.txt`
* Normalização básica
* Construção de objetos `Document`

## 4.2 Chunking Strategy

* Divisão baseada em caracteres ou tokens
* Controle de:

  * `chunk_size`
  * `chunk_overlap`
* Objetivo: equilibrar granularidade semântica e eficiência vetorial

## 4.3 Embedding Generation

* Conversão de texto em vetores de alta dimensionalidade
* Batch processing quando aplicável
* Modelo configurável via variável de ambiente

## 4.4 Vector Indexing

* Armazenamento dos embeddings no Chroma
* Persistência local via SQLite
* Indexação incremental possível

---

# 5. Setup do Ambiente

## 5.1 Instalação

```bash
git clone https://github.com/seu-usuario/rag-data-ingestion.git
cd rag-data-ingestion
poetry install
```

## 5.2 Configuração de Variáveis

Criar `.env`:

```env
OPENAI_API_KEY=your_api_key
```

---

# 6. Execução

```bash
poetry run python ingestion_pipeline.py
```

Ao executar:

* Os documentos são carregados
* São divididos em chunks
* Embeddings são gerados
* O índice vetorial é persistido em `db/chroma_db/`

---

# 7. Conceitos de Engenharia Trabalhados

* Arquitetura RAG
* Vetorização semântica
* Persistência vetorial
* Similaridade por cosseno
* Trade-offs de chunk size
* Separação entre ingestão e retrieval
* Fundamentos de indexação para sistemas LLM-aware

---

# 8. Limitações (Escopo de Estudo)

* Não há API exposta
* Não há controle de versionamento do índice
* Não há validação automática de qualidade de retrieval
* Não há estratégia de re-indexação incremental robusta

Este repositório serve como base conceitual antes da evolução para:

* FastAPI
* Observabilidade
* Pipelines assíncronos
* Deploy containerizado
* Orquestração em produção

---

# 9. Próximos Passos Técnicos

* Implementar módulo de retrieval separado
* Medir recall@k
* Testar múltiplos modelos de embedding
* Implementar semantic chunking
* Introduzir camada de avaliação automática

---

Se quiser, posso agora:

* Elevar ainda mais para nível arquitetura enterprise
* Ou deixar em formato ideal para portfólio de Engenharia de Dados + IA
* Ou estruturar como base para artigo técnico no LinkedIn

Qual direção você quer seguir?
