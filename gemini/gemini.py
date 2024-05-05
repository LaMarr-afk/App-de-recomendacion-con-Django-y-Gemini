def modelo_ai(comentario):
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyAxGjaJAmogw6Gl841M6CtcO2XvtO7q02o")
    model =genai.GenerativeModel(model_name="gemini-pro")
    consulta= comentario
    response=model.generate_content(consulta)
    return(print(response.text))

