document.getElementById('agendamentoForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const data = document.getElementById('data').value;
    const horario = document.getElementById('horario').value;

    fetch('./agendar.html', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data, horario }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});
