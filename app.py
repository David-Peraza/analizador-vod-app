import streamlit as st

try:
    import app_logic
    if hasattr(app_logic, 'main'):
        app_logic.main()
    else:
        st.error("El módulo compilado no contiene la función 'main()'.")
except Exception as e:
    st.error(f"Error al ejecutar la app: {e}")
    import traceback
    st.code(traceback.format_exc())
