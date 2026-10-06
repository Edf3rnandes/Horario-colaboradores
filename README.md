# Planner de Treinos

Planner por unidade (Altiplano, Bancários, Bessa e Cabo Branco) gerado a partir de `horario_colaborador.xlsx`.

- Abra `index.html` no navegador (não precisa de servidor).
- Por unidade: **Semana** (grade), **Turmas** (tabela), **Equipe** (professores/auxiliares) e **Quadras** (turmas simultâneas x quadras).
- **Conflitos**: pessoas em duas turmas ao mesmo tempo, troca de unidade sem intervalo, turmas sem auxiliar.
- A quantidade de quadras de cada unidade é digitada na própria página (fica salva no navegador).

## Editar equipe e funções

- Clique em uma turma (na grade ou em **Turmas → Editar**) para trocar o professor responsável e os auxiliares. O editor avisa se a pessoa já estiver em outra turma no mesmo horário. Ali também se escolhe **quantas quadras a turma usa** (padrão 1); a aba **Quadras** soma isso por horário e compara com as quadras da unidade.
- Em **Equipe**, marque cada pessoa como 🎓 Professor (formado) ou 🌱 Estagiário. A **Visão geral** lista os formados e os estagiários.
- As alterações ficam salvas no navegador. Em **Visão geral → Alterações** dá para baixar o `ajustes.json`. Colocando esse arquivo na raiz do repositório e rodando `python3 build.py`, as alterações passam a valer para todos.

## Matrículas e limite da turma

Use **📋 Colar matrículas** (na barra da unidade ou na Visão geral) e cole as linhas copiadas do sistema (`id, Nome, Descrição, Categoria, Unidade, Qtd. Matrículas, Limite`). A turma é encontrada pelo nome + unidade. Aparece como 👥 5/15 na grade (amarelo a partir de 80%, vermelho quando lotada) e como coluna **Alunos** na tabela, com as vagas restantes. Os valores atuais estão em `ajustes.json`.

## Atualizar a planilha

Edite `horario_colaborador.xlsx` (aba `Plan1`) e rode:

```
pip install openpyxl
python3 build.py
```

Isso regenera o `index.html` a partir de `template.html`.
