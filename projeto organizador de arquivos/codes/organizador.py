import shutil
from pathlib import Path

# 1. Nome do arquivo que você baixou
arquivo_zip = "organizador.zip" 
pasta_destino = Path("organizador")

# 2. Extrair se a pasta ainda não existir
if Path(arquivo_zip).exists():
    if not pasta_destino.exists():
        print(f"Extraindo {arquivo_zip}...")
        shutil.unpack_archive(arquivo_zip, extract_dir=pasta_destino)
        print("Extração concluída!")
else:
    print(f"Erro: O arquivo '{arquivo_zip}' não foi encontrado na pasta do script.")