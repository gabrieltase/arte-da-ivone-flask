import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

# Lê o arquivo .env (Cap. 9.8) e disponibiliza as variáveis em os.getenv
load_dotenv()

app = Flask(__name__)

# A secret_key é obrigatória para usar flash() (Cap. 8.3).
# Em produção, defina SECRET_KEY no .env; o valor abaixo serve só para testes.
app.secret_key = os.getenv("SECRET_KEY", "chave-de-desenvolvimento-troque-no-env")

# Dados do catálogo: o template percorre esta lista com {% for %} (Cap. 6.4)
PRODUTOS = [
    {"nome": "Necessaire", "imagem": "img/necessaire.png"},
    {"nome": "Estojo", "imagem": "img/estojo.png"},
    {"nome": "Bolsas", "imagem": "img/foto_bolsa.png"},
    {"nome": "Porta Óculos", "imagem": "img/porta_oculos3.png"},
    {"nome": "Porta Cartão", "imagem": "img/porta_cartao.png"},
    {"nome": "Porta Celular", "imagem": "img/foto_porta_celular.png"},
    {"nome": "Carteiras", "imagem": "img/carteira.png"},
    {"nome": "Pano de Prato e Bate Mão", "imagem": "img/pano_de_prato_e_bate_mao.png"},
    {"nome": "Kits para Cozinha", "imagem": "img/foto_ki_cozinha.png"},
    {"nome": "Kits de Necessaire", "imagem": "img/foto_kit_necessaire.png"},
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=PRODUTOS)


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        # .get() evita o erro 400 se algum campo faltar (Cap. 9.5)
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        mensagem = request.form.get("mensagem", "").strip()

        if not (nome and email and mensagem):
            flash("Preencha nome, e-mail e mensagem.", "danger")
        else:
            flash(f"Obrigada, {nome}! Sua mensagem foi enviada com sucesso.", "success")

        # Post/Redirect/Get: evita reenvio do formulário ao apertar F5 (Cap. 9.5)
        return redirect(url_for("contato"))

    return render_template("contato.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)