from sender import Sender
import base64

# Crie uma instância do Sender
envio = Sender()

# Caminho para a imagem
image_path = "blue-JPG-file-icon.jpg"

# Abra a imagem em modo binário e leia o conteúdo
with open(image_path, "rb") as img_file:
    image_data = img_file.read()

# Codifique a imagem em base64
image_base64 = base64.b64encode(image_data).decode()

# Crie a string HTML com a imagem codificada em base64
html = f"""
<html>
  <head></head>
    <body>
      <p><h4 style="font-size:15px;">Some Text.</h4></p>   
      <img src="data:image/jpeg;base64,{image_base64}" alt="Logo" style="width:250px;height:50px;">
    </body>
</html>
"""

# Envie o e-mail com a string HTML que contém a imagem
envio.enviar_email(html)
