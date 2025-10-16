#!/usr/bin/env python3
"""
نظام إدارة الملفات والتقارير
"""

import json
from datetime import datetime
from pathlib import Path

class ReportGenerator:
    def __init__(self):
        self.base_dir = Path.home() / "SocialMapperPro"
        self.reports_dir = self.base_dir / "reports"
        self.setup_directories()
    
    def setup_directories(self):
        self.reports_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_family_report(self, results, father_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"family_{father_name}_{timestamp}.txt"
        report_path = self.reports_dir / filename
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"تقرير عائلة: {father_name}\n")
            f.write(f"النتائج: {len(results)}\n\n")
            
            for result in results:
                f.write(f"الاسم: {result['name']}\n")
                f.write(f"الرابط: {result['url']}\n")
                f.write(f"النوع: {result['type']}\n")
                f.write("-" * 40 + "\n")
        
        return str(report_path)
    
    def generate_person_report(self, profile_data, username):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"person_{username}_{timestamp}.txt"
        report_path = self.reports_dir / filename
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"تقرير شخصي: {username}\n")
            f.write(f"الأصدقاء: {profile_data.get('friends_count', 0)}\n")
            f.write(f"المنشورات: {profile_data.get('posts_count', 0)}\n")
        
        return str(report_path)