import json
import os
from pytrends.request import TrendReq

def get_trends_for_niche():
    """
    Fetches trending searches from Google Trends for India,
    falls back to US if unavailable, and combines with local JSON trends.
    """
    pytrends = TrendReq(hl='en-US', tz=330)  # tz=330 for IST
    google_trends = []

    # Try India first
    try:
        trending_searches_df = pytrends.trending_searches(pn='IN')  # India
        google_trends = trending_searches_df[0].tolist()
    except Exception as e:
        print(f"⚠️ Error fetching India trends: {e}")
        # Fallback to US
        try:
            trending_searches_df = pytrends.trending_searches(pn='united_states')
            google_trends = trending_searches_df[0].tolist()
        except Exception as e2:
            print(f"⚠️ Error fetching fallback US trends: {e2}")
            google_trends = []

    # Read local trends
    try:
        trends_file = os.path.join("ai", "trends", "trends.json")
        with open(trends_file, "r") as f:
            local_trends = json.load(f)
        local_trends_list = [t["trend"] for t in local_trends if t["popularity"] > 70]
    except FileNotFoundError:
        local_trends_list = []

    # Combine and remove duplicates
    combined_trends = list(dict.fromkeys(local_trends_list + google_trends))
    return combined_trends


# For manual testing
if __name__ == "__main__":
    trends = get_trends_for_niche()
    print("📈 Popular trends:", trends)
