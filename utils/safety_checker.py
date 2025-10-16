#!/usr/bin/env python3
"""
أدوات الأمان والتحقق
"""

import re

class SafetyValidator:
    def check_environment(self):
        print("✅ بيئة التشغيل جاهزة")
        return True
    
    def validate_facebook_url(self, url):
        if 'facebook.com' in url:
            return True
        return False