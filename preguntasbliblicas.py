import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="📖 Generador de Preguntas Bíblicas", page_icon="✝", layout="wide")


st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 1rem;
    }
    .question-card {
        background-color: #f8fff8;
        padding: 2rem;
        border-radius: 15px;
        border-left: 6px solid #2E8B57;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .bible-verse {
        background-color: #FFF8DC;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #DAA520;
        font-style: italic;
        margin: 1rem 0;
    }
    .score-card {
        background: linear-gradient(135deg, #2E8B57, #3CB371);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)
PREGUNTAS_BIBLICAS = [
    
    {
        "pregunta": "¿Quién construyó el arca?",
        "opciones": ["Noé", "Moisés", "Abraham", "David"],
        "respuesta": "Noé",
        "dificultad": "Fácil",
        "categoria": "Antiguo Testamento",
        "referencia": "Génesis 6:14",
        "explicacion": "Dios le ordenó a Noé construir un arca para salvar a su familia y a los animales del diluvio."
    },
    {
        "pregunta": "¿Quién fue vendido por sus hermanos?",
        "opciones": ["José", "Benjamín", "Judá", "Rubén"],
        "respuesta": "José",
        "dificultad": "Fácil",
        "categoria": "Antiguo Testamento",
        "referencia": "Génesis 37:28",
        "explicacion": "Los hermanos de José lo vendieron por 20 piezas de plata a unos mercaderes."
    },
    {
        "pregunta": "¿Quién derrotó al gigante Goliat?",
        "opciones": ["David", "Saúl", "Jonatán", "Sansón"],
        "respuesta": "David",
        "dificultad": "Fácil",
        "categoria": "Antiguo Testamento",
        "referencia": "1 Samuel 17:50",
        "explicacion": "David derrotó a Goliat con una honda y una piedra."
    },
     {
        "pregunta": "¿Quién traicionó a Jesús?",
        "opciones": ["Judas Iscariote", "Pedro", "Tomás", "Juan"],
        "respuesta": "Judas Iscariote",
        "dificultad": "Fácil",
        "categoria": "Nuevo Testamento",
        "referencia": "Mateo 26:14-16",
        "explicacion": "Judas Iscariote traicionó a Jesús por 30 piezas de plata."
    },
    {
        "pregunta": "¿Dónde nació Jesús?",
        "opciones": ["Belén", "Nazaret", "Jerusalén", "Jericó"],
        "respuesta": "Belén",
        "dificultad": "Fácil",
        "categoria": "Nuevo Testamento",
        "referencia": "Mateo 2:1",
        "explicacion": "Jesús nació en Belén de Judea, cumpliendo la profecía de Miqueas 5:2."
    },
    {
        "pregunta": "¿Quién negó a Jesús tres veces?",
        "opciones": ["Pedro", "Juan", "Andrés", "Felipe"],
        "respuesta": "Pedro",
        "dificultad": "Fácil",
        "categoria": "Nuevo Testamento",
        "referencia": "Mateo 26:69-75",
        "explicacion": "Pedro negó conocer a Jesús tres veces antes de que cantara el gallo."
    },
     {
        "pregunta": "¿Qué pidió Salomón a Dios cuando se le apareció en sueños?",
        "opciones": ["Sabiduría", "Riquezas", "Larga vida", "Victoria en batalla"],
        "respuesta": "Sabiduría",
        "dificultad": "Intermedia",
        "categoria": "Antiguo Testamento",
        "referencia": "1 Reyes 3:9",
        "explicacion": "Salomón pidió un corazón entendido para gobernar al pueblo de Dios."
    },
    {
        "pregunta": "¿Quién interpretó los sueños del faraón en Egipto?",
        "opciones": ["José", "Daniel", "Moisés", "Jeremías"],
        "respuesta": "José",
        "dificultad": "Intermedia",
        "categoria": "Antiguo Testamento",
        "referencia": "Génesis 41:25-32",
        "explicacion": "José interpretó que habría 7 años de abundancia seguidos de 7 años de hambre."
    },
    {
        "pregunta": "¿Cuál fue el primer milagro de Jesús?",
        "opciones": ["Convertir agua en vino", "Sanar a un ciego", "Multiplicar panes", "Caminar sobre el agua"],
        "respuesta": "Convertir agua en vino",
        "dificultad": "Intermedia",
        "categoria": "Nuevo Testamento",
        "referencia": "Juan 2:1-11",
        "explicacion": "Jesús convirtió agua en vino en las bodas de Caná."
    },
    {
        "pregunta": "¿Quién fue el apóstol de los gentiles?",
        "opciones": ["Pablo", "Pedro", "Juan", "Santiago"],
        "respuesta": "Pablo",
        "dificultad": "Intermedia",
        "categoria": "Nuevo Testamento",
        "referencia": "Hechos 9:15",
        "explicacion": "Dios escogió a Pablo para llevar su nombre ante los gentiles."
    },
     {
        "pregunta": "¿Cuántos años vivió Matusalén?",
        "opciones": ["969 años", "777 años", "950 años", "930 años"],
        "respuesta": "969 años",
        "dificultad": "Difícil",
        "categoria": "Antiguo Testamento",
        "referencia": "Génesis 5:27",
        "explicacion": "Matusalén es la persona que más años vivió según la Biblia."
    },
    {
        "pregunta": "¿Qué rey encontró el libro de la ley en el templo?",
        "opciones": ["Josías", "Ezequías", "Joás", "Manasés"],
        "respuesta": "Josías",
        "dificultad": "Difícil",
        "categoria": "Antiguo Testamento",
        "referencia": "2 Reyes 22:8",
        "explicacion": "Durante las reparaciones del templo, el sumo sacerdote Hilcías encontró el libro de la ley."
    },
    {
        "pregunta": "¿Cuántos panes y peces usó Jesús para alimentar a los 5000?",
        "opciones": ["5 panes y 2 peces", "7 panes y 3 peces", "5 panes y 5 peces", "3 panes y 2 peces"],
        "respuesta": "5 panes y 2 peces",
        "dificultad": "Difícil",
        "categoria": "Nuevo Testamento",
        "referencia": "Mateo 14:17-19",
        "explicacion": "Con solo 5 panes y 2 peces, Jesús alimentó a una multitud de 5000 hombres, sin contar mujeres y niños."
    },
    {
        "pregunta": "¿Quién fue restaurado la vista cuando Ananías oró por él?",
        "opciones": ["Pablo", "Pedro", "Bernabé", "Esteban"],
        "respuesta": "Pablo",
        "dificultad": "Difícil",
        "categoria": "Nuevo Testamento",
        "referencia": "Hechos 9:17-18",
        "explicacion": "Después de su encuentro con Jesús en el camino a Damasco, Pablo quedó ciego y fue sanado por Ananías."
    }
]
if 'puntuacion' not in st.session_state:
    st.session_state.puntuacion = 0
if 'preguntas_respondidas' not in st.session_state:
    st.session_state.preguntas_respondidas = 0
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = None
if 'mostrar_respuesta' not in st.session_state:
    st.session_state.mostrar_respuesta = False
if 'respuesta_usuario' not in st.session_state:
    st.session_state.respuesta_usuario = None
if 'historial' not in st.session_state:
    st.session_state.historial = []

def obtener_pregunta_filtrada(dificultad, categoria):
    """Obtiene una pregunta aleatoria según los filtros"""
    preguntas_filtradas = [p for p in PREGUNTAS_BIBLICAS 
                          if p['dificultad'] == dificultad and p['categoria'] == categoria]
    
    if not preguntas_filtradas:
         preguntas_filtradas = PREGUNTAS_BIBLICAS
    
    return random.choice(preguntas_filtradas) if preguntas_filtradas else None

def reiniciar_quiz():
    """Reinicia el quiz"""
    st.session_state.puntuacion = 0
    st.session_state.preguntas_respondidas = 0
    st.session_state.historial = []
    st.session_state.mostrar_respuesta = False
    st.session_state.respuesta_usuario = None
st.markdown('<h1 class="main-header"> Generador de Preguntas Bíblicas</h1>', unsafe_allow_html=True)
st.markdown("### Pon a prueba tu conocimiento de las Escrituras")

with st.sidebar:
    st.header("⚙ Configuración del Quiz")
    
    dificultad = st.selectbox(
        "Nivel de dificultad:",
        ["Todas", "Fácil", "Intermedia", "Difícil"]
    )
    
    categoria = st.selectbox(
        "Categoría:",
        ["Todas", "Antiguo Testamento", "Nuevo Testamento"]
    )
    
    st.markdown("---")
    st.header(" Tu Progreso")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Puntuación", st.session_state.puntuacion)
    with col2:
        st.metric("Preguntas", st.session_state.preguntas_respondidas)
    
    if st.session_state.preguntas_respondidas > 0:
        porcentaje = (st.session_state.puntuacion / st.session_state.preguntas_respondidas) * 100
        st.metric("Porcentaje", f"{porcentaje:.1f}%")
    
    st.markdown("---")
    
    if st.button(" Reiniciar Quiz", type="primary"):
        reiniciar_quiz()
        st.rerun()

    col_left, col_right = st.columns([3, 1])

with col_left:
    
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button(" Nueva Pregunta", use_container_width=True):
            # Aplicar filtros
            dif_filtro = dificultad if dificultad != "Todas" else None
            cat_filtro = categoria if categoria != "Todas" else None
            
            if dif_filtro and cat_filtro:
                st.session_state.pregunta_actual = obtener_pregunta_filtrada(dif_filtro, cat_filtro)
            elif dif_filtro:
                preguntas_filtradas = [p for p in PREGUNTAS_BIBLICAS if p['dificultad'] == dif_filtro]
                st.session_state.pregunta_actual = random.choice(preguntas_filtradas) if preguntas_filtradas else None
            elif cat_filtro:
                preguntas_filtradas = [p for p in PREGUNTAS_BIBLICAS if p['categoria'] == cat_filtro]
                st.session_state.pregunta_actual = random.choice(preguntas_filtradas) if preguntas_filtradas else None
            else:
                st.session_state.pregunta_actual = random.choice(PREGUNTAS_BIBLICAS)
            
            st.session_state.mostrar_respuesta = False
            st.session_state.respuesta_usuario = None
    
    with col_btn2:
        if st.session_state.pregunta_actual and not st.session_state.mostrar_respuesta:
            if st.button(" Mostrar Respuesta", use_container_width=True):
                st.session_state.mostrar_respuesta = True

   
    if st.session_state.pregunta_actual:
        pregunta = st.session_state.pregunta_actual

        st.markdown(f'<div class="question-card">', unsafe_allow_html=True)
        
        col_info1, col_info2 = st.columns(2)
        with col_info1:
            st.write(f"*Dificultad:*  {pregunta['dificultad']}")
        with col_info2:
            st.write(f"*Categoría:*  {pregunta['categoria']}")
        
        st.markdown(f"###  {pregunta['pregunta']}")
        
      
        if not st.session_state.mostrar_respuesta:
            respuesta_seleccionada = st.radio(
                "Selecciona tu respuesta:",
                pregunta['opciones'],
                key="opciones_respuesta"
            )
            
            if st.button(" Enviar Respuesta", type="primary"):
                st.session_state.respuesta_usuario = respuesta_seleccionada
                st.session_state.mostrar_respuesta = True
                st.session_state.preguntas_respondidas += 1
                
                
                if respuesta_seleccionada == pregunta['respuesta']:
                    st.session_state.puntuacion += 1
                
                
                st.session_state.historial.append({
                    'pregunta': pregunta['pregunta'],
                    'respuesta_usuario': respuesta_seleccionada,
                    'respuesta_correcta': pregunta['respuesta'],
                    'correcta': respuesta_seleccionada == pregunta['respuesta'],
                    'timestamp': datetime.now().strftime("%H:%M:%S")
                })
        
        if st.session_state.mostrar_respuesta:
            st.markdown("---")

            st.markdown(f'<div class="bible-verse">', unsafe_allow_html=True)
            st.write(f" Referencia:** {pregunta['referencia']}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            
            if st.session_state.respuesta_usuario:
                if st.session_state.respuesta_usuario == pregunta['respuesta']:
                    st.success(f" *Correcto!* La respuesta es: {pregunta['respuesta']}")
                else:
                    st.error(f" *Incorrecto.* Tu respuesta: {st.session_state.respuesta_usuario}. La respuesta correcta es: {pregunta['respuesta']}")
            else:
                st.info(f" *Respuesta:* {pregunta['respuesta']}")
            
           
            st.write(f" Explicación:** {pregunta['explicacion']}")
        
        st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    st.subheader(" Puntuación")
    if st.session_state.preguntas_respondidas > 0:
        porcentaje = (st.session_state.puntuacion / st.session_state.preguntas_respondidas) * 100
        st.metric("", f"{st.session_state.puntuacion}/{st.session_state.preguntas_respondidas}")
        st.write(f"{porcentaje:.1f}%** de aciertos")
    else:
        st.write("Comienza respondiendo preguntas!")
    st.markdown('</div>', unsafe_allow_html=True)
    
   
    st.markdown("###  Estadísticas")
if st.session_state.historial:
        correctas = sum(1 for h in st.session_state.historial if h['correcta'])
        total = len(st.session_state.historial)
        
        col_stat1, col_stat2 = st.columns(2)
        with col_stat1:
            st.metric("Correctas", correctas)
        with col_stat2:
            st.metric("Total", total)


st.markdown("---")
st.subheader(" Modo de Estudio - Todas las Preguntas")

if st.checkbox("Mostrar todas las preguntas disponibles"):
    
    preguntas_mostrar = PREGUNTAS_BIBLICAS
    
    if dificultad != "Todas":
        preguntas_mostrar = [p for p in preguntas_mostrar if p['dificultad'] == dificultad]
    
    if categoria != "Todas":
        preguntas_mostrar = [p for p in preguntas_mostrar if p['categoria'] == categoria]
    
    for i, pregunta in enumerate(preguntas_mostrar):
        with st.expander(f"Pregunta {i+1}: {pregunta['pregunta']}", expanded=False):
            st.write(f"*Opciones:*")
            for opcion in pregunta['opciones']:
                if opcion == pregunta['respuesta']:
                    st.success(f" {opcion}")
                else:
                    st.write(f"• {opcion}")
            
            st.write(f"*Referencia:* {pregunta['referencia']}")
            st.write(f"*Explicación:* {pregunta['explicacion']}")
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>📖 <strong>Generador de Preguntas Bíblicas</strong> - Para edificación y estudio de las Escrituras</p>
    <p><em>"Tu palabra es una lámpara a mis pies; es una luz en mi sendero." - Salmo 119:105</em></p>
</div>
""", unsafe_allow_html=True)













    
