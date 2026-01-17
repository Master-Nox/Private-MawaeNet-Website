import streamlit as st
import base64
from streamlit_extras.bottom_container import bottom
from streamlit_extras.row import row

st.set_page_config(
    page_title="MawaeNet",
    page_icon="🌐",
    layout="wide"
)

st.markdown(
    """
        <style>
                .stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                    visibility: visible;  /* Ensure the header is visible */
                }

               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

# st.logo(image=r"MawaeNet.png", size="large", link="https://mawae.net")

toprow = row(6, vertical_align="center", gap="medium")
toprow.markdown("")
toprow.markdown("")
toprow.markdown("")
toprow.markdown("")
toprow.markdown("")
toprow.link_button("Home", type="secondary", use_container_width=True, url="https://mawae.net", help="Go to the Home page.") # When moved over to its own url, this will be substituted in.

# Load images as base64 for embedding in HTML
try:
    with open("static/images/jellyfin.webp", "rb") as f:
        jellyfin_b64 = base64.b64encode(f.read()).decode()
except FileNotFoundError:
    jellyfin_b64 = ""

try:
    with open("static/images/karakeep.webp", "rb") as f:
        karakeep_b64 = base64.b64encode(f.read()).decode()
except FileNotFoundError:
    karakeep_b64 = ""

try:
    with open("static/images/immich.webp", "rb") as f:
        immich_b64 = base64.b64encode(f.read()).decode()
except FileNotFoundError:
    immich_b64 = ""

try:
    with open("static/images/omnitools.webp", "rb") as f:
        omni_b64 = base64.b64encode(f.read()).decode()
except FileNotFoundError:
    omni_b64 = ""

try:
    with open("static/images/kuma.webp", "rb") as f:
        kuma_b64 = base64.b64encode(f.read()).decode()
except FileNotFoundError:
    kuma_b64 = ""

st.markdown("<h1 style='text-align: center;'>MawaeNet</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Welcome to the Private MawaeNet.</h5>", unsafe_allow_html=True)

# Create three columns for the link boxes
col1, col2, col3 = st.columns(3)

# Jellyfin
with col1:
    st.markdown(f'''
<a href="https://jellyfin.mawae.net" style="text-decoration: none; color: inherit;">
<div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center; background-color: #000000; margin: 10px;">
<p style="text-align: center; margin: 0; font-size: 2em;"><strong>Jellyfin</strong></p>
<img src="data:image/webp;base64,{jellyfin_b64}" alt="Jellyfin" width="128" style="margin: 10px 0;">
<p style="text-align: center; margin: 0;">Anime, Movie, and TV library</p>
</div>
</a>
''', unsafe_allow_html=True)

# OmniTools
with col1:
    st.markdown(f'''
<a href="https://omni.mawae.net" style="text-decoration: none; color: inherit;">
<div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center; background-color: #000000; margin: 10px;">
<p style="text-align: center; margin: 0; font-size: 2em;"><strong>OmniTools</strong></p>
<img src="data:image/webp;base64,{omni_b64}" alt="OmniTools" width="128" style="margin: 10px 0;">
<p style="text-align: center; margin: 0;">A collection of tools for images, videos, pdfs, text, etc</p>
</div>
</a>
''', unsafe_allow_html=True)

# Kuma
with col2:
    st.markdown(f'''
<a href="https://status.mawae.net" style="text-decoration: none; color: inherit;">
<div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center; background-color: #000000; margin: 10px;">
<p style="text-align: center; margin: 0; font-size: 2em;"><strong>Kuma</strong></p>
<img src="data:image/webp;base64,{kuma_b64}" alt="Kuma" width="128" style="margin: 10px 0;">
<p style="text-align: center; margin: 0;">Live status for all MawaeNet Services</p>
</div>
</a>
''', unsafe_allow_html=True)

# Karakeep
with col2:
    st.markdown(f'''
<a href="https://karakeep.mawae.net" style="text-decoration: none; color: inherit;">
<div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center; background-color: #000000; margin: 10px;">
<p style="text-align: center; margin: 0; font-size: 2em;"><strong>Karakeep</strong></p>
<img src="data:image/webp;base64,{karakeep_b64}" alt="Karakeep" width="128" style="margin: 10px 0;">
<p style="text-align: center; margin: 0;">Bookmark Manager</p>
</div>
</a>
''', unsafe_allow_html=True)

# Immich
with col3:
    st.markdown(f'''
<a href="https://immich.mawae.net" style="text-decoration: none; color: inherit;">
<div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center; background-color: #000000; margin: 10px;">
<p style="text-align: center; margin: 0; font-size: 2em;"><strong>Immich</strong></p>
<img src="data:image/webp;base64,{immich_b64}" alt="Immich" width="128" style="margin: 10px 0;">
<p style="text-align: center; margin: 0;">Photo Backup</p>
</div>
</a>
''', unsafe_allow_html=True)
    
with bottom():
    st.markdown("---")
    bottomrow = row(6, vertical_align="center", gap="medium")
    bottomrow.markdown("For questions, please reach out on Discord @masternox")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.link_button("Forgot Password?", type="secondary", use_container_width=True, url="https://account.mawae.net/reset-password/step1", help="Reset your password.")