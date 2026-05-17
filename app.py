# app.py
import streamlit as st
from cfg_parser import parse_cfg, print_cfg
from pda_converter import convert_cfg_to_pda
from visualizer import visualize_pda

st.set_page_config(page_title="CFG to PDA Converter", layout="wide")

st.title("CFG to PDA Converter")

st.write("Enter your CFG rules. You can use `ε` or `e` for epsilon.")

grammar_text = st.text_area(
    "CFG Rules",
    height=150
)

if st.button("Convert to PDA"):
    try:
        # split rules by lines and ignore empty lines
        grammar_lines = [
            line.strip()
            for line in grammar_text.splitlines()
            if line.strip() != ""
        ]

        cfg = parse_cfg(grammar_lines)
        pda = convert_cfg_to_pda(cfg)

        visualize_pda(pda, "pda_graph")

        st.image("pda_graph.png", caption="Generated PDA")

        st.success("PDA generated successfully!")

    except Exception as e:
        st.error(f"Error: {e}")