from flask import Flask, render_template

app = Flask(__name__)

# Lista de produtos do catálogo (arquivo dentro de static/img)
PRODUTOS = [
    {"titulo": "Necessaire", "img": "necessaire.png",
     "desc": "Prática para organizar seus itens do dia a dia."},
    {"titulo": "Estojo", "img": "estojo.png",
     "desc": "Para guardar canetas, lápis e pequenos objetos."},
    {"titulo": "Bolsas", "img": "foto_bolsa.png",
     "desc": "Peças feitas à mão, cada uma com seu charme."},
    {"titulo": "Porta Óculos", "img": "porta_oculos3.png",
     "desc": "Protege seus óculos com delicadeza."},
    {"titulo": "Porta Cartão", "img": "porta_cartao.png",
     "desc": "Pequeno, útil e fácil de levar na bolsa."},
    {"titulo": "Porta Celular", "img": "foto_porta_celular.png",
     "desc": "Seu celular sempre à mão e protegido."},
    {"titulo": "Carteiras", "img": "carteira.png",
     "desc": "Carteiras artesanais para o dia a dia."},
    {"titulo": "Pano de Prato e Bate Mão", "img": "pano_de_prato_e_bate_mao.png",
     "desc": "Bordados à mão para deixar a cozinha mais bonita."},
    {"titulo": "Kits para Cozinha", "img": "foto_ki_cozinha.png",
     "desc": "Conjuntos para presentear ou renovar a cozinha."},
    {"titulo": "Kits de Necessaire", "img": "foto_kit_necessaire.png",
     "desc": "Conjuntos de necessaires combinando."},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=PRODUTOS)


@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    # host 0.0.0.0 aceita conexões externas (necessário na EC2); porta 5000 liberada no Security Group
    app.run(host="0.0.0.0", port=5000, debug=False)
