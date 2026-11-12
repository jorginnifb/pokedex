from flask import flask 

app = flask(__name__)

#rotas serao inseridas aqui 
@app.route('/')
def inicio():
    url_api ="https://pokeapi.co/api/v2/pokemon-form/25"
    response = response.jason()
    dados = response.jason
    print(dados.get("name"))

if __name__ == '__main__':

    app.run(debug=true)