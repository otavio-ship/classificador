from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def analisar_numero():
    if request.method == 'POST':
        try:
            numero = int(request.form['numero'])

            # Verifica par/ímpar
            par_impar = "par" if numero % 2 == 0 else "ímpar"

            # Verifica positivo/negativo/zero
            if numero > 0:
                pos_neg = "positivo"
            elif numero < 0:
                pos_neg = "negativo"
            else:
                pos_neg = "zero"

            return render_template('analise.html',
                                   numero=numero,
                                   par_impar=par_impar,
                                   pos_neg=pos_neg)

        except ValueError:
            return render_template('analise.html', erro="Por favor, digite um número inteiro válido!")

    return render_template('analise.html')


if __name__ == '__main__':
    app.run(debug=True)