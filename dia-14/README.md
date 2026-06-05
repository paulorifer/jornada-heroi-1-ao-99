# Dia 14 — Estoque Conibase com JSON 

## O que foi praticado
- Lista de dicionários do zero
- Salvar dados em arquivo JSON com `json.dump()`
- Carregar dados de arquivo JSON com `json.load()`
- Uso de `encoding="utf-8"` para acentos
- Uso de `ensure_ascii=False` para caracteres especiais

## Código do dia

```python
import json

estoque = [
    {"nome": "cimento", "quantidade": 70, "categoria": "construção"},
    {"nome": "Argamassa", "quantidade": 197, "categoria": "construção"},
    {"nome": "Piso Formigues", "quantidade": 23, "categoria": "construção"}
]

# Salvar no arquivo
with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(estoque, arquivo, ensure_ascii=False)

# Carregar do arquivo
with open("estoque.json", "r", encoding="utf-8") as arquivo:
    estoque_carregado = json.load(arquivo)

print(estoque_carregado)
```

## Aprendizado do dia
- `dump` → Python pro arquivo
- `load` → arquivo pro Python
- Contexto real: estoque da Conibase