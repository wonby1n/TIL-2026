import requests
import json
from datetime import datetime, timedelta

def get_yesterday_solved(bj_id):
    """특정 아이디의 어제 푼 문제 개수를 가져옵니다."""
    # KST 기준 어제 날짜 구하기
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    url = f"https://solved.ac/api/v3/user/show?handle={bj_id}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # 실무적 팁: Solved.ac는 'solvedCount' 총합만 제공하므로, 
            # 일일 변동량을 정확히 계산하려면 매일 데이터를 저장하는 DB가 필요합니다.
            # 여기서는 '총 해결 수'를 출력하도록 구성했습니다.
            data = response.json()
            return data.get('solvedCount', 0)
    except:
        return None
    return 0

def send_to_mattermost():
    webhook_url = "https://meeting.ssafy.com/hooks/59f38t8jk3yjmmwciq98gn4a4e"
    ids = ["05dos1211", "chicken82", "ehtm75", "hometpgus", "kscheol25", 
           "kyo181", "skadbswnk", "tjfls295", "yoonix", "dudcjf1231"]
    
    report = "### 🏆 오늘의 백준 스터디 현황 리포트\n"
    report += f"**날짜**: {datetime.now().strftime('%Y-%m-%d')} 09:00\n\n"
    
    for bj_id in ids:
        count = get_yesterday_solved(bj_id)
        status = f"✅ {count}문제 해결 중" if count is not None else "❌ 확인 불가"
        report += f"- **{bj_id}**: {status}\n"
    
    report += "\n---\n> **\"오늘도 한 문제, 내일은 한 걸음 더!\"** 💪"

    payload = {"text": report}
    requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

if __name__ == "__main__":
    send_to_mattermost()