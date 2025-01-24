'''python -m venv venv (создается папка venv в которой будут установлены все зависимости)
venv\Scripts\activate (активирует venv)
pip install virtualnoeOkrugenie       (устанавливает библиотеку virtualnoeOkrugenie) если нужна
pip freeze (список зависимостей)
pip install -r requirements.txt (устанавливает зависимости из requirements.txt)
pip  install requests (устанавливает библиотеку requests)

import requests
def main():
    return requests.get(url="https://google.com")
    if __name__ == "__main__":
        print(main())
pip freeze (список зависимостей)       
pip freeze > requirements.txt (создает requirements.txt с зависимостями)       



'''