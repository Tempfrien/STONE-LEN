import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
from style_config import apply_custom_style

# --- ZONE 1: ตั้งค่าระบบ (Setup & Session) ---
st.set_page_config(page_title="STONE LEN - Rock Classification", layout="wide")
apply_custom_style()

if 'page' not in st.session_state:
    st.session_state.page = 'Main'

def change_page(name):
    st.session_state.page = name

# --- ZONE 2: องค์ประกอบลอยตัว (Fixed Image) ---
st.markdown("""
    <div class="fixed-image">
        <img src="https://lh3.googleusercontent.com/u/0/d/1j2yrrBp-xXv1vfk4fdrIxZxVmyX4Bszu">
    </div>
    """, unsafe_allow_html=True)

# --- ZONE 3: หน้าหลัก (AI Classification) ---
if st.session_state.page == 'Main':
    st.markdown('<h1 class="main-title">STONE LEN</h1>', unsafe_allow_html=True)
    
    if st.button("📖 เรียนรู้ลักษณะหิน"):
        change_page('Knowledge')
        st.rerun()

    st.markdown('<p class="sub-text">ROCK CLASSIFICATION : ถ่ายรูปหรืออัปโหลดรูปเพื่อจำแนกประเภทหิน</p>', unsafe_allow_html=True)

    # สร้าง Tab เพื่อเลือกวิธีนำเข้ารูปภาพ
    tab1, tab2 = st.tabs(["📸 ถ่ายภาพสด", "📁 อัปโหลดไฟล์"])

    source_img = None

    with tab1:
        cam_file = st.camera_input("กดปุ่มเพื่อเปิดกล้อง")
        if cam_file:
            source_img = cam_file

    with tab2:
        uploaded_file = st.file_uploader("เลือกรูปภาพจากเครื่อง", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            source_img = uploaded_file

    # --- ส่วนการประมวลผล (จะทำงานเมื่อมีรูปจากช่องทางใดช่องทางหนึ่ง) ---
    if source_img is not None:
        st.markdown("---")
        col1, col2 = st.columns([1, 1])
        image = Image.open(source_img).convert("RGB")
        
        with col1:
            st.image(image, caption="รูปที่ใช้ประมวลผล", use_container_width=True)
        
        # Logic AI (ใช้ Model และ Labels เดิมที่โหลดไว้)
        size = (224, 224)
        image_processed = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        img_array = np.asarray(image_processed)
        normalized_img = (img_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_img
        
        prediction = model.predict(data)
        index = np.argmax(prediction)
        
        with col2:
            st.markdown(f"""
                <div class="result-box">
                    <h2 style='text-align:center;'>🔍 ผลการวิเคราะห์</h2>
                    <hr>
                    <p style='font-size:20px;'>หินชนิดนี้คือ: <b style='color:#dcb799;'>{labels[index]}</b></p>
                    <p style='font-size:18px;'>ความแม่นยำ: <b>{prediction[0][index] * 100:.2f}%</b></p>
                </div>
            """, unsafe_allow_html=True)

# --- ZONE 4: หน้าความรู้ (Rock Info) ---
elif st.session_state.page == 'Knowledge':
    st.markdown('<h1 class="main-title">ROCK INFO</h1>', unsafe_allow_html=True)
    
    if st.button("🔙 กลับไปหน้าวิเคราะห์"):
        change_page('Main')
        st.rerun()

    st.markdown("""
        <div class="result-box">
            <h2 style="color:#2d3e33;">ประเภทของหินที่ควรรู้</h2>
            <hr>
            <h3>1. หินอัคนี (Igneous Rock)</h3>
            <p>เกิดจากการเย็นตัวของหินหนืด มักมีลักษณะแข็งและเห็นผลึกชัดเจน</p>
            <br>
            <h3>2. หินตะกอน (Sedimentary Rock)</h3>
            <p>เกิดจากการทับถมของเศษวัสดุ มักมีลักษณะเป็นชั้นๆ</p>
            <br>
            <h3>3. หินแปร (Metamorphic Rock)</h3>
            <p>เกิดจากความร้อนและความดันสูง มักมีริ้วขนานสวยงาม</p>
        </div>
    """, unsafe_allow_html=True)

# --- ZONE 5: แถบรายชื่อผู้พัฒนา ---
st.markdown("""
    <div class="footer-bar">
        Creators : Chadaporn Boonnii, Nopphanat Junnunl, Saranya Changkeb, Phatcharakamon Sodsri
    </div>
    """, unsafe_allow_html=True)
