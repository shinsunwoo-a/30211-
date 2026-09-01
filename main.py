import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="세계 문화 관광지 가이드",
    page_icon="✈️",
    layout="wide"
)

# 2. 화려하고 세련된 CSS 스타일링 적용
st.markdown("""
    <style>
    /* 전체 배경 그라데이션 및 폰트 설정 */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Malgun Gothic', sans-serif;
    }
    
    /* 메인 타이틀 화려하게 꾸미기 */
    .main-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(45deg, #FF4B4B, #FF8E53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }

    /* 버튼 스타일 개조 */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FF4B4B, #FF7676);
        color: white;
        font-weight: bold;
        border-radius: 20px;
        height: 50px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.6);
    }

    /* 관광지 카드 디자인 (글래스모피즘 효과) */
    .place-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .place-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.25);
    }
    
    /* 사이드바 디자인 변경 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #e4e9f2 100%);
        border-right: 2px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 대폭 확장된 국가 데이터베이스 (다양한 대륙 포함)
travel_data = {
    "프랑스": [
        {"name": "에펠탑", "desc": "파리를 상징하는 대표적인 철탑으로 야경이 아름답습니다."},
        {"name": "루브르 박물관", "desc": "모나리자 등 세계적인 예술품이 소장된 세계 최대 미술관입니다."},
        {"name": "몽마르트 언덕", "desc": "예술가들의 아지트였으며 파리 시내가 한눈에 내려다보이는 곳입니다."}
    ],
    "일본": [
        {"name": "도쿄 타워", "desc": "도쿄의 랜드마크로 붉은색과 흰색이 조화를 이루는 전파탑입니다."},
        {"name": "오사카 성", "desc": "일본의 역사적인 성이자 벚꽃 명소로 유명합니다."},
        {"name": "교토 청수사", "desc": "유네스코 세계문화유산으로 전통 건축물이 아름다운 사찰입니다."}
    ],
    "미국": [
        {"name": "자유의 여신상", "desc": "뉴욕 허드슨 강 입구에 있는 미국의 상징적인 동상입니다."},
        {"name": "그랜드 캐니언", "desc": "수백만 년 동안 대자연이 깎아 만든 웅장한 협곡입니다."},
        {"name": "금문교", "desc": "샌프란시스코의 붉은 현수교로 안개 낀 풍경이 유명합니다."}
    ],
    "이탈리아": [
        {"name": "콜로세움", "desc": "고대 로마 제국 시절 지어진 원형 경기장입니다."},
        {"name": "베네치아 운하", "desc": "물의 도시 베네치아를 곤돌라를 타고 즐길 수 있는 수로입니다."},
        {"name": "피사의 탑", "desc": "기울어진 독특한 모양으로 유명한 종탑입니다."}
    ],
    "영국": [
        {"name": "대영 박물관", "desc": "세계 각국의 방대한 문화유산과 유물이 소장된 박물관입니다."},
        {"name": "타워 브리지", "desc": "템스 강 위에 세워진 런던의 상징적인 개폐식 교량입니다."},
        {"name": "빅벤", "desc": "영국 국회의사당 북쪽에 위치한 거대한 시계탑입니다."}
    ],
    "스페인": [
        {"name": "사그라다 파밀리아", "desc": "가우디가 설계하고 여전히 건설 중인 바르셀로나의 성당입니다."},
        {"name": "구엘 공원", "desc": "알록달록한 타일과 독특한 건축물로 가득한 동화 같은 공원입니다."},
        {"name": "알람브라 궁전", "desc": "이슬람 문화의 정수를 보여주는 그라나다의 아름다운 궁전입니다."}
    ],
    "스위스": [
        {"name": "융프라우요흐", "desc": "유럽의 지붕이라 불리며 만년설과 알프스의 절경을 볼 수 있는 곳입니다."},
        {"name": "마테호른", "desc": "피라미드 모양의 독특하고 웅장한 설산으로 유명합니다."}
    ],
    "베트남": [
        {"name": "하롱베이", "desc": "수천 개의 기암괴석과 에메랄드빛 바다가 어우러진 절경입니다."},
        {"name": "호이안 올드타운", "desc": "밤이 되면 형형색색의 등불이 켜지는 아름다운 전통 도시입니다."}
    ],
    "호주": [
        {"name": "시드니 오페라 하우스", "desc": "조개껍데기 모양의 독특한 외관을 자랑하는 세계적인 건축물입니다."},
        {"name": "그레이트 배리어 리프", "desc": "우주에서도 보인다는 세계 최대의 산호초 군락입니다."}
    ],
    "캐나다": [
        {"name": "나이아가라 폭포", "desc": "세계에서 가장 유명한 거대하고 웅장한 폭포 중 하나입니다."},
        {"name": "밴프 국립공원", "desc": "에메랄드빛 호수와 로키산맥의 대자연을 만끽할 수 있는 곳입니다."}
    ],
    "독일": [
        {"name": "브란덴부르크 문", "desc": "베를린의 상징이자 통일과 평화의 역사적 기념물입니다."},
        {"name": "노이슈반슈타인 성", "desc": "동화 속 성의 모티브가 된 알프스 자락의 아름다운 성입니다."}
    ],
    "브라질": [
        {"name": "예수 그리스도상", "desc": "코르코바두 산 정상에 위치한 리우데자네이루의 거대한 상징물입니다."},
        {"name": "이과수 폭포", "desc": "세계에서 가장 웅장하고 거대한 규모를 자랑하는 폭포입니다."}
    ],
    "뉴질랜드": [
        {"name": "밀포드 사운드", "desc": "태고의 신비가 가득한 빙하 협곡과 피오르드 지형입니다."},
        {"name": "호비튼 무비 세트", "desc": "영화 '반지의 제왕' 촬영지로 아기자기한 동화마을 같은 곳입니다."}
    ],
    "멕시코": [
        {"name": "치첸이트사", "desc": "고대 마야 문명의 신비로움을 간직한 거대한 피라미드 유적입니다."},
        {"name": "칸쿤 해변", "desc": "에메랄드빛 카리브해를 품은 세계적인 휴양지입니다."}
    ],
    "싱가포르": [
        {"name": "마리나 베이 샌즈", "desc": "배 모양의 독특한 스카이파크 수영장으로 유명한 랜드마크입니다."},
        {"name": "가든스 바이 더 베이", "desc": "거대한 슈퍼트리와 실내 식물원이 어우러진 미래형 정원입니다."}
    ]
}

# 4. 메인 화면 헤더
st.markdown('<p class="main-title">✈️ World Travel Guide</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-title">총 <b>{len(travel_data)}개국</b>의 엄선된 세계 유명 관광지 정보를 확인해 보세요!</p>', unsafe_allow_html=True)

# 5. 사이드바 검색 및 선택 영역
st.sidebar.markdown("### 🔍 여행지 탐색")
search_method = st.sidebar.radio("조회 방식을 선택하세요", ["목록에서 선택하기", "직접 검색하기"])

selected_country = ""

if search_method == "목록에서 선택하기":
    country_list = list(travel_data.keys())
    selected_country = st.sidebar.selectbox("가고 싶은 나라를 골라주세요", country_list)
else:
    user_input = st.sidebar.text_input("나라 이름을 입력하세요 (예: 독일, 브라질 등)", "")
    if user_input:
        selected_country = user_input.strip()

# 사이드바 안내
st.sidebar.markdown("---")
st.sidebar.info("💡 드롭다운에서 선택하거나 직접 입력하여 다양한 국가의 명소를 구경하세요.")

# 6. 결과 출력 영역
if selected_country:
    if selected_country in travel_data:
        st.markdown(f"### 🎉 **'{selected_country}'** 추천 관광지 베스트")
        st.markdown("")
        
        # 2열 카드 레이아웃 배치
        cols = st.columns(2)
        for idx, place in enumerate(travel_data[selected_country]):
            with cols[idx % 2]:
                st.markdown(f"""
                    <div class="place-card">
                        <h3>📍 {place['name']}</h3>
                        <p style="color: #444; font-size: 16px; line-height: 1.5;">{place['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.error(f"죄송합니다! '{selected_country}'에 대한 정보가 아직 등록되지 않았습니다. 사이드바의 목록에서 다른 나라를 선택해 주세요.")
else:
    st.info("👈 왼쪽 사이드바에서 나라를 선택하거나 검색해 보세요!")
    
    # 하단 미리보기 배너
    st.markdown("---")
    st.markdown("### 🌟 등록된 주요 대륙별 인기 국가")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="유럽 대표", value="프랑스 / 스위스")
    with c2:
        st.metric(label="아시아 대표", value="일본 / 베트남")
    with c3:
        st.metric(label="아메리카 대표", value="미국 / 브라질")
    with c4:
        st.metric(label="오세아니아/기타", value="호주 / 뉴질랜드")
