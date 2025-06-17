import streamlit as st
import pandas as pd
qd = [28, 20, 14, 3, 1]
precio = [100, 200, 500, 1200, 2000]
datos = pd.DataFrame({
    "Precio": list((precio)),
    "Cantidad demandada": list((qd))
})
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@100..900&display=swap');
h1, h2, h3, h4, h5, h6, p, th, td, table {
    font-family: Inter !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown(r"""
## Elasticidad arco
*Por: Josué Arias - 17/06/2025 5:03*
- ### ¿Qué es la elásticidad?
La *elásticidad arco* es una formúla matemática, usada en economía para representar la forma en la que **la demanda reacciona frente a un cambio en el precio**
- ### ¿De qué sirve?
Es muy útil para medir como reaccionará la demanda de un bien **frente a un cambio en el precio**

Para dar un ejemplo más facil:
- ¿Como podemos saber que tanto puede un consumidor dejar de demandar $"x"$ cantidad del bien $"a"$ si su precio $"y"$ ahora es $"y + 10"$?

Primero se toman datos, usé estos de ejemplo:
""")
st.dataframe(pd.DataFrame({
    "Precio": [100, 110],
    "Cantidad demandada": [10, 8],
}), hide_index=True)
st.write("""
Como podemos apreciar, si el producto cuesta 100, el consumidor compra 10 unidades

Ahora, si el producto cuesta 110, el consumidor compra 8 unidades

Aquí entra la duda de:
> ¿Este producto es muy propenso a perder demanda si subo el precio?

Si la respuesta es si, este producto es **elástico**, es decir, **delicado** a cambios en el precio

Si la respuesta es no, significa que el producto es **inelástico**, lo que significa que el producto **no es delicado** a cambios en el precio. Esto ocurre principalmente con productos escenciales, como agua

- ### ¿Como mido eso?
Para obtener el valor, que nos va a servir para determinar si el producto es elástico, o inelástico, se usa esta fórmula llamada **elásticidad arco** o también **punto medio**:
""")
st.latex(r"""
\Large E =\frac{ \frac{\Delta Q} {Q\, promedio}} {\frac{\Delta P}{P\, promedio}}
""")
st.markdown("""
Siendo "Q" la cantidad demandada y "P" el precio, si la aplicamos:
""")

st.latex(r"""
\Large E =\frac{\frac{8 - 10}{(8 + 10) / 2}}{\frac{110 - 100}{(110 + 100) / 2}} = \frac{-0.222}{0.095} = -2.34
""")

data = {
    "Rango de Ed": ["Ed > 1", "Ed = 1", "0 < Ed < 1", "Ed = 0", "Ed = ∞"],
    "Tipo de Demanda": ["Elástica", "Unitaria", "Inelástica", "Perfectamente Inelástica", "Perfectamente Elástica"],
    "Significado Económico": [
        "La cantidad cambia más que el precio (ej.: productos no esenciales).",
        "Cambio proporcional igual en precio y cantidad.",
        "La cantidad cambia menos que el precio (ej.: alimentos básicos).",
        "La cantidad no varía (ej.: medicinas críticas).",
        "Mínimo cambio en precio hace que la demanda caiga a cero (ej.: commodities)."
    ]
}

df = pd.DataFrame(data)

st.markdown("""
Para interpretar la élasticidad, se usan estos **umbrales**:
""")

st.dataframe(df, hide_index=True, use_container_width=True)

st.markdown("""
Nuestro producto tiene elásticidad **elástica**, para interpretar su valor, se usa su **valor absoluto:**
""")
st.latex(r"""
\Large E = \left| -2.34 \right| = 2.34
""")
st.markdown("""
Acá vemos que entra en $Ed > 1 = Elástica$

Esto significa que este producto **no es escencial**, ya que un cambio en su precio, afectó **mucho** la demanda, si este fuera un producto escencial como el agua, por ejemplo, veriamos, muy probablamente que su precio suba, y aún asi la demanda se mantiene muy parecida, esto porque, siendo un producto necesario, ¿se puede simplemente dejar de comprar porque esta muy caro, siendo un bien del cual dependemos para sobrevivir? **no** sea como sea su demanda debe seguir.

He aquí el porque de la importancia del **libre mercado** y la competencia para evitar **monopolios**
""")
