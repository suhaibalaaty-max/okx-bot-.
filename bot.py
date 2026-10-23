import os, time, ccxt

# جلب المفاتيح بأمان من متغيرات السيرفر السحابي
api_key = os.getenv('OKX_API_KEY')
secret = os.getenv('OKX_SECRET_KEY')
passphrase = os.getenv('OKX_PASSPHRASE')

exchange = ccxt.okx({
    'apiKey': api_key,
    'secret': secret,
    'password': passphrase,
    'enableRateLimit': True
})

print("🚀 بدأ تشغيل بوت التداول على السيرفر السحابي...")

while True:
    try:
        # فحص الاتصال وجلب الرصيد للتأكد من عمل البوت
        balance = exchange.fetch_balance()
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] الاتصال ممتاز | رصيد USDT: {balance['total'].get('USDT', 0)}")
        
        # الانتظار لمدة 15 دقيقة قبل التكرار التالي
        time.sleep(900)
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")
        time.sleep(60)
