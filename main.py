import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="프리미엄 세계 여행 가이드",
    page_icon="🌍",
    layout="wide"
)

# 2. 더욱 화려하고 티 나게 개편된 CSS 스타일링 (네온 효과, 글래스모피즘, 애니메이션)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
        font-family: 'Malgun Gothic', sans-serif;
        color: #f8fafc;
    }
    .main-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 0 0 30px rgba(56, 189, 248, 0.3);
    }
    .sub-title {
        text-align: center;
        color: #94a3b8;
        font-size: 1.3rem;
        margin-bottom: 40px;
        font-weight: 600;
    }
    .place-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(16px);
        padding: 26px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .place-card:hover {
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 20px 40px rgba(56, 189, 248, 0.2);
        border: 1px solid rgba(56, 189, 248, 0.4);
        background: rgba(30, 41, 59, 0.9);
    }
    .place-title {
        color: #38bdf8;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .place-desc {
        color: #cbd5e1;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 2px solid #334155;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 대폭 확장된 국가 데이터베이스 (각 국가별 관광지 4~5개, 사진 키워드 제거)
travel_data = {
    "대한민국": [
        {"name": "경복궁", "desc": "조선 시대의 정궁으로 웅장한 건축물과 전통의 아름다움을 간직한 곳입니다."},
        {"name": "N서울타워", "desc": "남산 정상에 위치해 서울의 아름다운 야경과 전경을 담을 수 있는 랜드마크입니다."},
        {"name": "부산 해운대", "desc": "탁 트인 백사장과 푸른 바다가 펼쳐지는 대한민국 최고의 해양 휴양지입니다."},
        {"name": "제주 성산일출봉", "desc": "바다 위에 솟아오른 거대한 화산 성채로 일출의 장관이 예술인 곳입니다."},
        {"name": "경주 불국사", "desc": "신라 천년의 불교 예술과 석가탑, 다보탑의 고결함을 품은 유네스코 세계유산입니다."}
    ],
    "프랑스": [
        {"name": "에펠탑", "desc": "파리를 상징하는 대표적인 철탑으로 환상적인 야경과 조명을 자랑합니다."},
        {"name": "루브르 박물관", "desc": "모나리자 등 세계적인 예술품과 피라미드 조형물이 있는 최대 미술관입니다."},
        {"name": "몽마르트 언덕", "desc": "예술가들의 아지트이자 파리 시내가 한눈에 내려다보이는 낭만적인 곳입니다."},
        {"name": "베르사유 궁전", "desc": "절대왕정의 화려함과 거대한 정원이 조화로운 역사의 정수입니다."},
        {"name": "니스 해변", "desc": "지중해의 눈부신 에메랄드빛 바다와 따스한 태양이 반기는 휴양지입니다."}
    ],
    "일본": [
        {"name": "도쿄 타워", "desc": "도쿄의 상징인 붉은빛 전파탑으로 로맨틱한 분위기를 선사하는 명소입니다."},
        {"name": "오사카 성", "desc": "일본의 유서 깊은 역사적 건축물이자 아름다운 정원과 성곽이 어우러진 곳입니다."},
        {"name": "교토 청수사", "desc": "유네스코 세계문화유산으로 고즈넉한 전통 미와 단풍/벚꽃이 빛나는 사찰입니다."},
        {"name": "오키나와 츄라우미 수족관", "desc": "거대한 고래상고가 유영하는 세계 최대 수준의 해양 수족관입니다."},
        {"name": "후쿠오카 오호리 공원", "desc": "도심 속에서 여유롭게 호수를 산책하며 휴식을 즐길 수 있는 아름다운 공원입니다."}
    ],
    "미국": [
        {"name": "자유의 여신상", "desc": "뉴욕 허드슨 강 입구에 위치해 자유와 독립을 상징하는 거대한 동상입니다."},
        {"name": "그랜드 캐니언", "desc": "수백만 년 동안 대자연이 빚어낸 웅장하고 신비로운 거대 협곡입니다."},
        {"name": "금문교", "desc": "샌프란시스코의 붉은 현수교로 안개 낀 바다 풍경과 어우러져 절경을 이룹니다."},
        {"name": "라스베가스 스트립", "desc": "화려한 네온사인과 세계적인 호텔, 쇼가 가득한 불야성의 거리입니다."},
        {"name": "옐로스톤 국립공원", "desc": "간헐천과 야생동물이 살아 숨 쉬는 세계 최초의 국립공원입니다."}
    ],
    "스위스": [
        {"name": "융프라우요흐", "desc": "유럽의 지붕이라 불리며 사계절 내내 만년설의 대절경을 선사하는 곳입니다."},
        {"name": "마테호른", "desc": "피라미드 형태의 독보적인 위용을 뽐내는 알파인 산악 지대의 상징입니다."},
        {"name": "인터라켄", "desc": "두 호수 사이에 위치해 알프스를 즐기는 전 세계 여행자의 베이스캠프입니다."},
        {"name": "루체른 호수", "desc": "중세 도시의 풍경과 에메랄드빛 호수, 카펠교가 어우러진 낭만의 도시입니다."}
    ],
    "이탈리아": [
        {"name": "콜로세움", "desc": "고대 로마 제국 시절의 웅장함을 그대로 간직한 거대한 원형 경기장입니다."},
        {"name": "베네치아 운하", "desc": "물의 도시 베네치아에서 곤돌라를 타고 즐기는 로맨틱한 물길 풍경입니다."},
        {"name": "피렌체 두오모", "desc": "붉은 돔 성당 위로 피렌체 시내가 한눈에 내려다보이는 르네상스의 심장부입니다."},
        {"name": "로마 트레비 분수", "desc": "동전을 던지면 다시 로마에 오게 된다는 전설이 있는 아름다운 바로크 분수입니다."}
    ],
    "호주": [
        {"name": "시드니 오페라 하우스", "desc": "조개껍데기 디자인의 독창적인 건축미를 자랑하는 세계적인 랜드마크입니다."},
        {"name": "그레이트 배리어 리프", "desc": "우주에서도 보인다는 경이로운 에메랄드빛 세계 최대의 산호초 군락입니다."},
        {"name": "울루루(에어즈 록)", "desc": "붉은 대지 한가운데 솟아오른 호주 원주민의 신성한 거대 바위입니다."},
        {"name": "본다이 비치", "desc": "서핑의 성지이자 황금빛 모래사장과 시원한 파도가 반기는 해변입니다."}
    ],
    "영국": [
        {"name": "대영 박물관", "desc": "세계 각국의 역사적 유물과 고대 문화재가 보존된 거대한 박물관입니다."},
        {"name": "타워 브리지", "desc": "템스 강을 가로지르는 런던의 상징적인 고풍스러운 개폐식 교량입니다."},
        {"name": "빅벤 & 국회의사당", "desc": "런던의 시간을 알리는 웅장한 고딕 양식의 거대한 시계탑입니다."},
        {"name": "런던 아이", "desc": "템스 강변에서 런던의 전경을 360도로 조망할 수 있는 거대한 대관람차입니다."}
    ],
    "캐나다": [
        {"name": "밴프 국립공원", "desc": "로키산맥의 청록색 호수와 만년설이 빚어내는 태고의 신비로운 자연입니다."},
        {"name": "나이아가라 폭포", "desc": "엄청난 물줄기가 뿜어내는 굉음과 물보라가 압도적인 세계적 폭포입니다."},
        {"name": "토론토 CN 타워", "desc": "캐나다 스카이라인을 압도하며 도시 전체를 내려다보는 거대 타워입니다."},
        {"name": "퀘벡 구시가지", "desc": "북미에서 유일하게 성곽으로 둘러싸인 유럽 감성의 낭만적인 도시입니다."}
    ],
    "스페인": [
        {"name": "사그라다 파밀리아", "desc": "가우디의 천재성이 영원히 숨 쉬고 있는 바르셀로나의 미완의 걸작 성당입니다."},
        {"name": "알함브라 궁전", "desc": "이슬람 문화의 화려함과 정교함의 극치를 보여주는 그라나다의 보석입니다."},
        {"name": "구엘 공원", "desc": "알록달록한 타일 모자이크와 동화 같은 건축물이 가득한 환상적인 공원입니다."},
        {"name": "마드리드 프라도 미술관", "desc": "스페인 왕실의 소장품을 바탕으로 벨라스케스, 고야 등의 명작이 가득한 곳입니다."}
    ]
}

# 4. 메인 타이틀
st.markdown('<p class="main-title">🌍 프리미엄 세계 문화 관광지 가이드</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-title">총 <b>{len(travel_data)}개국</b>의 엄선된 알짜배기 명소들을 확인해 보세요!</p>', unsafe_allow_html=True)

# 5. 사이드바 구성
st.sidebar.markdown("### 🔍 여행지 탐색하기")
search_type = st.sidebar.radio("조회 방식 선택", ["목록에서 고르기", "직접 검색하기"])

selected = ""
if search_type == "목록에서 고르기":
    selected = st.sidebar.selectbox("나라를 선택하세요", list(travel_data.keys()))
else:
    inp = st.sidebar.text_input("나라 이름 입력 (예: 스페인, 캐나다)", "")
    if inp:
        selected = inp.strip()

st.sidebar.markdown("---")
st.sidebar.info("💡 왼쪽 메뉴에서 원하는 국가를 선택하면 카드형 디자인으로 알찬 관광지 정보가 출력됩니다.")

# 6. 결과 출력 영역 (카드 레이아웃 - 사진 제외 및 항목 확장)
if selected:
    if selected in travel_data:
        st.markdown(f"## ✨ **'{selected}'** 추천 관광지 베스트")
        st.markdown("")
        
        # 2열 반응형 카드 레이아웃 구성
        cols = st.columns(2)
        for idx, place in enumerate(travel_data[selected]):
            with cols[idx % 2]:
                st.markdown(f"""
                    <div class="place-card">
                        <div class="place-title">📍 {place['name']}</div>
                        <div class="place-desc">{place['desc']}</div>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.error(f"죄송합니다! '{selected}'에 대한 정보가 아직 등록되지 않았습니다. 다른 나라를 선택해 주세요.")
else:
    st.info("👈 왼쪽 사이드바에서 나라를 선택하거나 검색해 보세요!")
