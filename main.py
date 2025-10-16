#!/usr/bin/env python3
"""
SocialMapper Pro - Advanced OSINT Framework
الإصدار التعليمي الكامل
"""

import os
import sys
import time
from pathlib import Path

# إضافة المسارات للنظام
sys.path.append(str(Path(__file__).parent))

from core.facebook_scraper import FacebookScraper
from core.instagram_scraper import InstagramScraper
from ui.terminal_gui import MainInterface
from utils.safety_checker import SafetyValidator
from utils.file_manager import ReportGenerator

class SocialMapperPro:
    def __init__(self):
        self.version = "2.0.0"
        self.author = "OSINT Learner"
        self.ui = MainInterface()
        self.validator = SafetyValidator()
        self.reporter = ReportGenerator()
        
        # تهيئة المحركات
        self.fb_scraper = FacebookScraper()
        self.ig_scraper = InstagramScraper()
        
    def initialize_system(self):
        """تهيئة النظام بالكامل"""
        self.ui.show_banner()
        self.validator.check_environment()
        self.reporter.setup_directories()
        
    def shutdown_system(self):
        """إغلاق النظام بأمان"""
        self.ui.show_message("info", "جاري حفظ البيانات والإغلاق...")
        self.reporter.cleanup_temp_files()
        self.ui.show_message("success", "تم الإغلاق بأمان!")
        
    def run(self):
        """تشغيل النظام الرئيسي"""
        try:
            self.initialize_system()
            
            while True:
                choice = self.ui.main_menu()
                
                if choice == "1":
                    self.facebook_operations()
                elif choice == "2":
                    self.instagram_operations()
                elif choice == "3":
                    self.system_settings()
                elif choice == "4":
                    break
                else:
                    self.ui.show_message("error", "خيار غير صحيح!")
                    
        except KeyboardInterrupt:
            self.ui.show_message("warning", "تم إيقاف التشغيل بواسطة المستخدم")
        except Exception as e:
            self.ui.show_message("error", f"خطأ في النظام: {str(e)}")
        finally:
            self.shutdown_system()
    
    def facebook_operations(self):
        """عمليات فيسبوك المتكاملة"""
        fb_choice = self.ui.facebook_menu()
        
        if fb_choice == "1":
            self.search_by_father_name()
        elif fb_choice == "2":
            self.search_specific_person()
        elif fb_choice == "3":
            self.advanced_facebook_scan()
    
    def search_by_father_name(self):
        """البحث المتقدم عن الأبناء من اسم الأب"""
        try:
            # الحصول على البيانات من المستخدم
            target_data = self.ui.get_facebook_target()
            father_name = self.ui.get_father_name()
            
            # التحقق الأمني
            if not self.validator.validate_facebook_url(target_data['url']):
                self.ui.show_message("error", "رابط فيسبوك غير صحيح!")
                return
                
            # بدء عملية المسح
            self.ui.show_scan_progress("جاري البحث عن الأبناء...")
            
            # التنفيذ الفعلي
            results = self.fb_scraper.comprehensive_family_search(
                target_data['url'], 
                father_name,
                callback=self.ui.update_progress
            )
            
            # حفظ النتائج
            if results:
                report_path = self.reporter.generate_family_report(results, father_name)
                self.ui.show_results_summary(results, report_path)
            else:
                self.ui.show_message("warning", "لم يتم العثور على نتائج")
                
        except Exception as e:
            self.ui.show_message("error", f"خطأ في البحث: {str(e)}")
    
    def search_specific_person(self):
        """البحث المتقدم عن شخص معين"""
        try:
            username = self.ui.get_username()
            
            self.ui.show_scan_progress(f"جمع معلومات عن {username}...")
            
            # جمع البيانات الشاملة
            profile_data = self.fb_scraper.get_comprehensive_profile(
                username,
                include_friends=True,
                include_posts=True,
                include_comments=True
            )
            
            if profile_data:
                report_path = self.reporter.generate_person_report(profile_data, username)
                self.ui.show_person_report(profile_data, report_path)
            else:
                self.ui.show_message("warning", "لم يتم العثور على بيانات الملف الشخصي")
                
        except Exception as e:
            self.ui.show_message("error", f"خطأ في جمع البيانات: {str(e)}")
    
    def advanced_facebook_scan(self):
        """المسح المتقدم الشامل"""
        self.ui.show_message("info", "المسح المتقدم - قيد التطوير")
        
    def instagram_operations(self):
        """عمليات انستجرام"""
        self.ui.show_message("info", "وحدة انستجرام - قيد التطوير")
        
    def system_settings(self):
        """إعدادات النظام"""
        settings = self.ui.settings_menu()
        self.ui.show_message("success", f"تم تطبيق الإعدادات: {settings}")

def main():
    """الدالة الرئيسية للتشغيل"""
    try:
        app = SocialMapperPro()
        app.run()
    except Exception as e:
        print(f"❌ فشل تشغيل النظام: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()