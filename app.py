import streamlit as st

try:
    import app_logic
    if hasattr(app_logic, 'main'):
        app_logic.main()
except Exception as e:
    st.error(f"Error al ejecutar la aplicación: {e}")
