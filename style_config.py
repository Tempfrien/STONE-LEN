import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* --- ส่วนที่ 1: จัดการหน้าเว็บและซ่อนองค์ประกอบระบบ --- */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stDecoration"] {display:none;}
        [data-testid="stStatusWidget"] {display: none !important;}
        .viewerBadge_container__1QSob {display: none !important;}

        .stApp {
            background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                              url("https://images.wallpaperscraft.com/image/single/beach_rocks_stones_136868_3840x2400.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        /* --- ส่วนที่ 2: หัวข้อ STONE LEN (Neon Style) --- */
        .main-title {
            color: #ffffff !important;
            font-size: 80px !important;
            font-weight: 900;
            text-align: left;
            margin-top: -60px !important;
            font-family: 'Arial Black', sans-serif;
            text-shadow: 
                0 0 5px #fff,
                0 0 10px #fff,
                0 0 20px #ffaa00,
                0 0 40px #ffaa00,
                0 0 80px #ffaa00,
                0 0 90px #ffaa00,
                0 0 100px #ffaa00;
        }

        /* --- ส่วนที่ 3: กล่องอัปโหลด --- */
        [data-testid="stFileUploader"] {
            width: 350px !important; 
            margin: 0 auto !important;
        }
        [data-testid="stFileUploader"] section {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 20px !important;
            padding: 30px !important;
        }

        /* --- ส่วนที่ 4: ปุ่ม Upload file --- */
        button[kind="secondary"] {
            font-size: 0 !important;
            border-radius: 30px !important;
            padding: 10px 30px !important;
            background-color: white !important;
            border: 1px solid #ccc !important;
            display: block !important;
            margin: 0 auto !important;
        }
        button[kind="secondary"]::after {
            content: "Upload file";
            font-size: 16px !important;
            color: #333;
        }

        /* --- ส่วนที่ 5: แถบรายชื่อด้านล่าง --- */
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
            border-top: 1px solid rgba(255,255,255,0.1);
        }

        /* --- ส่วนที่ 6: โลโก้มุมขวาบนขอบโค้ง --- */
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

        /* --- ส่วนที่ 7: กล่องแสดงผลการวิเคราะห์ AI --- */
        .result-box {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            color: #333333 !important;
            margin-top: 20px;
        }
        .result-box h2 {
            color: #2d3e33 !important;
            margin-bottom: 15px;
        }
        </style>
    """, unsafe_allow_html=True)
