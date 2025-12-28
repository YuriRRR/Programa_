🧑‍💻 Sistema de Cadastro com Automação
=======================================

Um projeto Python completo que combina uma interface gráfica para cadastro de pessoas com um sistema de automação para registro em massa.

📋 Descrição
------------

Este projeto é composto por dois componentes principais:

1.  **Sistema de Cadastro (GUI)** - Uma aplicação desktop desenvolvida com PyQt5 para cadastro, validação e gerenciamento de registros de pessoas
    
2.  **Script de Automação** - Um script que utiliza PyAutoGUI para automatizar o preenchimento de formulários a partir de um arquivo CSV
    

✨ Funcionalidades
-----------------

### Sistema de Cadastro (cadastro.py)

*   ✅ Interface gráfica amigável e moderna
    
*   ✅ Validação de campos (nome obrigatório, email válido, telefone formatado)
    
*   ✅ Armazenamento persistente em arquivo JSON
    
*   ✅ Listagem completa de cadastros em tabela
    
*   ✅ Sistema de logs em tempo real
    
*   ✅ Barra de status com contador de registros e hora atual
    
*   ✅ Menu com opções de ajuda e saída
    
*   ✅ Limpeza automática de campos após cadastro
    

### Script de Automação (automatização.py)

*   🤖 Leitura automática de arquivos CSV
    
*   🎯 Preenchimento automatizado de formulários via controle de mouse
    
*   ⏱️ Intervalos configuráveis entre registros
    
*   📊 Processamento em lote de múltiplos registros
    

🛠️ Tecnologias Utilizadas
--------------------------

*   **Python 3.x**
    
*   **PyQt5** - Para interface gráfica
    
*   **PyAutoGUI** - Para automação de interface
    
*   **JSON** - Para armazenamento de dados
    
*   **CSV** - Para importação de dados em lote

⚙️ Pré-requisitos
-----------------

Antes de executar, instale as dependências:

  `   pip install pyqt5 pyautogui   `

🚀 Como Executar
----------------

### 1\. Sistema de Cadastro (GUI)

Execute o sistema principal:

  `   python cadastro.py   `

**Interface:**

*   Preencha os campos do formulário
    
*   Clique em "✅ Confirmar" para salvar
    
*   Use "📋 Listar" para ver todos os cadastros
    
*   Use "🗑️ Limpar" para limpar os campos
    

### 2\. Script de Automação

Para executar a automação:

1.  Certifique-se de ter a janela do formulário aberta e visível
    
2.  Execute:
    
    `   python automatização.py   `

O script irá:

*   Ler o arquivo registros\_ficticios.csv
    
*   Preencher automaticamente cada registro no formulário
    
*   Aguardar 1 segundo entre cada cadastro
    

🔧 Configuração da Automação
----------------------------

O script automatização.py utiliza coordenadas de tela fixas. Para ajustar às suas necessidades use algum programa para identificar suas coordenadas
1.  Atualize as coordenadas no script conforme necessário.
    

📝 Observações Importantes
--------------------------

⚠️ **Atenção:**

*   O script de automação depende das coordenadas da tela
    
*   Certifique-se de que a janela do formulário esteja na mesma posição durante a execução
    
*   Recomenda-se testar com poucos registros primeiro
    
*   Mantenha o mouse e o teclado inativos durante a execução da automação
    

📄 Licença
----------

Este projeto é de uso educacional e pode ser modificado conforme necessário.

👨‍💻 Autor
-----------

Desenvolvido como exemplo de sistema de cadastro com automação em Python.

💡 **Dica:** Para uso em produção, considere adicionar:

*   Banco de dados em vez de arquivo JSON
    
*   Exportação para diferentes formatos (PDF, Excel)
    
*   Busca e filtros na lista de cadastros
    
*   Backup automático dos dados
