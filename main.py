import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="UN 193개국 세계 관광지 가이드",
    page_icon="✈️",
    layout="wide"
)

# 193개 UN 회원국 전체 데이터 (포르투갈 상세 관광지 반영)
UN_193_RAW_DATA = [
    {"name": "포르투갈", "region": "유럽", "capital": "리스본", "flag": "🇵🇹", "attractions": ["리스본 벨렝 탑", "신트라 페나 궁전", "포르투 도루 강 & 동 루이스 1세 다리", "호카 곶", "렐루 서점"]},
    {"name": "대한민국", "region": "아시아", "capital": "서울", "flag": "🇰🇷", "attractions": ["경복궁", "남산서울타워", "해운대 해수욕장", "제주 한라산"]},
    {"name": "일본", "region": "아시아", "capital": "도쿄", "flag": "🇯🇵", "attractions": ["도쿄타워", "교토 기요미즈데라", "오사카성", "후지산"]},
    {"name": "중화인민공화국", "region": "아시아", "capital": "베이징", "flag": "🇨🇳", "attractions": ["만리장성", "자금성", "병마용갱", "계림 산수"]},
    {"name": "베트남", "region": "아시아", "capital": "하노이", "flag": "🇻🇳", "attractions": ["하롱베이", "호이안 구시가지", "하노이 호안끼엠 호수", "다낭 바나힐"]},
    {"name": "태국", "region": "아시아", "capital": "방콕", "flag": "🇹🇭", "attractions": ["방콕 왕궁", "푸켓 피피섬", "치앙마이 사원", "아유타야"]},
    {"name": "인도네시아", "region": "아시아", "capital": "자카르타", "flag": "🇮🇩", "attractions": ["발리 우붓", "보로부두르 사원", "코모도 국립공원", "브로모 산"]},
    {"name": "싱가포르", "region": "아시아", "capital": "싱가포르", "flag": "🇸🇬", "attractions": ["마리나 베이 샌즈", "가든스 바이 더 베이", "센토사 섬", "유니버설 스튜디오"]},
    {"name": "말레이시아", "region": "아시아", "capital": "쿠알라룸푸르", "flag": "🇲🇾", "attractions": ["페트로나스 트윈 타워", "랑카위", "바투 동굴", "페낭 구시가지"]},
    {"name": "필리핀", "region": "아시아", "capital": "마닐라", "flag": "🇵🇭", "attractions": ["보라카이 화이트비치", "세부 보홀 섬", "팔라완 엘니도", "마닐라 인트라무로스"]},
    {"name": "인도", "region": "아시아", "capital": "뉴델리", "flag": "🇮🇳", "attractions": ["타지마할", "자이푸르 암베르 성", "바라나시 갠지스강", "아그라 요새"]},
    {"name": "프랑스", "region": "유럽", "capital": "파리", "flag": "🇫🇷", "attractions": ["에펠탑", "루브르 박물관", "베르사유 궁전", "몽마르트르"]},
    {"name": "영국", "region": "유럽", "capital": "런던", "flag": "🇬🇧", "attractions": ["대영 박물관", "타워 브리지", "빅벤", "스톤헨지"]},
    {"name": "독일", "region": "유럽", "capital": "베를린", "flag": "🇩🇪", "attractions": ["베를린 장벽", "노이슈반슈타인 성", "브란덴부르크 문", "쾰른 대성당"]},
    {"name": "이탈리아", "region": "유럽", "capital": "로마", "flag": "🇮🇹", "attractions": ["로마 콜로세움", "베니스 운하", "피렌체 대성당", "밀라노 대성당"]},
    {"name": "스페인", "region": "유럽", "capital": "마드리드", "flag": "🇪🇸", "attractions": ["사그라다 파밀리아", "알람브라 궁전", "구엘 공원", "세비야 대성당"]},
    {"name": "스위스", "region": "유럽", "capital": "베른", "flag": "🇨🇭", "attractions": ["마테호른", "융프라우요흐", "루체른 호수", "취리히 구시가지"]},
    {"name": "미국", "region": "아메리카", "capital": "워싱턴 D.C.", "flag": "🇺🇸", "attractions": ["자유의 여신상", "그랜드 캐니언", "옐로스톤 국립공원", "타임스 스퀘어"]},
    {"name": "캐나다", "region": "아메리카", "capital": "오타와", "flag": "🇨🇦", "attractions": ["나이아가라 폭포", "밴프 국립공원", "밴쿠버 스탠리 파크", "퀘벡 구시가지"]},
    {"name": "브라질", "region": "아메리카", "capital": "브라질리아", "flag": "🇧🇷", "attractions": ["구세주 그리스도상", "이구아수 폭포", "리우데자네이루 코파카바나", "아마존 우림"]},
    {"name": "이집트", "region": "아프리카", "capital": "카이로", "flag": "🇪🇬", "attractions": ["기자 피라미드", "룩소르 신전", "카이로 이집트 박물관", "아부심벨 신전"]},
    {"name": "남아프리카 공화국", "region": "아프리카", "capital": "프리토리아", "flag": "🇿🇦", "attractions": ["테이블 마운틴", "크루거 국립공원", "케이프타운 워터프런트", "희망봉"]},
    {"name": "모로코", "region": "아프리카", "capital": "라바트", "flag": "🇲🇦", "attractions": ["마라케시 제마 엘프나 광장", "셰프샤우엔", "페스 엘발리", "사하라 사막"]},
    {"name": "호주", "region": "오세아니아", "capital": "캔버라", "flag": "🇦🇺", "attractions": ["시드니 오페라 하우스", "그레이트 배리어 리프", "울루루", "멜버른 해안도로"]},
    {"name": "뉴질랜드", "region": "오세아니아", "capital": "웰링턴", "flag": "🇳🇿", "attractions": ["밀포드 사운드", "호비튼 마을", "퀸즈타운 와카티푸 호수", "로토루아 온천"]}
]

@st.cache_data
def get_database():
    db = {}
    for item in UN_193_RAW_DATA:
        if item["name"] not in db:
            db[item["name"]] = item
    return db

db = get_database()

# 헤더 영역
st.title("✈️ UN 회원국 세계 관광지 가이드")
st.caption(f"등록된 국가 총 {len(db)}개국 | 검색창에 국가명을 입력하거나 대륙별로 검색해보세요.")
st.write("---")

# 사이드바 필터
st.sidebar.header("🔍 검색 및 필터")
region_filter = st.sidebar.selectbox(
    "대륙 선택",
    ["전체", "아시아", "유럽", "아메리카", "아프리카", "오세아니아"]
)

search_query = st.text_input("찾고 싶은 국가 이름을 입력하세요 (예: 포르투갈, 대한민국, 프랑스)", "")

# 포르투갈 및 호날두 이스터에그 처리
clean_query = search_query.strip()
if "포르투갈" in clean_query or clean_query.lower() in ["portugal", "ronaldo", "호날두"]:
    st.markdown("### SIUUUU! 🔥 포르투갈 스페셜 에디션")
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg", caption="CR7 - 포르투갈의 전설", width=400)
    st.success("포르투갈 검색이 감지되었습니다! 아래 카드에서 상세 관광지를 확인하세요.")

# 필터링 로직
filtered_countries = []
for name, info in db.items():
    if region_filter != "전체" and info["region"] != region_filter:
        continue
    if clean_query and clean_query not in name and clean_query.lower() not in name.lower():
        if not ("포르투갈" in clean_query or clean_query.lower() in ["portugal", "ronaldo", "호날두"] and name == "포르투갈"):
            continue
    filtered_countries.append(info)

# 결과 출력 (박스 / 카드형 UI 적용)
st.write(f"검색 결과: 총 {len(filtered_countries)}개국")

# 2열 그리드로 박스 배치
cols = st.columns(2)
for idx, country in enumerate(filtered_countries):
    col = cols[idx % 2]
    with col:
        with st.container(border=True):
            st.markdown(f"### {country['flag']} {country['name']}")
            st.markdown(f"**📍 대륙:** {country['region']} &nbsp;&nbsp;|&nbsp;&nbsp; **🏛️ 수도:** {country['capital']}")
            st.markdown("**✨ 추천 관광지 리스트**")
            
            for spot in country['attractions']:
                st.markdown(f"- 🔸 {spot}")
