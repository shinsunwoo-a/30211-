import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="프리미엄 세계 여행 가이드",
    page_icon="✈️",
    layout="wide"
)

# 2. 화려하고 세련된 CSS 스타일링 적용 (카드, 이미지, 그라데이션)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Malgun Gothic', sans-serif;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(45deg, #FF4B4B, #FF8E53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    .place-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
        transition: 0.3s;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }
    .place-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #dfe9f3 100%);
        border-right: 2px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 대폭 확장된 국가 데이터베이스 (대한민국 포함, 고화질 이미지 링크 장착)
travel_data = {
    "대한민국": [
        {"name": "경복궁", "desc": "조선 시대의 정궁으로 웅장한 건축물과 전통의 아름다움을 간직한 곳입니다.", "img": "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?auto=format&fit=crop&w=600&q=80"},
        {"name": "N서울타워", "desc": "남산 정상에 위치해 서울의 전경을 한눈에 담을 수 있는 랜드마크입니다.", "img": "https://images.unsplash.com/photo-1538485399081-0268579d4725?auto=format&fit=crop&w=600&q=80"},
        {"name": "부산 해운대", "desc": "아름다운 백사장과 시원한 바다가 펼쳐지는 대한민국 최고의 휴양지입니다.", "img": "https://images.unsplash.com/photo-1578637387939-43c525bc20c4?auto=format&fit=crop&w=600&q=80"}
    ],
    "프랑스": [
        {"name": "에펠탑", "desc": "파리를 상징하는 대표적인 철탑으로 환상적인 야경을 자랑합니다.", "img": "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?auto=format&fit=crop&w=600&q=80"},
        {"name": "루브르 박물관", "desc": "모나리자 등 세계적인 예술품이 소장된 세계 최대 미술관입니다.", "img": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=600&q=80"},
        {"name": "몽마르트 언덕", "desc": "예술가들의 아지트였으며 파리 시내가 내려다보이는 낭만적인 곳입니다.", "img": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=600&q=80"}
    ],
    "일본": [
        {"name": "도쿄 타워", "desc": "도쿄의 상징인 붉은빛 전파탑으로 로맨틱한 야경 명소입니다.", "img": "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?auto=format&fit=crop&w=600&q=80"},
        {"name": "오사카 성", "desc": "일본의 유서 깊은 역사적 건축물이자 아름다운 벚꽃 명소입니다.", "img": "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?auto=format&fit=crop&w=600&q=80"},
        {"name": "교토 청수사", "desc": "유네스코 세계문화유산으로 고즈넉한 전통 미가 빛나는 사찰입니다.", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=600&q=80"}
    ],
    "미국": [
        {"name": "자유의 여신상", "desc": "뉴욕 허드슨 강 입구에 위치한 미국의 상징적인 동상입니다.", "img": "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?auto=format&fit=crop&w=600&q=80"},
        {"name": "그랜드 캐니언", "desc": "수백만 년 동안 대자연이 빚어낸 웅장하고 신비로운 대협곡입니다.", "img": "https://images.unsplash.com/photo-1474044159976-18175f04b7a7?auto=format&fit=crop&w=600&q=80"},
        {"name": "금문교", "desc": "샌프란시스코의 붉은 현수교로 안개 낀 풍경이 예술입니다.", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=600&q=80"}
    ],
    "스위스": [
        {"name": "융프라우요흐", "desc": "유럽의 지붕이라 불리며 만년설의 대절경을 선사하는 곳입니다.", "img": "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?auto=format&fit=crop&w=600&q=80"},
        {"name": "마테호른", "desc": "피라미드 형태의 독보적인 위용을 뽐내는 거대한 설산입니다.", "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=600&q=80"}
    ],
    "이탈리아": [
        {"name": "콜로세움", "desc": "고대 로마 제국 시절의 웅장함을 간직한 거대한 원형 경기장입니다.", "img": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=600&q=80"},
        {"name": "베네치아 운하", "desc": "물의 도시 베네치아에서 곤돌라를 타고 즐기는 로맨틱한 수로입니다.", "img": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=600&q=80"}
    ],
    "호주": [
        {"name": "시드니 오페라 하우스", "desc": "조개껍데기 디자인의 독창적인 건축미를 자랑하는 랜드마크입니다.", "img": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=600&q=80"},
        {"name": "그레이트 배리어 리프", "desc": "우주에서도 보인다는 경이로운 세계 최대의 산호초 군락입니다.", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=600&q=80"}
    ],
    "영국": [
        {"name": "대영 박물관", "desc": "세계 각국의 역사적 유물과 문화재가 보존된 거대한 박물관입니다.", "img": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=600&q=80"},
        {"name": "타워 브리지", "desc": "템스 강을 가로지르는 런던의 상징적인 개폐식 교량입니다.", "img": "https://images.unsplash.com/photo-1526129318478-62ed807ebdf9?auto=format&fit=crop&w=600&q=80"}
    ]
}

# 4. 메인 타이틀
st.markdown('<p class="main-title">✈️ 프리미엄 세계 문화 관광지</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-title">총 <b>{len(travel_data)}개국</b>의 엄선된 아름다운 명소와 사진을 확인해 보세요!</p>', unsafe_allow_html=True)

# 5. 사이드바 구성
st.sidebar.markdown("### 🔍 여행지 탐색")
search_type = st.sidebar.radio("방식 선택", ["목록에서 고르기", "직접 검색하기"])

selected = ""
if search_type == "목록에서 고르기":
    selected = st.sidebar.selectbox("나라 선택", list(travel_data.keys()))
else:
    inp = st.sidebar.text_input("나라 이름 입력 (예: 대한민국, 프랑스)", "")
    if inp:
        selected = inp.strip()

st.sidebar.markdown("---")
st.sidebar.info("💡 사이드바에서 원하는 국가를 고르면 카드 형태의 멋진 관광지와 사진이 출력됩니다.")

# 6. 결과 출력 영역 (카드 + 이미지 레이아웃)
if selected:
    if selected in travel_data:
        st.markdown(f"## 🌟 **'{selected}'** 추천 관광지 베스트")
        st.markdown("")
        
        # 2열 카드 구성
        cols = st.columns(2)
        for idx, place in enumerate(travel_data[selected]):
            with cols[idx % 2]:
                st.markdown(f"""
                    <div class="place-card">
                        <h3>📍 {place['name']}</h3>
                        <p style="color: #444; font-size: 15px; line-height: 1.5;">{place['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)
                # 이미지 출력
                st.image(place['img'], use_column_width=True, caption=place['name'])
    else:
        st.error(f"죄송합니다! '{selected}'에 대한 정보가 아직 등록되지 않았습니다.")
else:
    st.info("👈 왼쪽 사이드바에서 나라를 선택하거나 검색해 보세요!")
