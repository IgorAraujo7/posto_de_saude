from main import app


@app.post("/cadastro")
async def cadastro_de_usuario():
    return "Bem vindos ao Posto de saúde"