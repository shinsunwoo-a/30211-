import streamlit as st

# 1. 페이지 기본 설정 (와이드 레이아웃 적용)
st.set_page_config(
    page_title="세계 문화 관광지 가이드",
    page_icon="🌍",
    layout="wide"
)

# 2. 커스텀 CSS 적용 (꾸미기)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 45px;
    }
    .stButton>button:hover {
        background-color: #ff2222;
    }
    .place-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 데이터베이스 확장 (다양한 대륙과 15개국 이상 등록)
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
        {"name": "구엘 공원", "desc": "알록달록한 타일과 독특한 건축물로 가득한 동화 같은 공원입니다."}
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
    "이집트": [
        {"name": "기자 피라미드", "desc": "고대 세계 7대 불가사의 중 하나로 거대한 파라오의 무덤입니다."},
        {"name": "룩소르 신전", "desc": "고대 이집트의 수도 테베에 세워진 거대한 신전 유적입니다."}
    ],
    "태국": [
        {"name": "방콕 왕궁", "desc": "화려한 황금빛 건축물들로 가득한 태국의 대표 랜드마크입니다."},
        {"name": "왓 아룬", "desc": "짜오프라야 강변에 위치하며 새벽녘에 아름답게 빛나는 사찰입니다."}
    ]
}

# 4. 메인 화면 구성
st.title("✈️ World Travel Guide & 핫플 추천기")
st.markdown("가보고 싶은 나라를 선택하거나 검색하여 유명 관광지와 설명을 확인해보세요!")

# 5. 사이드바 구성 (검색 및 필터 기능)
st.sidebar.header("🔍 검색 및 국가 선택")
search_method = st.sidebar.radio("조회 방식을 선택하세요", ["직접 검색하기", "목록에서 고르기"])

selected_country = ""

if search_method == "직접 검색하기":
    user_input = st.sidebar.text_input("나라 이름을 입력하세요", "")
    if user_input:
        selected_country = user_input.strip()
else:
    country_list = list(travel_data.keys())
    selected_country = st.sidebar.selectbox("등록된 나라 목록", country_list)

# 사이드바에 전체 등록 국가 수 표시
st.sidebar.markdown("---")
st.sidebar.info(f"현재 총 **{len(travel_data)}개국**의 정보가 등록되어 있습니다.")

# 6. 결과 출력 영역
if selected_country:
    if selected_country in travel_data:
        st.markdown(f"## 🎉 '{selected_country}' 추천 관광지 베스트")
        st.markdown("")
        
        # 2열 레이아웃으로 카드 배치
        cols = st.columns(2)
        for idx, place in enumerate(travel_data[selected_country]):
            with cols[idx % 2]:
                with st.container():
                    st.markdown(f"""
                        <div class="place-card">
                            <h3>📍 {place['name']}</h3>
                            <p style="color: #555; font-size: 16px;">{place['desc']}</p>
                        </div>
                    """, unsafe_allow_html=True)
    else:
        st.error(f"죄송합니다! '{selected_country}'에 대한 정보가 아직 없습니다. 다른 나라를 선택해 주세요.")
else:
    # 초기 화면 안내
    st.info("👈 왼쪽 사이드바에서 나라를 검색하거나 선택해주세요.")
    
    # 웰컴 배너 느낌으로 전체 국가 미리보기 제공
    st.markdown("### 🌟 등록된 여행지 미리보기")
    preview_cols = st.columns(4)
    countries = list(travel_data.keys())
    for i, country in enumerate(countries[:8]):
        with preview_cols[i % 4]:
            st.metric(label=f"인기 여행지", value=country)
