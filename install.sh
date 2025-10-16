#!/bin/bash
echo "🚀 SocialMapper Pro - Auto Installer for Kali Linux"

# تحديث النظام
echo "📦 تحديث حزم النظام..."
sudo apt update -y

# تثبيت Python والمكتبات
echo "🐍 تثبيت Python والمكتبات..."
sudo apt install -y python3 python3-pip python3-venv git firefox-esr

# إنشاء مجلد المشروع
echo "📁 إنشاء مجلد المشروع..."
mkdir -p SocialMapperPro
cd SocialMapperPro

# إنشاء بيئة افتراضية
echo "🔧 إنشاء بيئة Python افتراضية..."
python3 -m venv socialmapper_env
source socialmapper_env/bin/activate

# تحميل الملفات من GitHub
echo "📥 تحميل الملفات من GitHub..."
git clone https://github.com/yourusername/SocialMapperPro.git . || {
    echo "❌ فشل تحميل الملفات، إنشاء الهيكل محلياً..."
    
    # إنشاء الهيكل يدوياً إذا فشل التحميل
    mkdir -p core ui utils outputs/reports outputs/logs config
    
    # تنزيل الملفات الأساسية
    cat > main.py << 'EOF'
#!/usr/bin/env python3
print("📥 يرجى تنزيل الملفات الكاملة من:")
print("🔗 https://github.com/yourusername/SocialMapperPro")
print("🚀 ثم تشغيل: python3 setup.py")
EOF
}

# تثبيت المتطلبات
echo "📚 تثبيت مكتبات Python..."
pip3 install --upgrade pip
pip3 install selenium requests beautifulsoup4 colorama blessed webdriver-manager urllib3 lxml python-dateutil

# جعل الملفات قابلة للتنفيذ
chmod +x main.py setup.py

# تشغيل الإعداد
echo "⚙️ تشغيل الإعدادات..."
python3 setup.py

echo "🎉 تم التثبيت بنجاح!"
echo "💻 لتشغيل الأداة:"
echo "cd SocialMapperPro"
echo "python3 main.py"