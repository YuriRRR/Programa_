import sys
import json
from datetime import datetime
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer

class CadastroApp:
    def __init__(self):
        # Carregar a interface
        self.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
        self.formulario = uic.loadUi("cadastro.ui")
        
        # Lista para armazenar cadastros
        self.cadastros = []
        
        # Carregar cadastros existentes
        self.carregar_cadastros()
        
        # Conectar botões
        self.formulario.pushButton_confirmar.clicked.connect(self.cadastrar)
        self.formulario.pushButton_limpar.clicked.connect(self.limpar_campos)
        self.formulario.pushButton_listar.clicked.connect(self.listar_cadastros)
        
        # Conectar ações do menu
        self.formulario.actionSair.triggered.connect(self.sair)
        self.formulario.actionSobre.triggered.connect(self.mostrar_sobre)
        
        # Configurar validações
        self.setup_validacoes()
        
        # Configurar timer para atualização automática
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_status)
        self.timer.start(1000)  # Atualizar a cada 1 segundo
        
        # Configurar logs
        self.log("Sistema iniciado")
        
    def setup_validacoes(self):
        """Configurar validações nos campos"""
        # Configurar máscara para telefone
        self.formulario.lineEdit_telefone.setInputMask("(99) 99999-9999;_")
        
    def validar_email(self, email):
        """Validação simples de email"""
        if "@" in email and "." in email:
            return True
        return False
    
    def validar_telefone(self, telefone):
        """Validação de telefone"""
        telefone_limpo = ''.join(filter(str.isdigit, telefone))
        return len(telefone_limpo) >= 10
    
    def cadastrar(self):
        """Função principal de cadastro"""
        # Coletar dados
        nome = self.formulario.lineEdit_nome.text().strip()
        cidade = self.formulario.lineEdit_cidade.text().strip()
        email = self.formulario.lineEdit_email.text().strip()
        telefone = self.formulario.lineEdit_telefone.text().strip()
        idade = self.formulario.spinBox_idade.value()
        
        # Validar campos obrigatórios
        if not nome:
            self.mostrar_erro("Por favor, preencha o nome!")
            return
        
        if not self.validar_email(email):
            self.mostrar_erro("Por favor, insira um email válido!")
            return
        
        if not self.validar_telefone(telefone):
            self.mostrar_erro("Por favor, insira um telefone válido!")
            return
        
        # Criar dicionário com os dados
        cadastro = {
            'nome': nome,
            'cidade': cidade,
            'email': email,
            'telefone': telefone,
            'idade': idade,
            'data_cadastro': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        # Adicionar à lista
        self.cadastros.append(cadastro)
        
        # Salvar em arquivo
        self.salvar_cadastros()
        
        # Mostrar mensagem de sucesso
        QMessageBox.information(self.formulario, "Sucesso!", 
                              f"Cadastro realizado com sucesso!\n\n"
                              f"Nome: {nome}\n"
                              f"Cidade: {cidade}\n"
                              f"Email: {email}\n"
                              f"Telefone: {telefone}\n"
                              f"Idade: {idade}")
        
        # Adicionar ao log
        self.log(f"Cadastro realizado: {nome} - {email}")
        
        # Limpar campos
        self.limpar_campos()
        
        # Atualizar status
        self.atualizar_status()
        
    def limpar_campos(self):
        """Limpar todos os campos do formulário"""
        self.formulario.lineEdit_nome.clear()
        self.formulario.lineEdit_cidade.clear()
        self.formulario.lineEdit_email.clear()
        self.formulario.lineEdit_telefone.clear()
        self.formulario.spinBox_idade.setValue(0)
        self.formulario.lineEdit_nome.setFocus()
        
    def carregar_cadastros(self):
        """Carregar cadastros de arquivo JSON"""
        try:
            with open('cadastros.json', 'r', encoding='utf-8') as f:
                self.cadastros = json.load(f)
            self.log(f"Carregados {len(self.cadastros)} cadastros")
        except FileNotFoundError:
            self.cadastros = []
            self.log("Nenhum cadastro anterior encontrado")
        except Exception as e:
            self.log(f"Erro ao carregar cadastros: {str(e)}")
    
    def salvar_cadastros(self):
        """Salvar cadastros em arquivo JSON"""
        try:
            with open('cadastros.json', 'w', encoding='utf-8') as f:
                json.dump(self.cadastros, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.log(f"Erro ao salvar cadastros: {str(e)}")
    
    def listar_cadastros(self):
        """Listar todos os cadastros em uma nova janela"""
        if not self.cadastros:
            self.mostrar_erro("Não há cadastros para listar!")
            return
        
        # Criar uma nova janela para exibir a lista
        lista_window = QtWidgets.QDialog(self.formulario)
        lista_window.setWindowTitle("Lista de Cadastros")
        lista_window.setGeometry(100, 100, 700, 400)
        
        # Criar tabela
        tabela = QtWidgets.QTableWidget(lista_window)
        tabela.setGeometry(10, 10, 680, 350)
        
        # Configurar colunas
        colunas = ['Nome', 'Cidade', 'Email', 'Telefone', 'Idade', 'Data Cadastro']
        tabela.setColumnCount(len(colunas))
        tabela.setHorizontalHeaderLabels(colunas)
        
        # Preencher tabela
        tabela.setRowCount(len(self.cadastros))
        for i, cadastro in enumerate(self.cadastros):
            tabela.setItem(i, 0, QtWidgets.QTableWidgetItem(cadastro['nome']))
            tabela.setItem(i, 1, QtWidgets.QTableWidgetItem(cadastro['cidade']))
            tabela.setItem(i, 2, QtWidgets.QTableWidgetItem(cadastro['email']))
            tabela.setItem(i, 3, QtWidgets.QTableWidgetItem(cadastro['telefone']))
            tabela.setItem(i, 4, QtWidgets.QTableWidgetItem(str(cadastro['idade'])))
            tabela.setItem(i, 5, QtWidgets.QTableWidgetItem(cadastro['data_cadastro']))
        
        # Ajustar largura das colunas
        tabela.resizeColumnsToContents()
        
        # Botão para fechar
        btn_fechar = QtWidgets.QPushButton("Fechar", lista_window)
        btn_fechar.setGeometry(300, 370, 100, 25)
        btn_fechar.clicked.connect(lista_window.close)
        
        lista_window.exec_()
    
    def log(self, mensagem):
        """Adicionar mensagem ao log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.formulario.textEdit_log.append(f"[{timestamp}] {mensagem}")
        
        # Rolar para o final
        cursor = self.formulario.textEdit_log.textCursor()
        cursor.movePosition(cursor.End)
        self.formulario.textEdit_log.setTextCursor(cursor)
    
    def atualizar_status(self):
        """Atualizar barra de status"""
        total_cadastros = len(self.cadastros)
        hora_atual = datetime.now().strftime("%H:%M:%S")
        self.formulario.statusbar.showMessage(
            f"Total de cadastros: {total_cadastros} | Hora: {hora_atual}"
        )
    
    def mostrar_erro(self, mensagem):
        """Mostrar mensagem de erro"""
        QMessageBox.critical(self.formulario, "Erro", mensagem)
        self.log(f"ERRO: {mensagem}")
    
    def mostrar_sobre(self):
        """Mostrar informações sobre o sistema"""
        QMessageBox.about(self.formulario, "Sobre o Sistema",
                         "Sistema de Cadastro de Pessoas\n\n"
                         "Desenvolvido com PyQt5\n"
                         "Funcionalidades:\n"
                         "- Cadastro com validação\n"
                         "- Armazenamento em JSON\n"
                         "- Listagem de registros\n"
                         "- Log de atividades\n\n"
                         "© 2024")
    
    def sair(self):
        """Encerrar a aplicação"""
        resposta = QMessageBox.question(
            self.formulario, 
            "Confirmar Saída",
            "Deseja realmente sair?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if resposta == QMessageBox.Yes:
            self.log("Sistema encerrado")
            self.app.quit()
    
    def executar(self):
        """Executar a aplicação"""
        self.formulario.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    sistema = CadastroApp()
    sistema.executar()