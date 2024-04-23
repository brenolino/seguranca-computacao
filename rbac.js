// Simulando um hospital, onde diferentes pessoas tem diferentes funções.

// Cargos existentes no hospital.
const cargos = {
    medico: ['acessarProntuario', 'prescreverMedicação', 'acessarMedicamentos'],
    enfermeiro: ['lerSinaisVitais', 'acessarMedicamentos', 'administrarMedicamentos'],
    farmaceutico: ['acessarMedicamentos', 'gerenciarEstoque'],
    secretaria: ['gerenciarUsuários', 'configurarSistema', 'gerarRelatórios']
}

// Usuários cadastrados no hospital.
const usuarios = [
    {nome: 'Alice', cargo: 'medico'},
    {nome: 'Bianca', cargo: 'enfermeiro'},
    {nome: 'Carlos', cargo: 'farmaceutico'},
    {nome: 'Diego', cargo: 'admin'}
];

// Função para verificar se determinada pessoa tem acesso a uma determinada função.
function verificarPermissao(nome, acao) {
    const usuario = usuarios.find(usuario => usuario.nome == nome);

    if (!usuario) {
        console.log('Usuário não encontrado.');
        return false;
    }

    const permissões = cargos[usuario.cargo];
    if (!permissões || !permissões.includes(acao)) {
        console.log(`Usuário ${nome} não tem permissão para ${acao}.`);
        return false;
    }

    console.log(`Usuário ${nome} tem permissão para ${acao}.`);
    return true;
}

function removerCargo(nome){
    const usuario = usuarios.find(usuario => usuario.nome == nome);
    if(!usuario) return false;
    usuario.cargo = null;
    return true;
}

// Verificando se tal pessoa pode realizar a ação.
verificarPermissao('Alice', 'prescreverMedicação');
verificarPermissao('Bianca', 'gerenciarEstoque');
verificarPermissao('Carlos', 'acessarMedicamentos');
verificarPermissao('Diego', 'configurarSistema');

// Removendo cargo e verificando a ação anterior.
removerCargo('Alice');
verificarPermissao('Alice', 'prescreverMedicação');