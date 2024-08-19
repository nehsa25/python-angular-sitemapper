import enum


class SitemapItem:
    class Frequency(enum.Enum):
        ALWAYS = "always"
        HOURLY = "hourly"
        DAILY = "daily"
        WEEKLY = "weekly"
        MONTHLY = "monthly"
        YEARLY = "yearly"
        NEVER = "never"
        
    loc: str = ""
    lastmod: float = 0
    changefreq: Frequency = Frequency.MONTHLY
    priority: float = 0 # 0.0 to 1.0
    full_path: str = ""
    