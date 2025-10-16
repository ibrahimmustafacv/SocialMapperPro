#!/usr/bin/env python3
"""
برنامج التثبيت - SocialMapper Pro
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class SocialMapperInstaller:
    def __init__(self):
        self.system = platform.system().lower()
        self.requirements = [
            'selenium==4.15.0',
            'requests==2.31.0', 
            'beautifulsoup4==4.12.2',
            'colorama==0.4.6',
            'blessed==1.20.0',
            'webdriver-manager==4.0.1',
            'urllib3==2.1.0',
            'lxml==4.9.3',
            'python-dateutil==2.8.2'
        ]
    
    def run_installation(self):
        """تشغيل عملية التثبيت"""
        print("🚀 بدء تثبيت SocialMapper Pro...\n")
        
        steps = [
            ("فحص النظام", self.check_system),
            ("تثبيت المتطلبات", self.install_requirements),
            ("تهيئة المجلدات", self.setup_directories),
            ("تحميد متصفح Firefox", self.setup_firefox),
            ("التحقق النهائي", self.final_check)
        ]
        
        for step_name, step_func in steps:
            print(f"\n📦 {step_name}...")
            if not step_func():
                print(f"❌ فشل في: {step_name}")
                return False
            print(f"✅ اكتمل: {step_name}")
        
        print("\n🎉 تم التثبيت بنجاح!")
        print("💻 لتشغيل الأداة: python3 main.py")
        return True
    
    def check_system(self):
        """فحص متطلبات النظام"""
        print(f"   • النظام: {platform.system()} {platform.release()}")
        print(f"   • Python: {platform.python_version()}")
        
        if self.system not in ['linux', 'darwin']:
            print("   ⚠️  التثبيت على Windows يحتاج إعدادات إضافية")
        
        return True
    
    def install_requirements(self):
        """تثبيت المكتبات المطلوبة"""
        try:
            for package in self.requirements:
                print(f"   • تثبيت {package}...")
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install', package
                ])
            return True
        except subprocess.CalledProcessError as e:
            print(f"   ❌ خطأ في تثبيت المكتبات: {e}")
            return False
    
    def setup_directories(self):
        """إنشاء المجلدات الهيكلية"""
        try:
            directories = [
                'core',
                'ui', 
                'utils',
                'outputs/reports',
                'outputs/logs',
                'config'
            ]
            
            for directory in directories:
                Path(directory).mkdir(parents=True, exist_ok=True)
                print(f"   • تم إنشاء: {directory}")
            
            return True
        except Exception as e:
            print(f"   ❌ خطأ في إنشاء المجلدات: {e}")
            return False
    
    def setup_firefox(self):
        """إعداد متصفح Firefox"""
        try:
            from webdriver_manager.firefox import GeckoDriverManager
            driver_path = GeckoDriverManager().install()
            print(f"   • تم تثبيت GeckoDriver: {driver_path}")
            return True
        except Exception as e:
            print(f"   ❌ خطأ في إعداد Firefox: {e}")
            return False
    
    def final_check(self):
        """التحقق النهائي"""
        try:
            import selenium
            import requests
            import colorama
            from webdriver_manager.firefox import GeckoDriverManager
            
            print("   ✅ جميع المكتبات مثبتة بشكل صحيح")
            
            required_dirs = ['core', 'ui', 'utils', 'outputs/reports']
            for dir_path in required_dirs:
                if not Path(dir_path).exists():
                    print(f"   ❌ مجلد {dir_path} غير موجود")
                    return False
            
            print("   ✅ الهيكل المعد صحيح")
            return True
            
        except ImportError as e:
            print(f"   ❌ خطأ في استيراد المكتبات: {e}")
            return False

if __name__ == "__main__":
    installer = SocialMapperInstaller()
    
    if installer.run_installation():
        print("\n🎊 SocialMapper Pro جاهز للاستخدام!")
        print("\n📚 لبدء الاستخدام:")
        print("   1. cd SocialMapperPro")
        print("   2. python3 main.py")
        print("\n⚠️  تذكر: هذه الأداة للأغراض التعليمية فقط")
    else:
        print("\n❌ فشل التثبيت! راجع الأخطاء أعلاه.")
        sys.exit(1)