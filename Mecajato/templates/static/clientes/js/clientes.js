function add_carro() {
    
    container = document.getElementById('form-carro')

    html = "<br> <div class='row'> <div class='col-md'> <input class='form-control' type='text' placeholder='Carro' name='carro'> </div> <div class='col-md'> <input class='form-control' type='text' placeholder='Placa' name='placa'> </div> <div class='col-md'> <input class='form-control' type='number' placeholder='Ano' name='ano'> </div> </div>"

    container.innerHTML += html
}

function exibir_form(tipo) {
    add_cliente = document.getElementById('adicionar-cliente');
    att_cliente = document.getElementById('att_cliente');

    if (tipo === "1") {
        att_cliente.style.display = "none";
        add_cliente.style.display = "block";
    } else if (tipo === "2") {
        att_cliente.style.display = "block";
        add_cliente.style.display = "none";
    }
}

function dados_cliente() {
    cliente = document.getElementById('cliente-select');
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    id_cliente = cliente.value
    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        aux = document.getElementById('form-att-cliente')
        aux.style.display = 'block'

        id = document.getElementById('id')
        id.value = data['cliente_id']

        console.log(data)

        document.getElementById('nome').value = data['cliente']['nome']
        document.getElementById('sobrenome').value = data['cliente']['sobrenome']
        document.getElementById('email').value = data['cliente']['email']
        document.getElementById('cpf').value = data['cliente']['cpf']

        div_carros = document.getElementById('carros')
        div_carros.innerHTML = ""

        for (i = 0; i < data['carros'].length; i++) {
            div_carros.innerHTML += "<form action='/clientes/update_carro/" + data['carros'][i]['id'] + "' method='POST'>\
            <div class='row'>\
                <div class='col-md'>\
                    <input class='form-control' type='text' name='carro' value='" + data['carros'][i]['fields']['carro'] + "'>\
                </div>\
                <div class='col-md'>\
                    <input class='form-control' type='text' name='placa' value='" + data['carros'][i]['fields']['placa'] + "'>\
                </div>\
                <div class='col-md'>\
                    <input class='form-control' type='text' name='ano' value='" + data['carros'][i]['fields']['ano'] + "'>\
                </div>\
                <div class='col-md'>\
                    <input class='btn btn-success' style='width: 100%;' type='submit' value='Salvar'>\
                </div>\
                <div class='col-md'>\
                    <a class='btn btn-danger' style='width: 100%;' href='/clientes/excluir_carro/" + data['carros'][i]['id'] + "'>Excluir</a>\
                </div>\
                </form>\
            </div>\
            <br>" 
        }
    })
}

function update_cliente() {
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value

    fetch('/clientes/update_cliente/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf
        })
    }).then(function(result){
        return result.json()
    }).then(function(data){
        if (data['status'] == '200'){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterados com sucesso')
        } else {
            console.log('Erro interno do servidor')
        }
    })
}