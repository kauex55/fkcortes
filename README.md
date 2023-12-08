## Agendamento de Corte

## Visão Geral

Este é um sistema de agendamento de cortes, permitindo que os clientes agendem serviços de corte de cabelo, barba, entre outros. Desenvolvido com Flask (Python) para o backend e utiliza HTML, CSS e JavaScript no frontend.

### Estrutura do Projeto

- **app.py:** Arquivo principal do servidor Flask que contém as rotas e a lógica do backend.
- **static/:** Pasta que contém arquivos estáticos (CSS, JavaScript, imagens).
- **templates/:** Pasta que contém os arquivos HTML usados para renderizar as páginas.

### Funcionalidades

1. **Agendamento de Corte:**
    - Os clientes podem agendar um corte escolhendo data, horário, tipo de serviço, nome e telefone.
    - Os dados são enviados para o servidor usando uma requisição POST.

2. **Exclusão de Agendamento:**
    - Os administradores podem excluir um agendamento específico.
    - A exclusão é realizada por meio de uma requisição DELETE ao servidor.

### Rotas e Descrição

1. **GET /**
    - **Descrição:** Rota inicial que exibe a página principal com o formulário de agendamento.

2. **POST /agendar**
    - **Descrição:** Rota para agendar um corte.
    - **Entrada:** Dados do agendamento (data, horário, serviço, nome, telefone).
    - **Saída:** Mensagem de confirmação ou erro.

3. **DELETE /agendamentos/{id}**
    - **Descrição:** Rota para excluir um agendamento específico.
    - **Entrada:** ID do agendamento a ser removido.
    - **Saída:** Mensagem de confirmação ou erro.

### Campos do Formulário de Agendamento

- **Data:** Escolha da data para o agendamento.
- **Horário:** Escolha do horário desejado.
- **Serviço:** Opções de serviço (corte, barba, corte e barba, etc.).
- **Nome:** Nome do cliente.
- **Telefone:** Número de telefone para contato.

### Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Comunicação entre Frontend e Backend:** Fetch API.

Este sistema permite uma fácil interação para agendamento e exclusão de cortes, proporcionando uma experiência amigável aos usuários.