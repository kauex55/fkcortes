document.getElementById('agendamentoForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const data = document.getElementById('data').value;
    const horario = document.getElementById('horario').value;

    const agendamentoId = document.getElementById('agendamentoId').value;
    const method = agendamentoId ? 'PUT' : 'POST';
    const url = agendamentoId ? `/agendamentos/${agendamentoId}` : '/agendar';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            data: data,
            horario: horario
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);

        const recadoDiv = document.createElement('div');
        recadoDiv.innerText = 'Horário agendado com sucesso!';
        recadoDiv.className = 'recado';
        document.body.appendChild(recadoDiv);

        document.getElementById('agendamentoForm').reset();
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});

function excluirAgendamento(agendamentoId) {
    fetch(`/agendamentos/${agendamentoId}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function editarAgendamento(agendamentoId, data, horario) {
    document.getElementById('agendamentoId').value = agendamentoId;
    document.getElementById('data').value = data;
    document.getElementById('horario').value = horario;
    document.getElementById('submitBtn').innerText = 'Atualizar';
}
