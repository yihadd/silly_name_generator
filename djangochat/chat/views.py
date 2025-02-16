from django.shortcuts import render
from django.http import JsonResponse
import random

# Lists of Thai first and last names (with funny/silly meanings)
FIRST_NAMES = (
    'ป้าพริก', 'ลุงกระเทียม', 'น้าหอม', 'ป้าส้มตำ', 'ลุงข้าวผัด',
    'น้องหมูกรอบ', 'พี่แกงส้ม', 'คุณต้มยำ', 'น้าผัดไทย', 'ป้าทอดมัน',
    'ลุงกล้วยทอด', 'พี่ขนมจีน', 'น้องข้าวเหนียว', 'คุณมะม่วง', 'ป้าทุเรียน',
    'ลุงมะพร้าว', 'น้าสับปะรด', 'พี่แตงโม', 'คุณส้มโอ', 'ป้าลำไย',
    'น้องมังคุด', 'พี่ระกำ', 'คุณลิ้นจี่', 'ป้าเงาะ', 'ลุงขนุน',
    'น้าน้ำปลา', 'พี่ซีอิ๊ว', 'คุณพริกไทย', 'ป้าขิง', 'ลุงข่า'
)

LAST_NAMES = (
    'กินจุ', 'อิ่มดี', 'หิวจัง', 'อร่อยจริง', 'เผ็ดมาก',
    'หวานใจ', 'เปรี้ยวปาก', 'ขมนิด', 'เค็มนิดหน่อย', 'จืดชืด',
    'มันมาก', 'ชาบู', 'สุกี้', 'บุฟเฟ่ต์', 'กินได้',
    'ทานเก่ง', 'หม้อไฟ', 'ย่างเนย', 'ต้มแซ่บ', 'ผัดเผ็ด',
    'แกงป่า', 'ลาบก้อย', 'น้ำตก', 'ส้มตำ', 'ยำยำ',
    'ต้มยำ', 'แกงเขียว', 'ผัดกะเพรา', 'ราดหน้า', 'ผัดซีอิ๊ว'
)

def home(request):
    return render(request, 'home.html')

def generate_name(request):
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    
    response = JsonResponse({
        'first_name': first_name,
        'last_name': last_name
    })
    # Add CORS headers for cross-domain requests
    response["Access-Control-Allow-Origin"] = "https://yihadd.github.io/silly_name_generator/"  # Allow all domains (not recommended for production)
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# Remove unused functions
# Removing: room, checkview, send, getMessages