#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""site-026 초록 식물 보기 · 감성힐링 블로그 글 50편 생성"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "blog-posts.json"

POSTS = [
    {
        "id": "green-plant-viewing-complete-guide",
        "title": "초록 식물 보기 완벽 입문 — 정서 힐링의 시작",
        "summary": "잎을 천천히 바라보는 것만으로도 긴장이 풀립니다. 원리·효과·시작 3단계를 한눈에.",
        "category": "입문·가이드",
        "emoji": "🌿",
        "tags": ["입문", "식물힐링", "정서"],
        "date": "2026-07-10",
        "content": """<p class="article-lead">바쁜 하루 끝에 <strong>초록 잎 한 장</strong>을 천천히 바라보는 습관은, 마사지·호흡과 함께 쓰기 좋은 셀프케어입니다.</p>
<h2>왜 ‘보기’만으로도 도움이 될까</h2>
<p>녹색 시야는 시각적 휴식을 주고, 호흡을 자연스럽게 깊게 만듭니다. 강한 자극 없이 <em>정서</em>를 가라앉히는 데 적합해요.</p>
<h2>시작 3단계</h2>
<ol>
<li>창가·책상 식물 하나를 고른다</li>
<li>타이머 3분, 잎의 결·색만 본다</li>
<li>어깨를 내리고 코로 천천히 숨 쉰다</li>
</ol>
<p>마사지 전후 5분과 붙이면 이완 효과가 더 잘 느껴집니다. <a href="blog/plant-viewing-massage-combo.html">식물 보기+마사지</a>도 함께 읽어 보세요.</p>""",
    },
    {
        "id": "plant-viewing-5min-routine",
        "title": "하루 5분 초록 루틴 — 아침·점심·저녁",
        "summary": "바쁜 20~50대를 위한 짧은 식물 감상 루틴. 시간대별로 나눠 실천하기.",
        "category": "루틴",
        "emoji": "⏱️",
        "tags": ["루틴", "5분", "셀프케어"],
        "date": "2026-07-09",
        "content": """<p class="article-lead">길게 할 필요 없습니다. <strong>하루 5분</strong>만 초록에 시선을 두면 충분합니다.</p>
<ul>
<li><strong>아침</strong> — 창가 잎 2분, 물 한 잔</li>
<li><strong>점심</strong> — 책상 화분 1분, 눈 깜빡임</li>
<li><strong>저녁</strong> — 소파 옆 식물 2분, 어깨 풀기</li>
</ul>
<p>마사지 예약 전날에도 이 루틴으로 몸을 미리 이완해 두면 좋습니다.</p>""",
    },
    {
        "id": "plant-viewing-massage-combo",
        "title": "식물 보기 + 마사지 — 이완을 두 배로",
        "summary": "마사지 전후 초록 시야를 붙이면 정서·근육 이완이 이어집니다.",
        "category": "마사지·연계",
        "emoji": "💆",
        "tags": ["마사지", "이완", "웰니스"],
        "date": "2026-07-09",
        "content": """<p class="article-lead">마사지는 몸을, <strong>초록 식물 보기</strong>는 마음을 풀어 줍니다. 둘을 이어서 쓰면 셀프케어가 완성됩니다.</p>
<h2>추천 순서</h2>
<ol>
<li>마사지 전 3분 — 잎 바라보며 호흡</li>
<li>마사지·셀프 스트레칭</li>
<li>마사지 후 2분 — 같은 식물을 다시 보며 여운 남기기</li>
</ol>
<p>출장마사지·홈케어 전에도 창가에서 짧게 시작하면 긴장이 덜합니다.</p>""",
    },
    {
        "id": "desk-plant-office-healing",
        "title": "책상 위 작은 초록 — 직장인 눈·어깨 케어",
        "summary": "모니터 옆 화분 하나로 눈 피로와 정서 긴장을 낮추는 법.",
        "category": "직장·책상",
        "emoji": "🖥️",
        "tags": ["직장", "책상", "눈피로"],
        "date": "2026-07-08",
        "content": """<p class="article-lead">화면만 보다 보면 시선이 굳습니다. <strong>모니터 옆 작은 잎</strong>으로 시선을 옮기는 습관을 만드세요.</p>
<ul>
<li>50분 작업 → 1분 식물 보기 (20-20-20 규칙과 병행)</li>
<li>잎 끝·잎맥을 따라가며 눈 근육 풀기</li>
<li>어깨를 귀에서 멀리 내리기</li>
</ul>
<p>스킨십 마사지·목어깨 케어와도 잘 맞는 직장 루틴입니다.</p>""",
    },
    {
        "id": "morning-window-plant-view",
        "title": "아침 창가 식물 보기 — 하루를 부드럽게 열기",
        "summary": "알람 직후 3분. 커튼을 열고 초록을 먼저 보는 아침 루틴.",
        "category": "아침·루틴",
        "emoji": "🌅",
        "tags": ["아침", "창가", "루틴"],
        "date": "2026-07-08",
        "content": """<p class="article-lead">폰을 보기 전에 <strong>창가 초록</strong>을 먼저 보면, 하루의 정서 톤이 달라집니다.</p>
<ol>
<li>커튼 열기</li>
<li>잎에 닿는 빛 관찰 2분</li>
<li>심호흡 5회</li>
</ol>
<p>이후 가벼운 목·어깨 셀프마사지를 붙이면 몸이 더 잘 깨어납니다.</p>""",
    },
    {
        "id": "evening-plant-wind-down",
        "title": "저녁 식물 감상으로 하루 마무리",
        "summary": "수면 전 스크린 대신 초록. 정서 안정과 마사지 후 케어.",
        "category": "저녁·수면",
        "emoji": "🌙",
        "tags": ["저녁", "수면", "디톡스"],
        "date": "2026-07-07",
        "content": """<p class="article-lead">잠들기 전 피드는 각성을 올립니다. 대신 <strong>실내 식물</strong>을 3~5분 바라보세요.</p>
<p>조명만 살짝 낮추고, 잎의 그림자까지 천천히 따라가면 호흡이 깊어집니다. 마사지·족욕 직후에도 같은 순서로 마무리하면 좋아요.</p>""",
    },
    {
        "id": "leaf-texture-mindful-looking",
        "title": "잎맥·결 따라보기 — 마인드풀 식물 감상",
        "summary": "잎의 결을 따라가면 잡념이 줄어듭니다. 초보도 쉬운 관찰법.",
        "category": "마인드풀",
        "emoji": "🍃",
        "tags": ["마인드풀", "집중", "정서"],
        "date": "2026-07-07",
        "content": """<p class="article-lead">‘예쁘다’고만 느끼지 말고, <strong>잎맥 한 줄</strong>을 끝까지 따라가 보세요.</p>
<ul>
<li>중앙맥 → 곁맥 → 잎 끝</li>
<li>색이 진한 곳·연한 곳 구분</li>
<li>숨은 코로만, 입은 살짝 다물기</li>
</ul>
<p>명상이 부담스러울 때 쓰기 좋은 감성힐링 기법입니다.</p>""",
    },
    {
        "id": "beginner-easy-green-plants",
        "title": "초보 추천 초록 식물 — 보기용으로 키우기 쉬운 것",
        "summary": "스킨답서스, 산세베리아, 고무나무 등 감상에 좋은 입문 식물.",
        "category": "초보·추천",
        "emoji": "🪴",
        "tags": ["초보", "추천식물", "실내"],
        "date": "2026-07-06",
        "content": """<p class="article-lead">힐링용은 <strong>관리가 쉬운 초록</strong>이 먼저입니다. 시들면 정서에도 부담이 되니까요.</p>
<ul>
<li>스킨답서스 — 잎이 넓어 보기 좋음</li>
<li>산세베리아 — 직립형, 책상·코너</li>
<li>고무나무 — 큰 잎, 거실 포인트</li>
</ul>
<p>물·빛만 맞추면 매일 ‘초록 보기’ 루틴의 앵커가 됩니다.</p>""",
    },
    {
        "id": "stress-relief-green-gaze",
        "title": "스트레스 받을 때 초록 시선 돌리기",
        "summary": "회의·갈등 직후 2분. 식물을 보며 심박을 가라앉히는 법.",
        "category": "스트레스",
        "emoji": "😌",
        "tags": ["스트레스", "진정", "정서"],
        "date": "2026-07-06",
        "content": """<p class="article-lead">화가 난 직후엔 말로 풀기보다 <strong>시선부터</strong> 바꾸는 편이 빠릅니다.</p>
<ol>
<li>자리·창가로 이동</li>
<li>잎 하나에만 초점 90초</li>
<li>어깨·턱 힘 빼기</li>
</ol>
<p>이후 목 셀프마사지나 전문 마사지를 받으면 효과가 더 잘 남습니다.</p>""",
    },
    {
        "id": "plant-corner-home-wellness",
        "title": "집 안 식물 코너 만들기 — 힐링 존",
        "summary": "소파·창가에 작은 초록 존을 두면 마사지·휴식 공간이 됩니다.",
        "category": "공간·인테리어",
        "emoji": "🏡",
        "tags": ["공간", "홈케어", "웰니스"],
        "date": "2026-07-05",
        "content": """<p class="article-lead">특별한 인테리어가 필요 없습니다. <strong>의자 하나 + 식물 둘</strong>이면 힐링 존입니다.</p>
<ul>
<li>직사광선이 너무 세지 않은 창가</li>
<li>앉아서 잎이 눈높이에 오는 배치</li>
<li>폰은 다른 방에</li>
</ul>
<p>출장마사지 후 집에서 여운을 이어갈 때도 이 코너가 유용합니다.</p>""",
    },
    {
        "id": "commute-after-plant-reset",
        "title": "퇴근 후 첫 5분 — 현관·거실 식물로 리셋",
        "summary": "신발을 벗고 바로 초록을 보면 직장 긴장이 집에 덜 따라옵니다.",
        "category": "퇴근·리셋",
        "emoji": "🚪",
        "tags": ["퇴근", "리셋", "루틴"],
        "date": "2026-07-05",
        "content": """<p class="article-lead">현관이나 거실 입구에 <strong>잎이 큰 식물</strong>을 두면 ‘집 모드’ 스위치가 됩니다.</p>
<p>가방을 내려놓고 잎을 30초만 바라본 뒤, 손·어깨를 가볍게 풀어 보세요. 마사지 예약이 있는 날이라면 이 리셋이 몸을 미리 열어 줍니다.</p>""",
    },
    {
        "id": "selfcare-sunday-plant-hour",
        "title": "일요일 식물 한 시간 — 주간 셀프케어",
        "summary": "물주기·잎 닦기·감상까지. 주 1회 느린 식물 케어 타임.",
        "category": "셀프케어",
        "emoji": "☀️",
        "tags": ["일요일", "셀프케어", "루틴"],
        "date": "2026-07-04",
        "content": """<p class="article-lead">주말에 <strong>식물 케어 1시간</strong>을 잡으면, 몸과 공간 모두 정돈됩니다.</p>
<ol>
<li>잎 먼지 닦기 15분</li>
<li>물·분갈이 점검 20분</li>
<li>감상·호흡·가벼운 스트레칭 25분</li>
</ol>
<p>마사지·스파와 같은 ‘나를 돌보는 시간’으로 기록해 두세요.</p>""",
    },
    {
        "id": "green-color-psychology-healing",
        "title": "초록이 마음을 가라앉히는 이유 — 색과 정서",
        "summary": "녹색 시야와 안정감. 감성힐링형 식물 보기의 배경을 쉽게 정리.",
        "category": "정서·심리",
        "emoji": "💚",
        "tags": ["심리", "색채", "힐링"],
        "date": "2026-07-04",
        "content": """<p class="article-lead">초록은 자연·성장·휴식을 연상시켜 <strong>각성을 낮추는</strong> 색으로 자주 쓰입니다.</p>
<p>완벽한 이론보다 실전: 붉은·강한 화면 대신 잎을 보면 눈과 정서가 동시에 쉬어요. 마사지실의 차분한 조명·향과 같은 역할입니다.</p>""",
    },
    {
        "id": "phone-detox-plant-instead",
        "title": "스크롤 대신 잎 보기 — 디지털 디톡스",
        "summary": "잠들기 전·쉬는 시간에 폰 대신 식물을 보는 습관 만들기.",
        "category": "디지털디톡스",
        "emoji": "📵",
        "tags": ["디톡스", "습관", "수면"],
        "date": "2026-07-03",
        "content": """<p class="article-lead">‘금폰’이 어렵다면 <strong>대체 행동</strong>을 만드세요. 식물이 그 자리입니다.</p>
<ul>
<li>폰을 다른 방</li>
<li>타이머 5분, 잎만 보기</li>
<li>끝나면 물 한 잔·스트레칭</li>
</ul>
<p>수면·마사지 효과를 지키려면 블루라이트보다 초록 시야가 유리합니다.</p>""",
    },
    {
        "id": "bathroom-plant-spa-mood",
        "title": "욕실·세면대 옆 작은 초록 — 홈스파 무드",
        "summary": "샤워·족욕 전후 습도 좋은 곳에 작은 잎을 두면 스파 느낌이 납니다.",
        "category": "홈스파",
        "emoji": "🛁",
        "tags": ["스파", "욕실", "마사지"],
        "date": "2026-07-03",
        "content": """<p class="article-lead">습도를 좋아하는 작은 식물은 <strong>홈스파</strong> 분위기를 쉽게 만듭니다.</p>
<p>샤워 후 거울 대신 잎을 30초 보고, 목·어깨를 풀어 보세요. 전문 마사지 전날 컨디션 조절에도 좋습니다.</p>""",
    },
    {
        "id": "couple-plant-viewing-together",
        "title": "커플·가족과 함께 초록 보기",
        "summary": "말없이 같은 식물을 바라보는 3분. 관계 속 정서 케어.",
        "category": "관계·가족",
        "emoji": "👫",
        "tags": ["커플", "가족", "정서"],
        "date": "2026-07-02",
        "content": """<p class="article-lead">대화가 막힐 때, <strong>같은 잎</strong>을 함께 보는 것만으로도 분위기가 부드러워집니다.</p>
<p>주말 마사지·데이트 전 집에서 3분 루틴을 공유해 보세요. 감성힐링이 관계 케어로 이어집니다.</p>""",
    },
    {
        "id": "rainy-day-indoor-green",
        "title": "비 오는 날 실내 초록으로 기분 전환",
        "summary": "흐린 날씨엔 창밖 대신 잎의 생생한 녹색에 초점.",
        "category": "날씨·계절",
        "emoji": "🌧️",
        "tags": ["비", "실내", "기분"],
        "date": "2026-07-02",
        "content": """<p class="article-lead">회색 하늘이 기분을 누르는 날, <strong>잎의 선명한 초록</strong>이 대비가 됩니다.</p>
<p>조명을 살짝 밝히고 식물을 가까이 두세요. 따뜻한 차·가벼운 발마사지와 함께하면 더 좋습니다.</p>""",
    },
    {
        "id": "summer-heat-cool-green-view",
        "title": "더운 여름, 시원한 초록 시야로 열감 낮추기",
        "summary": "에어컨만 믿지 말고 시각적 쿨다운. 여름 식물 감상 팁.",
        "category": "계절·여름",
        "emoji": "🌴",
        "tags": ["여름", "쿨다운", "힐링"],
        "date": "2026-07-01",
        "content": """<p class="article-lead">더위는 몸뿐 아니라 <strong>정서 예민함</strong>도 올립니다. 시원한 잎·그늘진 코너를 활용하세요.</p>
<ul>
<li>직사광선 피한 자리</li>
<li>잎에 물 살짝 분무 후 감상</li>
<li>짧은 족욕·마사지와 병행</li>
</ul>""",
    },
    {
        "id": "winter-indoor-green-mood",
        "title": "겨울 실내 초록으로 처진 기분 올리기",
        "summary": "짧은 낮·건조한 공기. 겨울엔 잎 관리와 감상을 세트로.",
        "category": "계절·겨울",
        "emoji": "❄️",
        "tags": ["겨울", "실내", "무드"],
        "date": "2026-07-01",
        "content": """<p class="article-lead">겨울엔 바깥 녹지가 줄어 <strong>실내 식물</strong>의 역할이 커집니다.</p>
<p>가습기·물주기와 함께 매일 2분 감상을 유지하세요. 몸이 굳는 계절이라 마사지·스트레칭과도 잘 맞습니다.</p>""",
    },
    {
        "id": "plant-watering-as-meditation",
        "title": "물주기를 명상처럼 — 손끝 힐링",
        "summary": "물을 주는 동작 자체가 느린 셀프케어가 됩니다.",
        "category": "케어·명상",
        "emoji": "💧",
        "tags": ["물주기", "명상", "손"],
        "date": "2026-06-30",
        "content": """<p class="article-lead">물줄기를 보며 <strong>손과 호흡</strong>에만 집중해 보세요.</p>
<ol>
<li>물조리개 준비</li>
<li>흙이 젖는 소리·색 변화 관찰</li>
<li>잎을 한 바퀴 천천히 보기</li>
</ol>
<p>손 마사지·네일케어 전 워밍업으로도 좋습니다.</p>""",
    },
    {
        "id": "large-leaf-focus-exercise",
        "title": "큰 잎 하나에만 집중하기 — 시선 운동",
        "summary": "몬스테라·고무나무처럼 큰 잎은 초보 집중 연습에 최적.",
        "category": "연습·기법",
        "emoji": "🟢",
        "tags": ["집중", "큰잎", "기법"],
        "date": "2026-06-30",
        "content": """<p class="article-lead">작은 잎이 많으면 시선이 흩어집니다. <strong>큰 잎 하나</strong>만 고르세요.</p>
<p>가장자리를 시계 방향으로 천천히 따라가며 눈 근육을 풀어 줍니다. 모니터 피로·두통 완화 루틴에 넣기 좋아요.</p>""",
    },
    {
        "id": "aromatherapy-plant-combo",
        "title": "허브·향과 함께하는 초록 보기",
        "summary": "로즈마리·라벤더 등 향이 있는 식물로 감각을 더하기.",
        "category": "향·감각",
        "emoji": "🌸",
        "tags": ["아로마", "허브", "감각"],
        "date": "2026-06-29",
        "content": """<p class="article-lead">시각만으로도 충분하지만, <strong>은은한 향</strong>이 있으면 이완이 더 깊어집니다.</p>
<p>마사지 오일·디퓨저와 겹치지 않게, 허브는 가볍게만. 알레르기가 있으면 향 없는 잎 위주로.</p>""",
    },
    {
        "id": "post-massage-plant-aftercare",
        "title": "마사지 후 애프터케어 — 식물과 물 한 잔",
        "summary": "시술 직후 급하게 폰을 보지 말고 초록과 수분으로 여운 지키기.",
        "category": "마사지·애프터",
        "emoji": "🫖",
        "tags": ["애프터케어", "마사지", "수분"],
        "date": "2026-06-29",
        "content": """<p class="article-lead">마사지 직후 몸은 열려 있습니다. <strong>강한 자극(스크롤)</strong>보다 부드러운 시야가 맞습니다.</p>
<ul>
<li>미지근한 물</li>
<li>창가·로비 식물 2분</li>
<li>천천히 옷 입고 이동</li>
</ul>""",
    },
    {
        "id": "pre-massage-calm-with-plants",
        "title": "마사지 전 긴장 풀기 — 대기실·집에서 초록",
        "summary": "시술 전 몸이 굳어 있으면 효과가 반감됩니다. 식물로 미리 이완.",
        "category": "마사지·준비",
        "emoji": "🧘",
        "tags": ["준비", "긴장완화", "마사지"],
        "date": "2026-06-28",
        "content": """<p class="article-lead">예약 시간 10분 전, <strong>잎을 보며 어깨를 내리세요.</strong></p>
<p>대기실에 식물이 없다면 폰 배경을 초록 사진으로 바꿔도 임시 효과가 있습니다. 가능하면 실물이 더 좋아요.</p>""",
    },
    {
        "id": "neck-shoulder-plant-break",
        "title": "목·어깨 굳을 때 식물 브레이크",
        "summary": "거북목·승모근 긴장 사이사이, 시선 올리기와 초록 보기.",
        "category": "목어깨",
        "emoji": "🙆",
        "tags": ["목", "어깨", "스트레칭"],
        "date": "2026-06-28",
        "content": """<p class="article-lead">모니터보다 <strong>약간 높은 위치</strong>의 식물을 두면 자연스럽게 시선이 올라갑니다.</p>
<ol>
<li>턱 당기고 잎 보기 1분</li>
<li>귀·어깨 멀어지게 스트레칭</li>
<li>필요 시 전문 마사지</li>
</ol>""",
    },
    {
        "id": "eye-fatigue-green-rest",
        "title": "눈 피로에 초록 휴식 — 화면 중독 케어",
        "summary": "충혈·건조한 날엔 녹색 시야로 조절근을 쉬게 하기.",
        "category": "눈·피로",
        "emoji": "👀",
        "tags": ["눈피로", "화면", "휴식"],
        "date": "2026-06-27",
        "content": """<p class="article-lead">가까운 화면만 보면 눈 근육이 지칩니다. <strong>중간 거리의 잎</strong>을 바라보세요.</p>
<p>인공눈물·온찜질과 함께, 2시간마다 식물 1분 루틴을 권합니다.</p>""",
    },
    {
        "id": "anxiety-night-plant-light",
        "title": "불안한 밤, 은은한 조명과 식물",
        "summary": "수면 전 불안할 때 강한 불 대신 잎 실루엣으로 안정.",
        "category": "불안·수면",
        "emoji": "🕯️",
        "tags": ["불안", "밤", "수면"],
        "date": "2026-06-27",
        "content": """<p class="article-lead">불을 확 끄기 전, <strong>간접등과 식물 실루엣</strong>을 3분 바라보세요.</p>
<p>호흡이 고르면 침대로. 만성 불안·수면 문제는 전문가 상담이 우선입니다.</p>""",
    },
    {
        "id": "wfh-plant-meeting-reset",
        "title": "재택 회의 사이 초록 리셋 90초",
        "summary": "줌 백투백 일정 사이, 카메라 끄고 잎만 보기.",
        "category": "재택·업무",
        "emoji": "🏠",
        "tags": ["재택", "회의", "리셋"],
        "date": "2026-06-26",
        "content": """<p class="article-lead">회의가 이어지면 표정도 몸도 굳습니다. <strong>90초 초록</strong>으로 리셋하세요.</p>
<ul>
<li>카메라·마이크 오프</li>
<li>책상 식물에 시선</li>
<li>물 한 모금</li>
</ul>""",
    },
    {
        "id": "kids-plant-looking-habit",
        "title": "아이와 함께 잎 관찰하기",
        "summary": "아이 정서·집중력에도 도움이 되는 가벼운 식물 놀이.",
        "category": "육아·가족",
        "emoji": "🧒",
        "tags": ["아이", "관찰", "가족"],
        "date": "2026-06-26",
        "content": """<p class="article-lead">‘잎 색깔 찾기’ ‘새순 발견’ 같은 <strong>관찰 놀이</strong>로 함께하세요.</p>
<p>독성 식물은 손이 닿지 않게. 부모의 마사지·휴식 시간과 분리해 각자의 존을 지켜도 좋습니다.</p>""",
    },
    {
        "id": "senior-gentle-plant-viewing",
        "title": "시니어를 위한 부드러운 식물 감상",
        "summary": "눈·자세에 부담 없는 거리와 조명으로 초록 힐링.",
        "category": "시니어",
        "emoji": "🧓",
        "tags": ["시니어", "안전", "힐링"],
        "date": "2026-06-25",
        "content": """<p class="article-lead">의자에 앉아 <strong>눈높이 식물</strong>을 두는 것이 핵심입니다.</p>
<p>넘어질 위험 있는 화분은 피하고, 가벼운 손·발 마사지와 함께 짧은 시간부터.</p>""",
    },
    {
        "id": "travel-hotel-plant-photo-hack",
        "title": "여행·출장 중에도 초록 유지하는 법",
        "summary": "호텔에 식물이 없어도 공원·로비·사진으로 루틴 지키기.",
        "category": "여행·출장",
        "emoji": "✈️",
        "tags": ["여행", "출장", "루틴"],
        "date": "2026-06-25",
        "content": """<p class="article-lead">출장지에서도 <strong>로비 식물·근처 공원</strong>을 루틴에 넣으세요.</p>
<p>마사지·족욕 예약과 함께 ‘초록 10분’을 일정에 적어 두면 실천률이 올라갑니다.</p>""",
    },
    {
        "id": "balcony-green-morning-air",
        "title": "베란다 아침 공기와 초록",
        "summary": "환기 + 식물 보기로 하루를 여는 베란다 루틴.",
        "category": "베란다",
        "emoji": "🌤️",
        "tags": ["베란다", "환기", "아침"],
        "date": "2026-06-24",
        "content": """<p class="article-lead">가능하면 아침 <strong>베란다 문</strong>을 열고 잎과 공기를 함께 느껴 보세요.</p>
<p>미세먼지가 심한 날은 실내에서만. 스트레칭·가벼운 마사지 볼과 조합해도 좋습니다.</p>""",
    },
    {
        "id": "monstera-slow-looking-guide",
        "title": "몬스테라 천천히 보기 — 구멍·결 관찰",
        "summary": "인기 식물 몬스테라로 하는 감성 관찰 가이드.",
        "category": "식물별",
        "emoji": "🌴",
        "tags": ["몬스테라", "관찰", "감성"],
        "date": "2026-06-24",
        "content": """<p class="article-lead">구멍(페네스트레이션)의 모양을 따라가면 <strong>시선이 자연스럽게</strong> 느려집니다.</p>
<p>새 잎이 말려 나오는 과정도 좋은 관찰 포인트. 주 1회 사진을 남겨 변화를 기록해 보세요.</p>""",
    },
    {
        "id": "succulent-mini-desk-calm",
        "title": "다육·미니 화분으로 책상 진정 존",
        "summary": "공간이 좁아도 작은 초록이면 충분합니다.",
        "category": "미니·책상",
        "emoji": "🌵",
        "tags": ["다육", "미니", "책상"],
        "date": "2026-06-23",
        "content": """<p class="article-lead">큰 화분이 부담이면 <strong>다육 하나</strong>로 시작하세요.</p>
<p>형태가 또렷해 초보 관찰에 좋고, 물 주기도 간단합니다. 업무 스트레스 완충용으로 추천.</p>""",
    },
    {
        "id": "hanging-plant-eye-line",
        "title": "행잉 플랜트로 시선 올리기",
        "summary": "아래로만 보던 눈을 위로. 목 부담 줄이는 배치.",
        "category": "배치·시선",
        "emoji": "🪢",
        "tags": ["행잉", "시선", "목"],
        "date": "2026-06-23",
        "content": """<p class="article-lead">행잉 플랜트는 <strong>위를 보게</strong> 만들어 거북목 습관을 조금 깨 줍니다.</p>
<p>너무 높으면 목이 젖혀지니, 살짝 올려다보는 정도가 적당합니다.</p>""",
    },
    {
        "id": "plant-journal-mood-track",
        "title": "식물 일기 — 기분과 함께 기록하기",
        "summary": "오늘 본 잎, 오늘 기분. 감성힐링을 데이터처럼 쌓기.",
        "category": "기록·습관",
        "emoji": "📓",
        "tags": ["일기", "습관", "정서"],
        "date": "2026-06-22",
        "content": """<p class="article-lead">한 줄이면 됩니다. <em>「오늘 창가 3분, 기분 6→7」</em></p>
<p>마사지·운동 기록과 나란히 두면 셀프케어 패턴이 보입니다.</p>""",
    },
    {
        "id": "group-office-plant-culture",
        "title": "사무실 공유 식물로 팀 분위기 바꾸기",
        "summary": "공용 화분 하나로도 휴식 신호가 생깁니다.",
        "category": "직장·팀",
        "emoji": "🏢",
        "tags": ["사무실", "팀", "문화"],
        "date": "2026-06-22",
        "content": """<p class="article-lead">회의 테이블 옆 <strong>공용 식물</strong>은 ‘잠깐 쉬어도 된다’는 신호가 됩니다.</p>
<p>물주기 당번을 돌아가며 하면 가벼운 케어 루틴도 생깁니다.</p>""",
    },
    {
        "id": "foot-massage-plant-pairing",
        "title": "발마사지·족욕과 초록 시야 페어링",
        "summary": "발은 담그고 눈은 잎에. 하체 이완 + 정서 안정.",
        "category": "마사지·족욕",
        "emoji": "🦶",
        "tags": ["족욕", "발마사지", "페어링"],
        "date": "2026-06-21",
        "content": """<p class="article-lead">족욕 중 폰을 보면 각성이 올라갑니다. 대신 <strong>앞에 식물</strong>을 두세요.</p>
<p>15~20분 동안 잎만 바라보면 하체·정서가 함께 풀립니다.</p>""",
    },
    {
        "id": "scalp-care-green-ambiance",
        "title": "두피·헤드스파 분위기를 집에서 — 초록 배경",
        "summary": "셀프 두피 마사지할 때 시야에 초록을 두면 이완이 깊어집니다.",
        "category": "헤드스파",
        "emoji": "🧴",
        "tags": ["두피", "헤드스파", "셀프"],
        "date": "2026-06-21",
        "content": """<p class="article-lead">거울만 보면 긴장하기 쉽습니다. <strong>옆이나 앞의 식물</strong>을 배경으로 두피 마사지를 해 보세요.</p>""",
    },
    {
        "id": "breathing-with-leaf-rhythm",
        "title": "잎이 흔들리는 리듬에 맞춰 숨쉬기",
        "summary": "미풍에 흔들리는 잎을 메트로놈처럼 쓰는 호흡법.",
        "category": "호흡·연계",
        "emoji": "🌬️",
        "tags": ["호흡", "리듬", "이완"],
        "date": "2026-06-20",
        "content": """<p class="article-lead">선풍기·창문을 약하게 열고, <strong>잎이 한 번 흔들릴 때</strong> 들이쉬고 내쉬세요.</p>
<p>복식호흡·마사지 전 워밍업으로 쓰기 좋습니다.</p>""",
    },
    {
        "id": "color-contrast-green-white",
        "title": "흰 벽·초록 잎 대비로 시선 정리",
        "summary": "배경이 단순할수록 잎이 또렷해 감상이 쉬워집니다.",
        "category": "배치·디자인",
        "emoji": "⬜",
        "tags": ["배치", "대비", "시선"],
        "date": "2026-06-20",
        "content": """<p class="article-lead">패턴 벽지 앞보다 <strong>단색 벽</strong> 앞이 관찰에 유리합니다.</p>
<p>힐링 존은 시각 노이즈를 줄이는 것이 핵심이에요.</p>""",
    },
    {
        "id": "plant-sound-silence-combo",
        "title": "고요 + 초록 — 소리 없는 힐링",
        "summary": "음악이 부담될 때, 침묵과 식물만으로도 충분합니다.",
        "category": "감각·침묵",
        "emoji": "🔇",
        "tags": ["침묵", "감각", "힐링"],
        "date": "2026-06-19",
        "content": """<p class="article-lead">항상 ASMR·음악이 필요하지 않습니다. <strong>잎과 고요</strong>만으로도 정서가 가라앉습니다.</p>
<p>마사지실의 조용한 분위기와 같은 원리입니다.</p>""",
    },
    {
        "id": "21-day-green-gaze-challenge",
        "title": "21일 초록 보기 챌린지",
        "summary": "매일 3분. 습관이 될 때까지의 간단한 챌린지 보드.",
        "category": "챌린지",
        "emoji": "📅",
        "tags": ["챌린지", "21일", "습관"],
        "date": "2026-06-19",
        "content": """<p class="article-lead">달력에 동그라미만 쳐도 됩니다. <strong>21일간 하루 3분</strong>.</p>
<ul>
<li>1주 — 같은 식물, 같은 시간</li>
<li>2주 — 아침·저녁 분리</li>
<li>3주 — 마사지·스트레칭과 페어링</li>
</ul>""",
    },
    {
        "id": "holistic-plant-wellness-hub",
        "title": "식물·마사지·호흡을 잇는 홀리스틱 허브",
        "summary": "초록 보기를 중심으로 웰니스 루틴을 한곳에 모으는 법.",
        "category": "허브·종합",
        "emoji": "✨",
        "tags": ["홀리스틱", "웰니스", "허브"],
        "date": "2026-06-18",
        "content": """<p class="article-lead">이 사이트는 <strong>초록 식물 보기</strong>를 축으로, 마사지·힐링·셀프케어 정보를 연결합니다.</p>
<p>가이드·팁·FAQ를 함께 보면 나만의 루틴을 만들기 쉽습니다.</p>""",
    },
    {
        "id": "lunch-break-park-or-plant",
        "title": "점심시간 공원 vs 실내 식물 — 선택 가이드",
        "summary": "날씨·체력에 따라 바깥 녹지와 실내 초록을 고르는 법.",
        "category": "점심·야외",
        "emoji": "🌳",
        "tags": ["점심", "공원", "선택"],
        "date": "2026-06-18",
        "content": """<p class="article-lead">걸을 힘이 있으면 공원, 없으면 <strong>실내 잎 5분</strong>이 정답입니다.</p>
<p>둘 다 ‘초록 시야’라는 점은 같습니다. 완벽보다 지속.</p>""",
    },
    {
        "id": "pet-safe-plants-viewing",
        "title": "반려동물이 있을 때 안전한 감상 식물",
        "summary": "독성 없는 잎 위주로. 보기용 배치와 안전.",
        "category": "반려동물",
        "emoji": "🐾",
        "tags": ["펫", "안전", "배치"],
        "date": "2026-06-17",
        "content": """<p class="article-lead">고양·강아지가 있다면 <strong>독성 식물</strong>은 피하거나 손이 닿지 않게.</p>
<p>감상은 선반·행잉으로, 바닥은 안전한 종류만. 마사지·홈케어 공간과 분리해도 좋습니다.</p>""",
    },
    {
        "id": "night-shift-green-reset",
        "title": "교대·야근 후 초록으로 생체리듬 달래기",
        "summary": "불규칙 근무에도 짧은 식물 루틴으로 정서 균형 지키기.",
        "category": "야근·교대",
        "emoji": "🌃",
        "tags": ["야근", "교대", "리듬"],
        "date": "2026-06-17",
        "content": """<p class="article-lead">귀가 직후 스크린 대신 <strong>잎 3분</strong>. 그다음 샤워·가벼운 마사지.</p>
<p>수면 시간이 들쑥날쑥해도 ‘고정 루틴’ 하나가 있으면 정서가 덜 흔들립니다.</p>""",
    },
    {
        "id": "plant-gift-wellness-message",
        "title": "식물 선물로 전하는 웰니스 메시지",
        "summary": "마사지 이용권과 함께 작은 화분을 선물하는 아이디어.",
        "category": "선물·관계",
        "emoji": "🎁",
        "tags": ["선물", "웰니스", "관계"],
        "date": "2026-06-16",
        "content": """<p class="article-lead">‘쉬어라’는 말 대신 <strong>작은 초록</strong>을 건네 보세요.</p>
<p>관리법 한 줄 + 이 사이트 가이드 링크를 적어 주면 실용적입니다.</p>""",
    },
    {
        "id": "mindful-shopping-plant-pick",
        "title": "식물 고를 때 마음챙김 쇼핑",
        "summary": "충동구매 대신, 매일 볼 수 있는 잎인지 기준으로.",
        "category": "구매·선택",
        "emoji": "🛒",
        "tags": ["구매", "선택", "마인드풀"],
        "date": "2026-06-16",
        "content": """<p class="article-lead">예쁜 꽃보다 <strong>매일 볼 초록</strong>이 힐링용으로는 낫습니다.</p>
<ul>
<li>집 빛 조건에 맞는가</li>
<li>눈높이에 둘 수 있는가</li>
<li>물주기를 감당할 수 있는가</li>
</ul>""",
    },
    {
        "id": "green-viewing-info-hub",
        "title": "초록 식물 보기 정보 허브 — 이 사이트를 쓰는 법",
        "summary": "가이드·팁·FAQ·블로그로 나누어진 식물 힐링 허브 안내.",
        "category": "허브·안내",
        "emoji": "🗺️",
        "tags": ["허브", "안내", "정보"],
        "date": "2026-06-15",
        "content": """<p class="article-lead">여기는 <strong>초록 식물 보기</strong> 관련 정보 허브입니다.</p>
<ul>
<li><a href="../guide.html">가이드</a> — 입문·원리</li>
<li><a href="../tips.html">팁</a> — 상황별 실전</li>
<li><a href="../faq.html">FAQ</a> — 자주 묻는 질문</li>
<li><a href="../blog.html">블로그</a> — 주제별 글</li>
</ul>
<p>마사지·웰니스에 관심 있는 20~50대 독자를 위해 친근하고 실용적으로 정리했습니다.</p>""",
    },
]

for p in POSTS:
    p.setdefault("author", "식물")
    p.setdefault("published", True)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({"posts": POSTS}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {len(POSTS)} posts -> {OUT}")
