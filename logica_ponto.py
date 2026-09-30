funcionario_id = 1
funcionario_nome = "Juliana Silva"
funcionario_cargo = "Desenvolvedora"
funcionario_foto = "juliana.jpg"

historico_registros = [
    {"data": "23/10/2026", "horarios": "ENT: 08:03 | INT: 12:05 | RET: 13:00 | SAÍ: 17:08", "status": "Confirmado"},
    {"data": "24/10/2026", "horarios": "ENT: 08:03 | INT: 12:05 | RET: 13:00 | SAÍ: 17:08", "status": "Parcial"}
]

def tela1_reconhecimento():
    print("\n=== TELA 1: RECONHECIMENTO FACIAL / LOGIN ===")
    print("Horário Atual: 08:00 AM - Quarta-feira, 25 de Outubro")
    print("--------------------------------------------")
    
    id_digitado = int(input("Digite o ID para escanear o rosto e acessar o sistema: "))
    
    if id_digitado == funcionario_id:
        print("\n[STATUS FACIAL]: Rosto identificado com sucesso!")
        print(f"Bem-vindo(a), {funcionario_nome} ({funcionario_cargo})")
        return True
    else:
        print("\n[STATUS FACIAL]: [ERRO] Rosto/ID não encontrado! Acesso negado.")
        return False

def tela2_registrar_ponto():
    print("\n=== TELA 2: REGISTRAR PONTO ===")
    print(f"Colaborador Autenticado: {funcionario_nome}")
    print("--- Formulário de Marcação ---")
    
    tipo = input("Digite o tipo (Entrada, Intervalo, Retorno, Saida): ")
    data_hora = input("Digite a data e hora (ex: 25/10/2026 08:00): ")
    
    ponto_registrado = {
        "nome": funcionario_nome,
        "tipo": tipo,
        "horario": data_hora,
        "foto": funcionario_foto
    }
    
    novo_registro = {
        "data": data_hora,
        "horarios": f"Tipo: {tipo}",
        "status": "Confirmado"
    }
    historico_registros.append(novo_registro)
    
    print("\n--------------------------------------------")
    print("✓ STATUS: Ponto registrado com sucesso!")
    print(f"Colaborador: {ponto_registrado['nome']}")
    print(f"Marcação: {ponto_registrado['tipo']} às {ponto_registrado['horario']}")
    print("--------------------------------------------")

def tela3_historico():
    print("\n=== TELA 3: HISTÓRICO PESSOAL E RESUMO DO MÊS ===")
    print(f"Colaborador: {funcionario_nome} | Cargo: {funcionario_cargo}")
    print("--------------------------------------------")
    print("RESUMO DO MÊS:")
    print("- Total de Horas Trabalhadas: 160h / 168h")
    print("- Saldo Banco de Horas: +4h 30m (Extra)")
    print("- Atrasos no Mês: 1h 15m")
    print("--------------------------------------------")
    print("REGISTROS RECENTES:")
    for registro in historico_registros:
        print(f"• Data: {registro['data']} | {registro['horarios']} | Status: {registro['status']}")

def tela4_politicas():
    print("\n=== TELA 4: INFORMAÇÕES INSTITUCIONAIS E POLÍTICAS ===")
    print("AVISO GERAL: Manutenção Programada no Setor B (Data: 28/10)")
    print("--------------------------------------------")
    print("DESTAQUES DE POLÍTICAS DE RH (DOWNLOADS):")
    print("1. Codigo_de_Conduta_Atualizado.pdf")
    print("2. Plano_de_Saude_Novas_Regras.pdf")
    print("3. Seguranca_no_Trabalho.pdf")
    print("--------------------------------------------")
    print("HORÁRIOS DE TURNO PADRÃO:")
    print("Turno A: 06:00 - 14:00 (ENT | INT | 12:05)")
    print("Turno B: 14:00 - 22:00 (ENT | INT | 23:07 | SAÍ)")

def tela5_dashboard():
    print("\n=== TELA 5: DASHBOARD EM TEMPO REAL (GESTÃO) ===")
    print("+-----------------------------------+")
    print("| Presentes: 28  | Faltas: 3  | Atrasos: 5 |")
    print("+-----------------------------------+")
    print("\nVISTA RÁPIDA DA EQUIPE:")
    print("- João P.  -> Status: Em Ponto")
    print("- Maria C. -> Status: Falta")
    print("- Lucas R. -> Status: Atraso")

def tela6_gestao_faltas():
    print("\n=== TELA 6: GESTÃO DE FALTAS, ATRASOS E AJUSTES ===")
    print("1. Juliana Silva | 23 Out | Atraso de 15 min")
    print("2. Lucas R.       | 24 Out | Falta não justificada")
    print("--------------------------------------------")
    opcao = input("Deseja justificar alguma ocorrência? (S/N): ")
    if opcao.upper() == "S":
        numero = input("Digite o número da ocorrência (1 ou 2): ")
        motivo = input("Digite a justificativa: ")
        print(f"\n✓ Ocorrência {numero} ajustada com sucesso! Motivo: {motivo}")

def tela7_relatorios():
    print("\n=== TELA 7: RELATÓRIOS CONSOLIDADOS ===")
    print("Mês: Setembro | Horas Normais: 160h | Horas Extras: 15h | Total: 175h")
    print("Mês: Outubro  | Horas Normais: 160h | Horas Extras: 12h | Total: 172h")
    print("--------------------------------------------")
    exportar = input("Deseja exportar? (1-PDF / 2-CSV / 0-Cancelar): ")
    if exportar == "1":
        print("\n[OK] Arquivo 'relatorio_ponto.pdf' gerado!")
    elif exportar == "2":
        print("\n[OK] Arquivo 'relatorio_ponto.csv' gerado!")

def menu_principal():
    # Exige autenticação antes de abrir o menu do sistema
    autenticado = tela1_reconhecimento()
    
    if autenticado:
        loop = True
        while loop:
            print("\n====================================")
            print("          TIMELINK - SYSTEM         ")
            print("====================================")
            print("1. Reconhecimento Facial (Revalidar)")
            print("2. Registrar Ponto")
            print("3. Histórico e Resumo do Mês")
            print("4. Informações e Políticas")
            print("5. Dashboard em Tempo Real")
            print("6. Gestão de Faltas e Ajustes")
            print("7. Relatórios Consolidados")
            print("0. Sair do Sistema")
            
            opcao = input("\nEscolha a tela que deseja acessar (0 a 7): ")
            
            if opcao == "1":
                tela1_reconhecimento()
            elif opcao == "2":
                tela2_registrar_ponto()
            elif opcao == "3":
                tela3_historico()
            elif opcao == "4":
                tela4_politicas()
            elif opcao == "5":
                tela5_dashboard()
            elif opcao == "6":
                tela6_gestao_faltas()
            elif opcao == "7":
                tela7_relatorios()
            elif opcao == "0":
                print("\nEncerrando o sistema TimeLink... Até logo!")
                loop = False
            else:
                print("\n[ERRO] Opção Inválida! Tente um número de 0 a 7.")

menu_principal()