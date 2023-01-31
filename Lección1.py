######################
# Instrucciones de terminal
######################

#streamlit run app.py para iniciar la app
#Control+C para terminar desde el terminal
#Actualizar al ejecutar el programa: ≡ -> Settings -> Run on save

######################
# Import libraries
######################

import streamlit as st

# ######################
# Configuración de página
# ######################

st.set_page_config(
    page_title="Lecciones",
    page_icon="https://pti-teledetect.csic.es/wp-content/uploads/2021/12/logointa.png",
    layout="wide", #"wide" or "centered"
    initial_sidebar_state="expanded", #"auto" or "expanded" or "collapsed"
    menu_items={
        'Get Help': "https://www.tecnolivo.eu/wp-content/uploads/2018/01/Inta_logo.jpg",
        'Report a bug': "https://www.tecnolivo.eu/wp-content/uploads/2018/01/Inta_logo.jpg",
        'About': "# This is a header. This is experimento an *extremely* cool app!"
    }
)

"El nombre de la app y su logo están configurados al principio"
"Además, se ha modificado Get Help, Report a Bug y About del menú ≡"
"Si Get Help o Report a Bug no se incluye, no aparece en el menú"
"Con About, en cambio, sale el mensaje por defecto"


######################
# Menu
######################

st.sidebar.header('Ménu') #subtitulo
st.sidebar.write('texto del ménu')
sequence = st.sidebar.text_area("textbox ménu", "texto del textbox \n Se le puede añadir deslizador, subtitulo...", height=25)
st.sidebar.selectbox('selectbox ménu', ('opción 1', 'opción 2', 'opción 3'), 1)

"Aqui se modifica el menú lateral"


######################
# Page Title
######################

st.write("""
# Título 1: Presentación 📖
## Subtitulo 1.1: subtitulos
### subsubtitulo 1.1.1
#### subsubsubtitulo 1.1.1.1
##### subsubsubtitulo 1.1.1.1.1
###### subsubsubsubtitulo 1.1.1.1.1.1
## Subtitulo 1.2: formatos de texto

Texto *texo_cursiva* _texto-cursiva2_ \n
 **texto_negrita** __texto-negrita2__ \n
 :red[texto rojo]\n
 :green[$\sqrt{x^2+y^2}=1$]
""") 

st.latex(r"\int_a^b \lim_{x \rightarrow 2} x^2") 
"existe una orden para usar latex"

st.header('subtitulo 1.3: tipos de título')
"titulo se puede añadir con un [# *str*] al principio, con [st.title(*str*)] o con [st.markshadow(*str*)]"
"Todas las opciones admiten emojis 📖 :book:"
"con más # bajamos un bivel el titulo"

st.subheader('subsubtitulo 1.3.2: tipos de textos')
st.write("otra forma de poner texto")
"también puedes ponerlo solo. Se conoce como _Magic_"
st.text("y en otros formatos")
st.caption("como caption, una letra pequeña para pies de pagina y explicaciones")
st.code("o codigo, como: a = 1234 \n incluso funciones, vease def a(): \n#Puedes elegir el lenguaje con la varible language=")
st.write(f"También puedes usar f() {int(2.3)} como con la barra de carga para hacer strings dinamicos")
"Además se puede cambiar fuente y tamaño, pero no lo he mirado"
"[st.write(·)] es como un print, puedes ponerle números, o comas para combinar"

st.subheader('subsubtitulo 1.3.3: markdown')

"Generalmente el texto, con write y de forma magica, cumple las leyes de GitHub Flavored Markdown"
"Markdown tiene su propia entrada en la Wikipedia"

"Markdown permite _italica_, **negrita** y `monospace`"

"Si queremos una raya horizontal solo es necesario tres guiones"
"---"

"Podemos hacer listas, y numeracion"
st.markdown(
"""
The following list won't indent no matter what I try:
- Item 1
- Item 2
- Item 3 \n
    -apple \n
    -banana
"""
)

"La sangría funciona de forma distinta según el caso"

st.markdown(
"""
hola \n
 hola \n
    hola
hola
"""
)
"---"
"También podemos crear links varios a scripts o webs: [1.leccion2, 2.no funciona- itm.jpg, 3.web]"
"[nombreinventado1](Lección2)"
"[nombreinventado2](itm)"
"[nombreinventado3](https://www.aeh2.org/wp-content/uploads/2021/01/inta-logo.png)"

st.header('Subtitulo 1.4: mensajes')
st.success("Perfecto!")
st.info("Información!")
st.warning("warning")
st.error("Error")
st.exception("NameError('no está definido')")

# ######################
# Deslizador
# ######################
st.title("Título 2: Deslizador")

window = st.slider("Etiqueta Deslizador",value = 25)

st.write("el valor del deslizador es:  " + str(window))
st.write(f"Con f(), el valor del deslizador es:  {window} ")

window3 = st.select_slider("Etiqueta Deslizador Select",options = ['a','b','c','d','e','f','e'], value='b')
st.write("el valor del deslizador Select es:  " + str(window3))

window4 = st.select_slider("Etiqueta Deslizador Select Rango",options = ['a','b','c','d','e','f','e'], value=('b','e'))
st.write("los valores del deslizador Select son:  " + str(window4))

# ######################
# Text Box
# ######################

st.title("Título 3: Textbox")
window2 = st.slider("Tamaño del textbox por defecto",value = 25, max_value = 250)
sequence = st.text_area("Etiqueta Textbox", "texto del textbox", height=window2, help="tooltip", max_chars=window2)
st.text_area("Etiqueta Textbox", "texto del textbox", key = "textbox2", height=25, disabled=True)

"Se puede obtener informacion sobre estas variables:"
st.write(window2)
st.write(sequence)

"Además se puede decidir si es la etiqueta visible o no con la variable label_visibility"
"Y evitar que se escribe con la variable disabled"
"Y crear tooltip con la variable help"
"Y fijar el maximo de caracteres con la variable max_chars"
""
"Si label da problemas, hay una variable key adicional"

"## Sección 3.1: Input text"
st.text_input("a","b")


# ######################
# Check Box
# ######################

st.title("Título 4: Checkbox")
boton = st.checkbox('Casilla')
if boton:
    "La casilla está marcada"

# ######################
# Gráficas
# ######################

st.title("Título 5: Gráficas")
st.bar_chart([[1,1,1],[2,2,2],[3,3,3]])
st.bar_chart({"alfa": [1,2,3], "beta": [1,2,3], "gamma": [1,2,3]})

"Para personalizar más es necesario el paquete pandas."

"Hay otras muchas funciones que hacen graficos, pero todas necesitan de pandas, o de numpy, o de matplotlib.pyplot (supuestamente)"
"Vienen detalladas en la sección _Chart elements_ de"
"https://docs.streamlit.io/library/api-reference?highlight=expander#streamlit.beta_expander"
""

"st.bokeh_chart crea una grafica XY solo con el paquete bokeh.plotting"

"## Sección 4.1: Grafos"

"El paquete graphviz crea grafos que se pueden adjuntar a la app"
"dirigidos, no dirigidos, con colores, cdistintas formas para nodos"
"Usando el mismo lenguaje, podemos crear grafos sin añadir paquetes usando **st.graphviz_chart(·)** "

st.graphviz_chart('''
    digraph {
        roca -> roca
        tierra -> tierra 
        fuego -> hielo 
        hielo -> planta
        planta -> roca
        tierra -> roca
        roca -> fuego
        fuego -> planta
        hielo -> roca
        planta -> tierra
        tierra -> fuego
        roca -> hielo
    }
''') #el digraph no es obligatorio



# ######################
# Select box
# ######################

st.title("Título 6: Select Box")
option = st.selectbox(
    'Etiqueta selectbox',
     ["opción 1","opción 2 - elegida por defecto","opción 3"],1)

"Elegiste: " + option

# ######################
# Button box
# ######################

st.title("Título 7 : Button Box")
boton1 = st.button('Añade', type = "primary")
boton2 = st.button('Elimina') #por defecto: type = "secondary"

if 'texto_boton' not in st.session_state:
    st.session_state['texto_boton'] = 'hola'

if 'texto_boton' in st.session_state:
    if boton1:
        st.session_state['texto_boton'] += "hola"

    if boton2:
        st.session_state['texto_boton'] = "hola" 

    texto_boton = st.session_state['texto_boton']
    texto_boton

st.header("Título 7.1. Session State")
"[st.session.state[·]] funciona como un diccionario para guardar variables"
"Gracias a esto la app recuerda como va la cadena hola"
"Si solo usaramos una variable en python, habría que definirla primero,"
"perdiendo el nuevo valor por el de inicializacion cada vez que se pulsa el boton"
"por que el botón reinicia el script (excepto con los box)"
""
"para borrar una variable usamos :blue[del] st.session_state[key]" 
"para eliminarlas todas usamos un bucle for y la instruccion anterior"
""
"Clear Cache elimina todas las variables también"
"Settings -> Clear Cache (C)"
""
"La variable se guarda con multipagina"
""
"para más inormación"
"https://docs.streamlit.io/library/api-reference/session-state"

# ######################
# Radio box
# ######################

st.title("Título 8 : Radio Box")
chosen = st.radio(
        'Etiqueta radio',
        ("opción 1", "opción 2", "opción 3"),
        1)
st.write(f"Marcaste {chosen} en el radio box.")

# ######################
# Multiselect box
# ######################
st.header("Sección 8.1 : Multiselect Box")
location = st.multiselect(
    "Donde trabajas?",
    ("Londres", "Nueva York", "Accra", "Kiev", "Nepal", "Buenos Aires", "Caracas"),
)
st.write("Seleccionó:", len(location), "locaciones:", location)


# ######################
# Columnas
# ######################

st.title("Título 9 : Columnas")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Botón')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen2 = st.radio('Radio Box2', ("Opción 1", "Opción 2", "Opción 3"))
    st.write(f"Marcaste {chosen2} en el radio box.")

"Aviso: st.spinner() y st.echo(), de los títulos 10 y 11, no funcionan con columnas."

# ######################
# Carga
# ######################

st.title("Título 10 : Carga")
boton3 = st.button('Empezar')
if not boton3:
    "Esperando a empezar."
else:
    with st.spinner("Esperando por ello..."):
        for i in range(100000000):
            i += 1
    st.success("Hecho")

# ######################
# Imprimir código como código
# ######################

st.title("Título 11 : Imprimir código")
with st.echo("above"):
    st.write("Este codigo sera impreso!")

"Esto imprime el propio codigo, a diferencia del st.code(·) explicado en el Título 1.3.2"

# ######################
# Barra de progreso
# ######################

st.title("Título 12 : Barra de progreso")

"Los valores de la barra siempre deben estar entre 0 y 100, pero no los de la etiqueta"

'Empezamos una computación larga...'

boton4 = st.button('Empezar2')
if not boton4:
    "___Esperando a empezar."
else:

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(200):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Vamos por la iteración {i+1}')
        bar.progress((i+1)//2) #bar_progress debe empezar con 0 y terminar en 100
        for i in range(1000000):
            i += 1

    latest_iteration.text(f'FIN')

    '...y la terminamos!'

# ######################
# Distintas páginas
# ######################

st.title("Título 13 : Varias páginas web.")

"Se ejecutaran como subpaginas los scripts (.py) dentro de una carpeta llamada *pages*"
"El nombre de la carpeta es obligatorio"
"El nombre de las carpetas es el mismo de los scripts por defecto"
""

"Al ejecutar una pagina u otra el menú asociado también cambia \n"
""

"https://docs.streamlit.io/library/get-started/multipage-apps explica un poco más," 
"como algún comando para ordenar las paginas, o que muestren un emoji en el menú."

# ######################
# Más Utilidades
# ######################

st.title("Título 14: Más Utilidades")

"Todas las utilidades:"
"https://docs.streamlit.io/library/api-reference?highlight=expander#streamlit.beta_expander"
""
"Excel:"
"https://docs.streamlit.io/knowledge-base/tutorials/databases/public-gsheet"
""
"Publicar/Descargar App:"
"https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app"

