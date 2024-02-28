import pandas as pd

from sender import Sender



envio = Sender()

print("INICIO")

df = pd.read_excel('testes.xlsx')



df_test = df.copy()

df_test.drop(df_test.columns[0], axis=1, inplace=True)


body = """\
<html>
  <head></head>
  <body>
      <div style="text-align: center;">
          <p>Segue o quantitativo de processos da sua vara<br>
            <a href="https://desenvolvimento.trf5.jus.br/">Desenvolvimento Qlik</a><br>
            Envio de emails do Instant Red Alert.
          </p>

          <h1 style="text-align: center;">Relatório</h1>
          <div style="margin: 0 auto; width: fit-content;">
            {0}
          </div>
      </div>
      <div style="text-align: center; margin-top: 20px;">
          <img src="https://residenciaregional.jfrn.jus.br/wp-content/uploads/2022/03/Residencia_logo-C.png" alt="Logo Imagem 1" style="max-width: 200px; float: left;">
          <img src="https://residenciaregional.jfrn.jus.br/wp-content/uploads/2024/02/logo-trf5-300x191.png" alt="Logo Imagem 2" style="max-width: 200px; float: right;">
      </div>
  </body>
</html>
""".format(df_test.to_html(index=False, index_names=False))

envio.enviar_email(body)

print("Email enviado")