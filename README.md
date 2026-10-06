# Planner de Treinos

Planner por unidade (Altiplano, Bancários, Bessa e Cabo Branco) gerado a partir de `horario_colaborador.xlsx`.

- Abra `index.html` no navegador (não precisa de servidor).
- Por unidade: **Semana** (grade), **Turmas** (tabela), **Equipe** (professores/auxiliares) e **Quadras** (turmas simultâneas x quadras).
- **Conflitos**: pessoas em duas turmas ao mesmo tempo, troca de unidade sem intervalo, turmas sem auxiliar.
- A quantidade de quadras de cada unidade é digitada na própria página (fica salva no navegador).

## Atualizar a planilha

Edite `horario_colaborador.xlsx` (aba `Plan1`) e rode:

```
pip install openpyxl
python3 build.py
```

Isso regenera o `index.html` a partir de `template.html`.
