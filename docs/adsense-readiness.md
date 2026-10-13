# 애드센스 심사 준비 작업 기록

작성일: 2026-10-13
대상: wspace.ai.kr 전체(홈과 서브도메인 4개)

## 목적

Google AdSense 심사를 통과할 수 있도록 다섯 사이트의 정책 페이지, 사이트 간 이동, 페이지 설명 글, 검색엔진용 파일을 갖춘다. 애드센스는 루트 도메인(`wspace.ai.kr`) 단위로 심사하고, 심사관은 홈에서 출발해 링크를 따라 서브도메인까지 본다.

## 사이트 구성

| 주소 | 내용 | 저장소 | 배포 |
|---|---|---|---|
| https://www.wspace.ai.kr | 홈, 정책 페이지 | chrisjo-dev/wspace-home | GitHub Pages(main 루트) |
| https://read.wspace.ai.kr | 매일 외국어 읽기 | chrisjo-dev/english-reading | GitHub Pages(main 루트), 페이지는 Actions가 생성 |
| https://blog.wspace.ai.kr | 기술 블로그(Astro, Notion 동기화) | chrisjo-dev/notion-blog | Actions 배포(매일 18:00 KST) |
| https://util.wspace.ai.kr | BrowserTools(정적 HTML 27종) | chrisjo-dev/utile | GitHub Pages(main 루트) |
| https://brain.wspace.ai.kr | Brain Training(Vite, React, PWA) | chrisjo-dev/card-memory-game | Actions 배포(main push) |

## 공통으로 한 일

- **정책 페이지 3개를 홈에 만들고 모든 사이트에서 연결했다.**
  - 개인정보처리방침: https://www.wspace.ai.kr/privacy/
  - 소개: https://www.wspace.ai.kr/about/
  - 연락처: https://www.wspace.ai.kr/contact/
- **다섯 사이트의 모든 페이지 하단에 같은 링크를 넣었다.** wspace 홈, 소개, 개인정보처리방침, 연락처. 블로그 영어판은 Home, About, Privacy, Contact로 표기한다.
- 사이트마다 `robots.txt`와 사이트맵을 갖췄다.
- 사이트마다 404 페이지를 두었다. 브레인은 앱 구조상 없다.
- 운영자 표기는 "Chris Jo", 연락 이메일은 `wonsang.dev@gmail.com`이다.

## 사이트별 작업

### 홈 (wspace-home)

| 커밋 | 내용 |
|---|---|
| `c9decc3` | 개인정보처리방침, 소개, 연락처 페이지 추가. 공통 스타일 `style.css`, `robots.txt`, `sitemap.xml`, `404.html` 추가 |
| 같은 커밋 | 홈 화면 보강. 사이트 소개 문단, 서비스 카드 4개, "오늘의 외국어 지문", "최근 블로그 글 5개" 섹션 |
| 같은 커밋 | `tools/update_recent.py`와 `.github/workflows/update.yml`. 하루 두 번(08:17, 18:37 KST) 읽기 사이트 목록과 블로그 RSS를 읽어 홈의 최근 항목을 갱신한다. 60일 무활동으로 예약 실행이 꺼지지 않도록 실행마다 다시 켠다 |

개인정보처리방침에 담은 내용은 다음과 같다.
- 적용 범위
- 뉴스레터 이메일과 구독 언어(Buttondown 위탁)
- 블로그 댓글(giscus, GitHub)
- 브라우저 저장소 사용(BrowserTools, Brain Training)
- GitHub Pages 접속 기록과 외부 글꼴
- **Google AdSense 광고 쿠키 고지와 맞춤 광고 해제 방법** (Google 광고 설정, aboutads.info, Google 파트너 사이트 정책 링크)
- 보관과 파기, 이용자 권리, 아동, 변경, 문의

### 매일 외국어 읽기 (english-reading)

| 커밋 | 내용 |
|---|---|
| `152c32f` | 언어 첫 화면(`/en/`, `/ja/`)을 지문 목록으로 바꾸고, 첫 화면 카드가 목록으로 가게 함 |
| `8f5ac32` | 모든 페이지(첫 화면, 목록, 날짜 페이지, 주간 복습)에 공통 하단 추가 |
| 같은 커밋 | canonical 주소 지정. `/en/archive/`는 `/en/`을 대표 주소로 둬 중복 페이지 문제를 없앰 |
| 같은 커밋 | `publish.py`가 `sitemap.xml`과 `robots.txt`를 매번 다시 만든다(언어 목록, 날짜 페이지, 주간 복습 포함) |
| 같은 커밋 | `404.html` 추가 |

### 블로그 (notion-blog)

| 커밋 | 내용 |
|---|---|
| `2a89f0b`, `d8bc1d2` | `blog.wspace.ai.kr` 이전. Astro `base: '/notion-blog'` 제거, 코드와 Notion 동기화 스크립트에 박힌 옛 경로 52개 파일 정리 |
| `22fa3d8` | 배포 워크플로에 "Keep schedule alive" 단계 추가. 2026-08부터 60일 무활동으로 자동 배포가 꺼져 있던 문제를 막음 |
| `d8536df` | 공통 하단(한국어와 영어 분기), 홈 제목을 "Blog"에서 "Chris Jo 기술 블로그"(영어 "Chris Jo Tech Blog")로 변경, 홈 설명 문구, 404 페이지 추가, 깨진 `favicon.svg` 링크 제거 |

### BrowserTools (utile)

| 커밋 | 내용 |
|---|---|
| `5a2daa3` | 첫 화면에 소개 문단과 설명 문구(meta description) 추가 |
| 같은 커밋 | 도구 27개 페이지마다 고유 설명 문구와 "이 도구는" 안내(기능, 사용법, 파일이나 카메라를 기기 안에서 처리한다는 안내) 추가 |
| 같은 커밋 | 공통 하단, `robots.txt`, `sitemap.xml`(28개 주소), `404.html` 추가 |

### Brain Training (card-memory-game)

| 커밋 | 내용 |
|---|---|
| `7fc4ef1` | `brain.wspace.ai.kr` 이전. Vite `base`를 `/`로 변경 |
| `da03619` | 설명 문구와 OG 태그, 첫 화면에 "게임 소개, 하는 방법" 섹션(카드 메모리, N-Back, 역방향 스팬 규칙, 기록은 브라우저에만 저장), 공통 하단, `robots.txt`, `sitemap.xml` 추가. 테스트 26개와 빌드 통과 |

## 점검 결과 (2026-10-13 배포 후)

| 항목 | www | read | blog | util | brain |
|---|---|---|---|---|---|
| HTTPS(정식 인증서, 강제) | 정상 | 정상 | 정상 | 정상 | 정상 |
| 정책 페이지 하단 링크 | 있음 | 있음 | 있음 | 있음 | 있음(앱이 그림) |
| robots.txt | 200 | 200 | 200 | 200 | 200 |
| 사이트맵 | 200 | 200 | 200 | 200 | 200 |
| meta description | 있음 | 있음 | 있음 | 있음 | 있음 |
| http 혼합 콘텐츠 | 없음 | 없음 | 없음(148쪽 확인) | 없음 | 없음 |

## 남은 일

### 운영자가 직접 할 일
1. **Google Search Console 등록:** `wspace.ai.kr`을 "도메인" 속성으로 추가하고, 안내하는 TXT 레코드를 가비아 DNS에 넣어 소유를 확인한다. 그다음 사이트맵 5개를 제출한다.
   - https://www.wspace.ai.kr/sitemap.xml
   - https://read.wspace.ai.kr/sitemap.xml
   - https://blog.wspace.ai.kr/sitemap-index.xml
   - https://util.wspace.ai.kr/sitemap.xml
   - https://brain.wspace.ai.kr/sitemap.xml
2. **애드센스 신청:** 사이트 주소는 `wspace.ai.kr`(루트 도메인)으로 넣는다. 신청 화면이 주는 확인 코드(메타 태그 또는 ads.txt)를 받으면 홈 저장소에 넣는다.
3. **승인 뒤 ads.txt:** 게시자 ID가 나오면 다섯 사이트 루트에 `ads.txt`를 둔다.

### 신청 시점 권장
- 매일 외국어 읽기는 지문이 아직 적다(영어 3편, 일본어 1편). 2~3주 쌓인 뒤 신청하면 "내용이 적은 사이트" 판정 위험이 줄어든다.
- 블로그는 한국어 글 53편이 있어 가장 강한 근거다.

### 알려진 위험
- 외국어 읽기 지문과 블로그 영어판은 AI 도구로 만든다. 소개 페이지에 "사실과 출처를 확인한 뒤 올린다"는 원칙을 적어 두었지만, 대량 자동 생성 콘텐츠로 보일 위험은 남아 있다.
- Brain Training은 게임 앱이라 글 분량이 적다. 승인에 결정적이지는 않지만 광고를 붙일 때는 게임 화면을 방해하지 않게 배치해야 한다.

## 신청 기록

- 2026-10-13: 애드센스 검토 요청. 사이트 `wspace.ai.kr`, 게시자 ID `ca-pub-2339195232447097`.
- 같은 날 다섯 사이트 모든 페이지 `<head>`에 사이트 코드(adsbygoogle.js)를, 각 사이트 루트에 `ads.txt`(`google.com, pub-2339195232447097, DIRECT, f08c47fec0942fa0`)를 넣었다.
  - 홈 `690cd79`, 읽기 `ac394e6`, 블로그 `1b2a6f4`, 유틸 `92905f6`, 브레인 `fc1d67c`
- 같은 날 외국어 지문을 과거 날짜로 보충해 영어 10편, 일본어 10편을 맞췄다(`908608a`). 모든 편에 음성이 있다.
- 승인 뒤 할 일: 광고 단위를 만들어 위치별로 배치(외국어 읽기는 지문과 주요 단어 사이, 블로그는 본문 중간과 끝, 유틸은 도구 아래, 브레인은 게임 목록 아래). 세금 정보(W-8BEN) 제출.
