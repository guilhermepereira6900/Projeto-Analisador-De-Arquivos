import shutil
from pathlib import Path
from datetime import datetime

# Definição do diretório alvo (onde os ficheiros estão)
# No meu caso, seria a pasta extraída do "organizador.zip"
diretorio_alvo = Path("organizador")
arquivo_log = Path("registro.log")

# Garantir que a pasta existe antes de começar
if not diretorio_alvo.exists():
    print(f"A pasta {diretorio_alvo} não foi encontrada. Por favor, extraia o zip primeiro.")
else:
    # Contadores para o resumo final
    contagem_arquivos = 0
    extensoes_vistas = set()

    print("🚀 A iniciar organização...")

    # Percorrer todos os itens na pasta
    for item in diretorio_alvo.iterdir():
        # Ignorar pastas já existentes, focar apenas em ficheiros
        if item.is_file():
            
            # Identificar a extensão (ex: .pdf, .png)
            # .suffix devolve a extensão com o ponto (ex: ".png")
            # .lower() garante que .PNG e .png sejam tratados como a mesma coisa
            extensao = item.suffix.lower().replace(".", "")
            
            # Caso o ficheiro não tenha extensão
            if not extensao:
                extensao = "outros"

            # Criar a subpasta da extensão (caso não exista)
            pasta_destino = diretorio_alvo / extensao
            pasta_destino.mkdir(exist_ok=True)

            # Mover o ficheiro para a nova pasta
            caminho_final = pasta_destino / item.name
            shutil.move(item, caminho_final)

            # Registrar a movimentação no log
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            linha_log = f"[{agora}] MOVIDO: {item.name} para {extensao}/\n"
            
            with open(arquivo_log, "a", encoding="utf-8") as log:
                log.write(linha_log)

            # Atualizar os dados do resumo
            contagem_arquivos += 1
            extensoes_vistas.add(extensao)

    # Exibir o Resumo Final
    print("\n" + "="*30)
    print("ORGANIZAÇÃO CONCLUÍDA!")
    print(f"Total de ficheiros movidos: {contagem_arquivos}")
    print(f"Extensões organizadas: {', '.join(extensoes_vistas)}")
    print(f"Verifique o histórico em: {arquivo_log}")
    print("="*30)