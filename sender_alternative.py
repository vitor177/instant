import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from datetime import date
import pandas as pd

data = date.today()
data = data.strftime('%d/%m/%Y')

strFrom = "instantredalert@gmail.com"
strTo = "joovitor177@gmail.com"
password = 'ymmh doef rovb ntvk'

# Create the root message
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'Multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)

# Read and prepare the table
dtype_map = {'Sigla': str, 'Entre 1 ano e 2': int, 'Maior que 2 anos': int, 'Menor que 1 ano': int}
tabela_ordenada = pd.read_csv('prescricao_resumo.csv', dtype=dtype_map, index_col=False)
tabela_ordenada.index += 1

conteudo_tabela = tabela_ordenada.to_html()
cleaned_html = conteudo_tabela.replace('border="1"', '').replace('class="dataframe"', '')
styled_html = cleaned_html.replace('<table>', '<table style="border-collapse: collapse; width: 100%;">').replace('<tr>', '<tr style="background-color: #f2f2f2;">')
html_modificado = styled_html.replace('text-align: right;', 'text-align: center;')

variable = f"""
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório Mensal de Prescrição e Improbidade Administrativa</title>
    <style>
        body {{
            font-family: "Verdana", "sans-serif";
        }}

        .titulo {{
            font-size: 1.5em;
            font-weight: bold;
            text-align: center;
            background-color: #ADADAD;
            padding: 0.5em 0 0.5em 0.5em;
            position: relative;
            margin-bottom: 0;
        }}

        .subtitulo {{
            font-size: 0.8em;
            text-align: center;
            background-color: #E8E8E8;
            padding: 0.5em 0 0.5em 0.5em;
            margin-top: 0;
            position: relative;
            top: 0;
        }}

        .tabela_de_imagens {{
            align-items: center;
            margin: 2em auto;
            display: table;
            border-spacing: 0;
        }}

        .footer {{
            text-align: center;
            background-color: #ADADAD;
            width: 100%;
            padding: 1em 0;
            margin-top: 1em;
        }}

        .grafico {{
            width: 100%;
            max-width: 400px;
            padding: 0;
            margin: 0;
            display: block;
        }}

        table {{
            margin: auto;
        }}

        th {{
            font-weight: bold;
        }}

        th, td {{
            padding: 8px;
            white-space: nowrap;
        }}

        td {{
            padding: 10px;
            text-align: center;
            width: 120px;
            font-weight: none;
            word-wrap: break-word;
        }}

        tr:nth-child(even) {{
            background-color: #E8E8E8;
        }}

        tr:hover:nth-child(1n + 2) {{
            background-color: #6b6a6a;
            color: #fff;
        }}

        @media (max-width: 600px) {{
            .grafico {{
                width: 100%;
                max-width: 200px;
            }}
            .titulo {{
                font-size: 1.2em;
            }}
            .subtitulo {{
                font-size: 0.7em;
            }}
        }}
    </style>
</head>

<body>
    <div>
        <p class="titulo">Relatório Mensal Prescrição em Improbidade Administrativa e Geral</p>
        <p class="subtitulo">Data de extração: <strong>{data}</strong></p>

        <table class="tabela_de_imagens">
            <tr>
                <td>
                    <img class="grafico" src="cid:image0" style="width: 250px; height: 250px;" />
                </td>
                <td>
                    <img class="grafico" src="cid:image1" style="width: 250px; height: 250px;" />
                </td>
                <td>
                    <img class="grafico" src="cid:image2" style="width: 250px; height: 250px;" />
                </td>
            </tr>
            <tr>
                <td>
                    <img class="grafico" src="cid:image3" style="width: 250px; height: 250px;" />
                </td>
                <td>
                    <img class="grafico" src="cid:image4" style="width: 250px; height: 250px;" />
                </td>
                <td>
                    <img class="grafico" src="cid:image5" style="width: 250px; height: 250px;" />
                </td>
            </tr>
        </table>
    </div>
    <div>
        <p class="secao">
        </p>
        """ + html_modificado + """
    </div>

    <div class="footer">
        <strong>Para mais informações acesse o Instant:</strong><br>
        <a href="https://instant.trf5.jus.br/inspecao-web/#/login">
            https://instant.trf5.jus.br/inspecao-web/#/login
        </a>
    </div>

    <div class="nota_email">
        ------------------------------------------------------------------------<br>
        Envio de e-mails automático do Red Alert <br>
        TRF5 - Tribunal Regional Federal da 5ª Região
    </div>
</body>

"""



msgText = MIMEText(variable, 'html')
msgAlternative.attach(msgText)

file_names = ['chart0.png', 'chart1.png', 'chart2.png', 'chart3.png', 'chart4.png', 'chart5.png']

# Loop para adicionar as imagens ao email
for idx, file_name in enumerate(file_names, start=0):
    # Abrindo o arquivo da imagem em modo binário
    with open(f'./graficos/{file_name}', 'rb') as fp:
        # Lendo o conteúdo da imagem
        img_data = fp.read()
        
        # Criando o objeto MIMEImage com os dados da imagem
        msgImage = MIMEImage(img_data)
        
        # Definindo o Content-ID da imagem
        msgImage.add_header('Content-ID', f'<image{idx}>')
        
        # Anexando a imagem ao email
        msgRoot.attach(msgImage)

# Conexão
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(strFrom, password)
    server.sendmail(
        strFrom, strTo, msgRoot.as_string()
    )
    print("Enviado")
