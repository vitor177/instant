import pandas as pd

from sender import Sender



envio = Sender()


df = pd.read_excel('cd411b79-19a8-47bd-a7d7-bf6c13328af0.xlsx')

df_test = df.head()


body = """\
<html>
  <head></head>
  <body>
   <p>Olá,<br>
        Tudo bem? Segue o quantitativo de processos da sua vara<br>
        <a href="https://desenvolvimento.trf5.jus.br/">Desenvolvimento Qlik</a> 
        <br>
        Envio de emails do Instant Red Alert -.
        </p>
    {0}
  </body>
</html>
""".format(df_test.to_html())

envio.enviar_email(body)