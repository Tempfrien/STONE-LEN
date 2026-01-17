import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* --- SECTION 1: ล้างค่ามาตรฐานของ Streamlit --- */
        header {visibility: hidden; display: none !important;}
        footer {visibility: hidden; display: none !important;}
        #MainMenu {visibility: hidden; display: none !important;}
        .stDeployButton {display:none !important;}
        [data-testid="stDecoration"] {display:none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        .viewerBadge_container__1QSob {display: none !important;}

        /* --- SECTION 2: พื้นหลังแอป --- */
        .stApp {
            background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                              url("https://images.wallpaperscraft.com/image/single/beach_rocks_stones_136868_3840x2400.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        /* --- SECTION 3: หัวข้อ STONE LEN (Neon) --- */
        .main-title {
            color: #ffffff !important;
            font-size: 80px !important;
            font-weight: 900;
            text-align: left;
            margin-top: -60px !important;
            font-family: 'Arial Black', sans-serif;
            text-shadow: 
                0 0 5px #fff, 0 0 10px #fff, 0 0 20px #ffaa00,
                0 0 40px #ffaa00, 0 0 80px #ffaa00, 0 0 90px #ffaa00, 0 0 100px #ffaa00;
        }

        /* --- SECTION 4: การตกแต่งปุ่มทั้งหมด --- */
        .stButton > button {
            background-color: #dcb799 !important;
            color: white !important;
            border-radius: 20px !important;
            padding: 10px 25px !important;
            font-weight: bold !important;
            border: 2px solid #fff !important;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #ffffff !important;
            color: #2d3e33 !important;
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(255,170,0,0.4);
        }

        /* --- SECTION 5: กล่องแสดงผลและรับไฟล์ --- */
        [data-testid="stFileUploader"] {
            width: 350px !important; 
            margin: 0 auto !important;
        }
        [data-testid="stFileUploader"] section {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 20px !important;
        }
        .result-box {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            color: #333333 !important;
        }

        /* --- SECTION 6: โลโก้ Fixed มุมขวาบน --- */
        .fixed-image {
            position: fixed;
            top: 0;
            right: 0;
            width: 325px;
            z-index: 1000;
            border-radius: 0 0 0 35px !important; 
            overflow: hidden !important;
        }
        .fixed-image img {
            width: 100% !important;
            border-radius: 0 0 0 35px !important;
            object-fit: cover;
        }

        /* --- SECTION 7: แถบ Footer --- */
        .footer-bar {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: rgba(45, 62, 51, 0.95);
            color: white;
            text-align: center;
            padding: 12px 0;
            font-size: 20px;
            z-index: 9999;
        }

        /* --- SECTION 8: ปรับแต่งสำหรับมือถือ (Responsive) --- */
        @media (max-width: 768px) {
            .fixed-image { width: 130px; border-radius: 0 0 0 15px !important; }
            .main-title { font-size: 45px !important; margin-top: -30px !important; }
            .footer-bar { font-size: 12px; }
            [data-testid="stFileUploader"] { width: 100% !important; }
        }
        </style>
    """, unsafe_allow_html=True)
